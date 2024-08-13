from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from travel_tour.models import Tour 

@receiver(post_save, sender=Tour)
def send_tour_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'Новый тур добавлен'
        message = f'Новый тур "{instance.name}" был успешно добавлен!\n\nОписание: {instance.description}\nЦена: {instance.price}'
        email_from = 'haydarovaziz840@gmail.com'
        recipient_list = ['hayd4rovaziz@yandex.ru']

        try:
            send_mail(subject, message, email_from, recipient_list)
            print("Email sent successfully")
        except Exception as e:
            print("Error sending email:", e)
