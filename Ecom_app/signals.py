from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enquiry
from django.core.mail import send_mail
from .views import confirm_enquiry_email, admin_confirm_email

@receiver(post_save, sender=Enquiry)
def EnquiryEmailSender(sender, instance, created, **kwargs):
     if created:
        confirm_enquiry_email(instance)
        admin_confirm_email(instance)
        
        
        """ subject = 'Thank you for you enquiry'
        message = f'Hi {instance.first_name} {instance.last_name},\n\n We have received your enquiry with regards to {instance.product.name}. We will soon reach out to you. Thank you!!!'
        from_email = 'vinod@example.com'
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)

        #Email notification for the administrators

        subject_admin = f'New Enquiry for {instance.product.name}'
        message_admin = f'Enquiry Details:\n\nFirst Name: {instance.first_name}\nLast Name: {instance.last_name}\nEmail: {instance.email}\nMobile: {instance.mobile}\nProduct: {instance.product.name}\nMessage: {instance.message}'
        from_email_admin = 'vinod@example.com'
        recipient_list_admin = ['admin@example.com','prajwal@example.com']
        send_mail(subject_admin, message_admin, from_email_admin, recipient_list_admin) """
