from django.core.mail import send_mail
from django.conf import settings


def envoyer_code_mfa(utilisateur, code: str) -> None:
    sujet = f"Votre code de connexion — {settings.APP_NAME}"
    message = f"Bonjour {utilisateur.prenom}, votre code est : {code}. Valable {settings.MFA_CODE_EXPIRY_MINUTES} minutes."
    send_mail(
        subject=sujet,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[utilisateur.email],
        fail_silently=False,
    )