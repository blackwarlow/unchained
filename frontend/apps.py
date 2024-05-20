from django.apps import AppConfig
from django.core import checks

from frontend.core.asset_loader import DjangoViteAssetLoader


class DjangoViteAppConfig(AppConfig):
    name = "frontend"
    verbose_name = "Frontend"

    def ready(self) -> None:
        # Make Loader instance at startup to prevent threading problems
        # but do not crash while doing so.
        DjangoViteAssetLoader.instance()

        # Check for potential errors with loading manifests in DjangoViteConfigs.
        checks.register(check_loader_instance, checks.Tags.staticfiles)


def check_loader_instance(**kwargs):
    return DjangoViteAssetLoader.instance().check(**kwargs)
