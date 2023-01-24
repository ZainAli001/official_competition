from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(user_logged_in, sender = User)
def sender_signal(sender,request,user, **kwargs):
    print('-----------------------------')
    print('Sender is :', sender)
    print('Request passed is :', request)
    print('User who sends signal: ', user)
    print(f'kwargs: {kwargs}')

@receiver(user_login_failed)
def user_login_fail_signal(sender,request,credentials, **kwargs):
    print('-----------------------------')
    print('Sender is :', sender)
    print('Request passed is :', request)
    print('User who sends signal: ', credentials)
    print(f'kwargs: {kwargs}')



# user_logged_in.connect(sender_signal, sender=User)