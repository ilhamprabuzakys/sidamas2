import random
import string
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from . import models

@receiver(post_save, sender=User)
def set_password_on_user_creation(sender, instance, created, **kwargs):
    if created and not instance.password:
        password = generate_random_password()
        send_user_creation_email(instance, password, 'Registrasi Akun')

        instance.set_password(password)
        instance.save()

@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        satker_id = kwargs.get('satker_id')
        notelp = kwargs.get('notelp')
        role = kwargs.get('direktorat')

        profile, created = models.Profile.objects.get_or_create(
            user=instance,
            defaults={
                'satker': satker_id,
                'role': role,
                'notelp': notelp
            }
        )

        if created:
            print(f'INFO : User {instance.username} belum memiliki Profile')
        else:
            print(f'INFO : User sudah memiliki Profile dengan ID {profile.pk}')
            profile.satker_id = satker_id
            profile.role = role
            profile.notelp = notelp
            profile.save()

@receiver(post_save, sender=User)
def update_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        print(f'INFO : Triggered Update For Model Profile')
        instance.profile.save()

def generate_random_password(length: int = 8) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def send_user_creation_email(instance, password, subject):
    from_email = 'SIDAMAS <no-reply-sidamas@bnn.go.id>'
    receiver_list = [instance.email]

    html_body = render_to_string('users/emails/email_data_akun.html', {
        'user': instance, 'password' : password
    })

    email = EmailMultiAlternatives(
        subject=subject,
        body=html_body,
        from_email=from_email,
        to=receiver_list,
    )
    email.attach_alternative(html_body, "text/html")

    email.send(fail_silently=False)