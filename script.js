document.addEventListener('DOMContentLoaded', (event) => {
    const sendButton = document.getElementById('send-button');
    const userInput = document.getElementById('user-input');
    const chatbotMessages = document.getElementById('chatbot-messages');

    sendButton.addEventListener('click', () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            addMessageToChat('user', userMessage);
            userInput.value = '';
            getBotResponse(userMessage);
        }
    });

    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendButton.click();
        }
    });

    function addMessageToChat(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);
        messageElement.textContent = message;
        chatbotMessages.appendChild(messageElement);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    function getBotResponse(userMessage) {
        // Simulate a bot response after a delay
        setTimeout(() => {
            const botMessage = `You said: ${userMessage}`;
            addMessageToChat('bot', botMessage);
        }, 1000);
    }
});
