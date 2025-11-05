import logging

from django.apps import apps
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver


@receiver(user_logged_out)
def cleanup_demo_data(sender, request, user, **kwargs):
    """ Clear demo app data when the user logout. """
    if user:
        models_to_clean = [
            "outflows.Outflow",
            "inflows.Inflow",
            "products.Product",
            "suppliers.Supplier",
            "brands.Brand",
            "categories.Category",
        ]

        for model_path in models_to_clean:
            logger = logging.getLogger("django_console")
            try:
                app_label, model_name = model_path.split(".")
                Model = apps.get_model(app_label, model_name)
                Model.objects.all().delete()
                logger.info(
                    "All data has been removed for the demo app."
                )
            except Exception as e:
                logger.error(f"Error to cleanup demo data: {e}")
