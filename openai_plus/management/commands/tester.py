# -*- coding: utf-8 -*-
from logging import getLogger
from django.core.management.base import BaseCommand

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "Listens to Digio webhook and processes them"

    def handle(self, *args, **options):
        _ = [args, options]
        print("heheeh")
        logger.info("Starting digio worker with queue:")

