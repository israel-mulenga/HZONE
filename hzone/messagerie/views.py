from django.shortcuts import render
from .models import Message, Discussion
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from hzone_app.models import Listing
User = get_user_model()

from django.shortcuts import render
from .models import Message, Discussion
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from hzone_app.models import Listing

User = get_user_model()
@login_required
def chat_view(request, listing_id, receiver_username):
    receiver = User.objects.get(username=receiver_username)
    listing = Listing.objects.get(id=listing_id) 

    # ✅ Vérifier si une discussion existe entre ces deux utilisateurs
    discussion, created = Discussion.objects.get_or_create(
        listing=listing,
        owner=listing.owner,
        client=request.user if request.user != listing.owner else receiver  # ✅ Assure que le client est bien celui qui consulte
    )

    messages = Message.objects.filter(discussion=discussion).order_by('-timestamp')

    return render(request, 'messagerie/chat.html', {
        'receiver': receiver,
        'receiver_photo': receiver.profile_photo.url if receiver.profile_photo and receiver.profile_photo.name else None,
        'listing': listing,
        'messages': messages,
        'discussion': discussion,
    })


@login_required
def get_chat_messages(request, discussion_id):
    try:
        discussion = Discussion.objects.get(id=discussion_id)  # ✅ Vérifie que la discussion existe

        # ✅ Récupère tous les messages liés à la discussion, peu importe qui les a envoyés
        messages = Message.objects.filter(discussion=discussion).order_by("timestamp")

        print(f"✅ Messages récupérés ({request.user.username}) :", list(messages))  # ✅ Debugging en terminal Django

        message_list = [
            {
                "sender": msg.sender.username,
                "receiver": msg.receiver.username,
                "content": msg.content,
                "timestamp": msg.timestamp
            }
            for msg in messages
        ]

        return JsonResponse({"messages": message_list}, safe=False)

    except Discussion.DoesNotExist:
        return JsonResponse({"error": "Discussion non trouvée"}, status=404)

    except Exception as e:
        return JsonResponse({"error": f"Erreur interne : {str(e)}"}, status=500)

@login_required
def list_discussions(request):
    discussions = Discussion.objects.filter(owner=request.user) | Discussion.objects.filter(client=request.user)

    for discussion in discussions:
        discussion.last_message = discussion.last_message()  # ✅ Ajoute la récupération du dernier message

    return render(request, 'messagerie/discussions.html', {
        'discussions': discussions,
    })

