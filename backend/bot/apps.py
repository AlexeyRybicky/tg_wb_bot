"""
В модуле содержаться настройки приложения
"""

from django.apps import AppConfig


class BotConfig(AppConfig):
    """Настройки `bot` приложения"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
