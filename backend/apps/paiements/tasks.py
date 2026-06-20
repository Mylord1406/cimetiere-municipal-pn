from celery import shared_task


@shared_task
def alertes_retard_paiement():
    from apps.paiements.models import Paiement
    from django.core.mail import send_mail
    from django.conf import settings
    from django.utils import timezone
    from datetime import timedelta

    date_limite = timezone.now() - timedelta(days=7)

    paiements_retard = Paiement.objects.filter(
        statut="EN_ATTENTE",
        date_paiement__lt=date_limite,
    ).select_related("reservation__client")

    nb = 0
    for p in paiements_retard:
        try:
            client = p.reservation.client if p.reservation else None
            if not client:
                continue
            send_mail(
                subject="⚠️ Retard de paiement — Cimetière Municipal de Pointe-Noire",
                message=f"""Bonjour {client.prenom} {client.nom},

Nous vous informons que votre paiement de {int(p.montant_xaf):,} FCFA (réf. {p.reference}) est en attente depuis plus de 7 jours.

Veuillez régulariser votre situation au plus vite.

Cordialement,
Cimetière Municipal de Pointe-Noire""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[client.email],
                fail_silently=True,
            )
            nb += 1
        except Exception:
            pass

    return f"{nb} alertes retard paiement envoyées."