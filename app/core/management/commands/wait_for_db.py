"""
django command to wait for the db to be available
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """django command to wait for DB"""

    def handle(self, *args, **options):
        pass
