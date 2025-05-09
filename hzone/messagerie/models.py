from django.conf import settings
from django.db import models
from hzone_app.models import Listing  # ✅ Import du modèle Listing

class Discussion(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="discussions")  # ✅ Lien avec l’annonce
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_discussions")  # ✅ Propriétaire du bien
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="client_discussions")  # ✅ Client qui initie la discussion
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Date de création

    def __str__(self):
        return f"Discussion sur {self.listing.title} entre {self.owner.username} et {self.client.username}"

class Message(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="messages")  # ✅ Lien avec la discussion
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")  # ✅ Expéditeur
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_messages")  # ✅ Destinataire
    content = models.TextField()  # ✅ Contenu du message
    timestamp = models.DateTimeField(auto_now_add=True)  # ✅ Date d'envoi

    def __str__(self):
        return f"{self.sender} -> {self.receiver} (Discussion sur {self.discussion.listing.title}): {self.content[:20]}"
