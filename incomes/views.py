from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userpreferences.models import UserPreference
import json
from django.http import JsonResponse, HttpResponse
from .models import Source, Income
import datetime
import csv


# Create your views here.


def search_income(request):
    """
    Function which allows to search incomes
    """
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        income = Income.objects.filter(
            amount__istartswith=search_str, owner=request.user
            ) | Income.objects.filter(
            date__istartswith=search_str, owner=request.user
            ) | Income.objects.filter(
            description__icontains=search_str, owner=request.user
            ) | Income.objects.filter(
            source__icontains=search_str, owner=request.user)
        data = income.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url='/authentication/login')
def index(request):
    """
    Function bringing information to the table
    """
    categories = Source.objects.all()
    income = Income.objects.filter(owner=request.user)
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    try:
        currency = UserPreference.objects.get(user=request.user).currency
    except UserPreference.DoesNotExist:
        currency = 'EUR - Euro'
    context = {
        'income': income,
        'page_obj': page_obj,
        'currency': currency
    }
    return render(request, 'income/index.html', context)


@login_required(login_url='/authentication/login')
def add_income(request):
    """
    Function allowing to add income
    """
    sources = Source.objects.all()
    context = {
        'sources': sources,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'income/add_income.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/add_income.html', context)
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'income/add_income.html', context)

        Income.objects.create(
            owner=request.user, amount=amount,
            date=date, source=source, description=description)
        messages.success(request, 'Income saved successfully')

        return redirect('income')


@login_required(login_url='/authentication/login')
def income_edit(request, id):
    """
    Function allowing to edit income
    """
    income = Income.objects.get(pk=id)
    sources = Source.objects.all()
    context = {
        'income': income,
        'values': income,
        'sources': sources
    }
    if request.method == 'GET':
        return render(request, 'income/edit_income.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/edit_income.html', context)
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'income/edit_income.html', context)
        income.amount = amount
        income.date = date
        income.source = source
        income.description = description

        income.save()
        messages.success(request, 'Income updated successfully')

        return redirect('income')


@login_required(login_url='/authentication/login')
def delete_income(request, id):
    """
    Function allowing to delete income
    """
    if not Income.owner != request.user:
        messages.info(request, 'You are not the owner of this income')
        return redirect('home')

    income = Income.objects.get(pk=id)
    income.delete()
    messages.success(request, 'Income removed')
    return redirect('income')


@login_required(login_url='/authentication/login')
def delete_confirmation_income(request, id):
    """
    Function for delete confirmation page
    """
    income = Income.objects.get(pk=id)
    context = {'income': income}

    if request.method == "POST":
        income.delete()
        return redirect('income')

    return render(request, 'income/delete-confirmation-income.html', context)


def income_source_summary(request):
    """
    Function summarizing income over last 6 months for the chart view
    """
    todays_date = datetime.date.today()
    six_months_ago = todays_date-datetime.timedelta(days=30*6)
    income = Income.objects.filter(
        owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {

    }

    def get_source(income):
        """
        Function for the chart getting sources
        """
        return income.source
    source_list = list(set(map(get_source, income)))

    def get_income_source_amount(source):
        """
        Function for the chart getting amounts per source
        """
        amount = 0
        filtered_by_source = income.filter(source=source)

        for item in filtered_by_source:
            amount += item.amount
        return amount

    for x in income:
        for y in source_list:
            finalrep[y] = get_income_source_amount(y)

    return JsonResponse({'income_source_data': finalrep}, safe=False)


def stats_income_view(request):
    """ Function returns the expenses chart page """
    return render(request, 'income/stats-income.html')


def export_csv_income(request):
    """
    Function allowing to export CSV files
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Income' + str(
        datetime.datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Amount', 'Description', 'Source', 'Date'])

    income = Income.objects.filter(owner=request.user)

    for income in income:
        writer.writerow([
            income.amount, income.description, income.source, income.date])

    return response
