import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from members.models import Member

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = '''
    Migrate existing users created before the Member model was introduced to use a Member'''

    def handle(self, *args, **options):
        users = User.objects.all()

        for user in users:
            member = Member.objects.filter(user=user)
            if not member:
                Member.objects.create(user=user)

        logger.info('migrated all users to use members')
