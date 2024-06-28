# your_app/management/commands/remove_duplicates.py

from django.core.management.base import BaseCommand
from django.db.models import Count
from task_62_app.models import UserProfile


class Command(BaseCommand):
    help = 'Remove duplicate UserProfile instances'

    def handle(self, *args, **kwargs):
        # Find duplicate UserProfiles
        duplicates = UserProfile.objects.values('user').annotate(count=Count('id')).filter(count__gt=1)

        for duplicate in duplicates:
            profiles = UserProfile.objects.filter(user=duplicate['user'])
            # Keep the first instance, delete the rest individually
            for profile in profiles[1:]:
                profile.delete()
                self.stdout.write(self.style.SUCCESS(f'Removed duplicate profile for user: {duplicate["user"]}'))
