<template>
  <div id="app">
    <div id="chatbot">
      <div id="chatbot-header">
        <h2>LAW GPT</h2>
      </div>
      <div id="chatbot-messages">
        <div v-for="message in messages" :class="['message', message.type + '-message']">{{ message.text }}</div>
      </div>
      <div id="chatbot-input">
        <input type="text" v-model="userInput" @keyup.enter="sendMessage" id="user-input" placeholder="write to know...">
        <button @click="sendMessage" id="send-button">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: '',
      messages: [
        { text: 'Hello! How can I assist you with legal judgements today?', type: 'bot' }
      ]
    };
  },
  methods: {
    sendMessage() {
      if (this.userInput.trim() !== "") {
        this.messages.push({ text: this.userInput, type: 'user' });
        this.userInput = '';

        // Simulate bot response
        setTimeout(() => {
          this.messages.push({ text: 'The page is under construction. Please wait for a while. Thank you for your patience.', type: 'bot' });
          this.$nextTick(() => {
            const messagesContainer = this.$el.querySelector('#chatbot-messages');
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
          });
        }, 500);
      }
    }
  }
};
</script>

<style scoped>
#chatbot {
  display: grid;
  grid-template-rows: auto 1fr auto;
  width: 100%;
  max-width: 100%;
  height: 100vh;
  max-height: 100vh;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
  margin: 0 auto;
}
#chatbot-header {
  background-color: #f1f1f1;
  color: burlywood;
  width: 100%;
  height: 115px;
  padding: 0;
  text-align: center;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
#chatbot-messages {
  padding: 10px;
  overflow-y: auto;
}
.message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 5px;
}
.bot-message {
  background-color: #f1f1f1;
  align-self: flex-start;
}
.user-message {
  background-color: #dcf8c6;
  align-self: flex-end;
}
#chatbot-input {
  display: flex;
  border-top: 1px solid #ccc;
  width: 75%;
  justify-content: center;
  align-items: center;
  height: 25px;
  padding: 10px;
  margin: 0 auto;
}
#user-input {
  flex: 1;
  background-color: #f1f1f1;
  padding: 10px;
  border: 1px solid #ccc;
  border-bottom-left-radius: 10px;
}
#send-button {
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  border-bottom-right-radius: 10px;
}
#send-button:hover {
  background-color: #45a049;
}
</style>
</html>