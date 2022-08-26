from django.apps import AppConfig


class ExpensesConfig(AppConfig):
    """
    Class that defines plural name for 'Expense' in Admin Panel
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expenses'
