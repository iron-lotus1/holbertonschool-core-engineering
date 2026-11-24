#!/usr/bin/node

const socket = new WebSocket("ws://" + window.location.host + "/ws");

const messages = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");

// Display connection status
socket.onopen = function() {
    addMessage("Connected to server");
};

// Receive messages from server
socket.onmessage = function(event) {
    addMessage(event.data);
};

// Handle connection errors
socket.onerror = function() {
    addMessage("Connection error");
};

// Handle connection closing
socket.onclose = function() {
    addMessage("Disconnected from server");
};

// Display messages on the page
function addMessage(message) {
    const newMessage = document.createElement("p");

    newMessage.textContent = message;

    messages.appendChild(newMessage);

    messages.scrollTop = messages.scrollHeight;
}

// Send message to server
function sendMessage() {
    const message = messageInput.value;

    if (message.trim() !== "" && socket.readyState === WebSocket.OPEN) {
        socket.send(message);

        messageInput.value = "";
    }
}

// Send button
sendButton.addEventListener("click", sendMessage);

// Allow Enter key to send messages
messageInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
