from django.apps import AppConfig


class Django2Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django2"

    def ready(self) -> None:
        import django2.signals  # noqa: F401
