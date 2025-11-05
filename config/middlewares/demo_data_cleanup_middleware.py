import logging

from django.apps import apps
from django.contrib.sessions.models import Session
from django.utils import timezone

logger = logging.getLogger("django_console")


class DemoDataCleanupMiddleware:
    """Clear demo app data automatically."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.cleanup_expired_sessions_data()

        response = self.get_response(request)
        return response

    def cleanup_expired_sessions_data(self):
        expired_sessions = Session.objects.filter(expire_date__lt=timezone.now())

        if expired_sessions.exists():
            models_to_clean = [
                "outflows.Outflow",
                "inflows.Inflow",
                "products.Product",
                "suppliers.Supplier",
                "brands.Brand",
                "categories.Category",
            ]

            for model_path in models_to_clean:
                try:
                    app_label, model_name = model_path.split(".")
                    Model = apps.get_model(app_label, model_name)
                    Model.objects.all().delete()
                    logger.info("All data has been removed for the demo app.")
                except Exception as e:
                    logger.error(f"Error to cleanup demo data: {e}")

            expired_sessions.delete()
