from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, get_connection


MESSAGE_TITLE= 'Welcome to snar'
MESSAGE_BODY = '''
    Hello, {name}!

    We\'re glad you\'ve decided to participate in our research.
    '''


@receiver(signal=post_save, sender=User)
def send_welcome_mail(sender: User, instance: User, created: bool, **kwargs) -> None:
    ''''''
    if created:
        with get_connection() as conn:
            EmailMessage(
                MESSAGE_TITLE,
                MESSAGE_BODY.format(name=instance.first_name),
                settings.EMAIL_HOST_USER,
                (instance.email,),
                connection=conn
            ).send()