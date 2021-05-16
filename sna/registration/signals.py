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
record their social media usage daily.

An email from research manager will allocate you to one of methods which you will be using for
the duration of these thirty days.
Facebook, YouTube, and Instagram are the only social media apps which are used for the
study.

If you continue the excessive use of social, continue recording the data.

You will be contacted for an interview after the completion of the experiment.

Login at http://snar-309908.lm.r.appspot.com/

Thank you and good luck!

REMINDER: if you fail to follow the instructions for thirty days and end up using social media
as you normally do, please continue recording the amount of hours you do so until the
experiment has reached its thirty day limit.

SNAR team
'''


@receiver(signal=post_save, sender=User)
def send_welcome_mail(sender: User, instance: User, created: bool, **kwargs) -> None:
    ''''''
    if created:
        with get_connection() as conn:
            EmailMessage(
                MESSAGE_TITLE,
                MESSAGE_BODY.format(name=instance.username),
                settings.EMAIL_HOST_USER,
                (instance.email,),
                connection=conn
            ).send()