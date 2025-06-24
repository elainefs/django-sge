import logging

from django.core.management.base import BaseCommand

from ai.agent import SGEAgent


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger = logging.getLogger("django_console")
        try:
            agent = SGEAgent()
            agent.invoke()
            logger.info("AI Agent successfully invoked.")
        except Exception as ex:
            logger.error(f"Error invoking AI Agent: {ex}")
