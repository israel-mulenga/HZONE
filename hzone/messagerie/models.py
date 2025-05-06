from django.conf import settings
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")  # ✅ Expéditeur
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_messages")  # ✅ Destinataire
    content = models.TextField()  # ✅ Contenu du message
    timestamp = models.DateTimeField(auto_now_add=True)  # ✅ Date d'envoi

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content[:20]}"
