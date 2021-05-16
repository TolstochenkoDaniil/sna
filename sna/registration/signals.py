from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, get_connection


MESSAGE_TITLE= 'Welcome to snar'
MESSAGE_BODY = '''
Dear {name},

Thank you for registering for this experiment!

The purpose of this experiment is to identify the most effective method of preventing excessive
social media use. Three methods will be tested in this experiment:
1. Time restriction
2. Notification blocker
3. Delete apps.

The duration of the experiment is 30 days during which all the participants are required to
record their social media usage.
A member of the research group will be in touch with you shortly to allocate you to one of
below methods.

Login at http://snar-309908.lm.r.appspot.com/

Best regards,
SNAR team
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