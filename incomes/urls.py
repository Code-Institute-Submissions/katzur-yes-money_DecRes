from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="income"),
    path('add-income', views.add_income, name="add-income"),
    path('edit-income/<int:id>', views.income_edit, name="income-edit"),
    path('income-delete/<int:id>', views.delete_income, name="income-delete"),
    path(
        'delete-confirmation-income/<int:id>',
        views.delete_confirmation_income, name="delete-confirmation-income"),
    path('search-income', csrf_exempt(
        views.search_income), name="search_income"),
    path(
        'income_source_summary',
        views.income_source_summary, name="income_source_summary"),
    path('stats-income', views.stats_income_view, name="stats-income"),
    path(
        'export_csv_income',
        views.export_csv_income, name="export-csv-income"),
]
