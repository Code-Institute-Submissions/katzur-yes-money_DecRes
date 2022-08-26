from django.apps import AppConfig


class IncomesConfig(AppConfig):
    """
    Class that defines plural name for 'Income' in Admin Panel
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'incomes'
