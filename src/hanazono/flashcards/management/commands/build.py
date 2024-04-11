import mkdocs.config
from django.core.management.base import BaseCommand
from mkdocs.commands import build

from hanazono.utils import logger

log = logger.custom(__name__)


class Command(BaseCommand):
    help = "Build site."

    def handle(self, *args, **options):
        config = mkdocs.config.load_config()
        build.build(config)
        log.info(f"""Site built in {config["site_dir"]}""")
