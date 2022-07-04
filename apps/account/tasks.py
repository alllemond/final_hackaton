
from project.celery import app
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail



@app.task
def send_activation_code(email, activation_code):
        message = f""" Thank you for registering in our site.
                        Your link for activation is: http://localhost:8000/account/activate/{activation_code}/ """

        send_mail(
            "Account Activation",
            message,
            EMAIL_HOST_USER,
            [email],
        )