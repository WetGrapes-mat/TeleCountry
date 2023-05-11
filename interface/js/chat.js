const glass = document.querySelector('.chat__input_glass'),
      chat = document.querySelector('.chat__messages-area');

let id = 1;

let messagesList = [];
let botMessage = '';

async function getNewBotMessage(url, toPost) {
    try {
        console.log(JSON.stringify(toPost));
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(toPost),
            headers: {
                'Content-Type': 'application/json'
            }
        });
       
        const res = await response.json();
        const botNewMessageText = res.result;
        return botNewMessageText;
    } catch (error) {
       console.error(error);
    }
}

function findNearestBotMessage(currentIndex) {
    for (let i = currentIndex - 1; i >= 0; i--) {
      if (messagesList[i].sender === 'bot') {
        return messagesList[i].message;
      }
    }
    return null; // Если не найдено сообщение от бота
}

function sendUserMessage(){
    let messageContent = '';
    const input = document.querySelector('.chat__input');
    if (input.value.length > 0 && input.value.length <= 800)
    {
        messageContent = input.value;
        let message = document.createElement('div');
        message.className = "chat__message message-user";
        message.innerHTML = `
        <div class="chat__message_content">
        <div id="added-${id}" class="chat__message_text">
            ${input.value}
        </div>
        </div>
        <div class="chat__message_avatar">
            <img src="../img/chat/user.png" alt="user">
        </div>`;
        chat.prepend(message);
        const element = chat.querySelector(`#added-${id}`);
        const width = element.offsetWidth + 29;
        element.parentElement.style.width = `${width}px`
        id += 1;
        input.value = '';
    }
    messagesList.push({'sender': 'user', 'message': messageContent});
    const lastBotMessage = findNearestBotMessage(messagesList.length);
    getNewBotMessage('http://localhost:8080/chat', {"question": lastBotMessage, "answer": messageContent})
        .then(answer => {
            sendBotTextMessage(answer);
        })
}

function sendUserTextMessage(text){
    let message = document.createElement('div');
    message.className = "chat__message message-user";
    message.innerHTML = `
    <div class="chat__message_content">
    <div id="added-${id}" class="chat__message_text">
        ${text}
    </div>
    </div>
    <div class="chat__message_avatar">
        <img src="../img/chat/user.png" alt="user">
    </div>`;
    chat.prepend(message);
    const element = chat.querySelector(`#added-${id}`);
    const width = element.offsetWidth + 29;
    element.parentElement.style.width = `${width}px`
    id += 1;
    messagesList.push({'sender': 'user', 'message': text});
    const lastBotMessage = findNearestBotMessage(messagesList.length);
    getNewBotMessage('http://localhost:8080/chat', {"question": lastBotMessage, "answer": text})
        .then(answer => {
            sendBotTextMessage(answer);
        })
}

function sendBotTextMessage(text)
{
    if (typeof(text) === 'string')
    {
        let message = document.createElement('div');
        message.className = "chat__message message-bot";
        message.innerHTML = `
        <div class="chat__message_avatar">
            <img src="../img/chat/bot.png" alt="bot">
        </div>
        <div class="chat__message_content">
            <div class="chat__message_text">
                ${text}
            </div>
        </div>`;
        chat.prepend(message);
        messagesList.push({'sender': 'bot', 'message': text});
    }
}

sendBotTextMessage(`Привет, меня зову Бот. Я помогу тебе подобрать страну для переезда или путешествия!`);
// Events

document.addEventListener('keyup', (event) => {
    if (event.key == 'Enter')
    {
        sendUserMessage();
        event.preventDefault();
    }
});

document.addEventListener('click', (event) => {
    if (event.target == glass)
    {
        event.preventDefault();
        sendUserMessage();
    }
});

let isRecording = false;
const startRecordingUrl = 'http://localhost:8080//start_voice';
const stopRecordingUrl = 'http://localhost:8080//stop_voice';

const button = document.querySelector('.chat__input_micro');

button.addEventListener('click', async () => {
  if (!isRecording) {
    try {
        console.log('Запись голоса начата');
        isRecording = true;
        const startResponse = await fetch(startRecordingUrl)
        const data = await startResponse.json();
        const message = data;
        sendUserTextMessage(message.voice);
    } catch (error) {
      console.error('Ошибка при начале записи:', error);
    }
  } else {
    try {
        isRecording = false;
        console.log('Запись голоса завершена');
        const stopResponse = fetch(stopRecordingUrl);
      // Здесь обрабатываете ответ от сервера при завершении записи

        
      
    } catch (error) {
      console.error('Ошибка при завершении записи:', error);
    }
  }
});
