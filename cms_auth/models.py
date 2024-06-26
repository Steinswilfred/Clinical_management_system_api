from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token


# Create a signal which receives the post request from the auth user model
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        # If the post request from the user model is valid
        # Then create a token
        Token.objects.create(user=instance)
