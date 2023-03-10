
const form = document.querySelector('.chat-form');
const messages = document.querySelector('.chat-messages');
const button = document.querySelector('.chat-form button');
const input = document.querySelector('.chat-form input');

const handleSubmit = async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const question = formData.get('question');
  addUserMessage(question);
  const response = await getBotResponse(question);
  addBotMessage(response);
};

button.addEventListener('click', handleSubmit);

input.addEventListener('keydown', async (event) => {
  if (event.key === 'Enter') {
    handleSubmit(event);
  }
});
async function getBotResponse(question) {
    console.log('getBotResponse');
  const response = await fetch('/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ question })
  });
  const data = await response.json();
  return data.response;
}

// function addBotMessage(message) {
//   const messageEl = document.createElement('div');
//   messageEl.classList.add('chat-message', 'bot-message');
//   messageEl.innerHTML = `<p>${message}</p>`;
//   messages.appendChild(messageEl);
// }
function addBotMessage(message) {
    const messageEl = document.createElement('div');
    messageEl.classList.add('chat-message', 'bot-message');
    messageEl.innerHTML = `<p>${message}</p>`;
    messages.appendChild(messageEl);
  }

  function addUserMessage(message) {
    const messageEl = document.createElement('div');
    messageEl.classList.add('chat-message', 'user-message');
    messageEl.innerHTML = `<p>${message}</p>`;
    messages.appendChild(messageEl);
  }