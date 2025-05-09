document.addEventListener('DOMContentLoaded', function() {
    const burgerMenu = document.querySelector('.burger-menu');
    const navLinks = document.querySelector('.nav-links');

    burgerMenu.addEventListener('click', function() {
        this.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    document.addEventListener('click', function(e) {
        if (!burgerMenu.contains(e.target) && !navLinks.contains(e.target)) {
            burgerMenu.classList.remove('active');
            navLinks.classList.remove('active');
        }
    });

    // ✅ Récupérer le destinataire depuis l’URL Django
    let receiver = document.getElementById("receiver_username").textContent;
    let socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/" + receiver + "/");

    socket.onopen = function() {
        console.log("✅ Connexion WebSocket établie avec " + receiver);
    };

    socket.onmessage = function(event) {
        let data = JSON.parse(event.data);
        addMessage({
            sender: data.sender,
            content: data.message,
            time: new Date(data.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        });
    };

    document.getElementById("sendButton").addEventListener("click", sendMessage);
    document.getElementById("messageInput").addEventListener("keypress", function(e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        let messageInput = document.getElementById("messageInput");
        let messageContent = messageInput.value.trim();

        if (messageContent === "") return;

        socket.send(JSON.stringify({receiver: receiver, message: messageContent}));

        addMessage({
            sender: "Moi",
            content: messageContent,
            time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        });

        messageInput.value = "";
    }

    function addMessage(message) {
        const messageDiv = document.createElement("div");
        messageDiv.className = `message ${message.sender === "Moi" ? "sent" : "received"}`;

        const messageContentDiv = document.createElement("div");
        messageContentDiv.className = "message-content";

        const messageText = document.createElement("p");
        messageText.textContent = message.content;

        const messageTime = document.createElement("span");
        messageTime.className = "message-time";
        messageTime.textContent = message.time;

        messageContentDiv.appendChild(messageText);
        messageContentDiv.appendChild(messageTime);
        messageDiv.appendChild(messageContentDiv);

        document.getElementById("chatMessages").appendChild(messageDiv);

        document.getElementById("chatMessages").scrollTop = document.getElementById("chatMessages").scrollHeight;
    }

    // ✅ Charger les anciens messages depuis Django
    fetch(`/chat/messages/${receiver}/`)
        .then(response => response.json())
        .then(messages => {
            messages.forEach(msg => {
                addMessage({
                    sender: msg.sender,
                    content: msg.content,
                    time: new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                });
            });
        });
});
