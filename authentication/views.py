import json
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth
from django.core.mail import send_mail


# Create your views here.


class EmailValidationView(View):
    def post(self, request):
        """
        Function which will validate the email
        """
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({
                'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({
                'email_error': 'Email in use, choose another one'}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        """
        Function which will validate the username
        """
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({
                'username_error': 'Use alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                'username_error': 'Username used, try other one'}, status=409)
        return JsonResponse({'username_valid': True})


class RegistrationView(View):
    def get(self, request):
        """ Returns registration page """
        return render(request, 'authentication/register.html')

    def post(self, request):
        """
        Registration form function
        """
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(
                        request, 'authentication/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(
                    request, 'Account successfully created! Try to log in.')
                return render(request, 'authentication/register.html')

        return render(request, 'authentication/register.html')


class LoginView(View):
    def get(self, request):
        """ Returns login page """
        return render(request, 'authentication/login.html')

    def post(self, request):
        """
        Login form function
        """
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(
                        request, 'Hi, '+user.username+' You are now logged in')
                    return redirect('expenses')

            messages.error(
                request, 'Account nonexistent or wrong credentials. Try again')
            return render(request, 'authentication/login.html')


class IndexView(View):
    def get(self, request):
        """ Returns index page """
        return render(request, 'index.html')


class LogoutView(View):
    def post(self, request):
        """
        Logout function redirecting to index page
        """
        auth.logout(request)
        messages.success(request, 'You have been successfully logged out')
        return redirect('index')


class ContactView(View):
    def get(self, request):
        """ Returns contact page """
        return render(request, 'authentication/contact.html')


def contact(request):
    """
    Contact form functiom
    """
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'YESMoney Contact Form message from' + message_name,
            message,
            message_email,
            ['test@test.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been successfully sent!')
        return redirect('index')

    else:
        return render(request, 'authentication/contact.html')
