const glass = document.querySelector('.chat__input_glass'),
      chat = document.querySelector('.chat__messages-area');

let id = 1;


function sendUserMessage(){
    const input = document.querySelector('.chat__input');
    if (input.value.length > 0 && input.value.length <= 45)
    {
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
    }
}

sendBotTextMessage(`Привет, меня зову Бот. Я помогу тебе подобрать страну для переезда или путешествия!`);
sendBotTextMessage(`Я умею так:`);
sendBotTextMessage(`Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit sunt corporis illo ipsum quod sint, dolorem consequuntur eaque ipsam quia culpa earum repellat magnam veniam tempore architecto ducimus cum pariatur.
Lorem ipsum dolor, sit amet consectetur adipisicing elit. Doloribus laudantium, maxime vel velit dignissimos officia vitae placeat soluta laborum doloremque laboriosam nemo, libero tenetur, explicabo officiis. Ducimus eaque cumque debitis!
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error, natus doloribus? Earum esse, quo pariatur ab nobis culpa dolorum, a odit corporis est doloribus, harum qui tenetur porro minus ex?`);

// Events

document.addEventListener('keyup', (event) => {
    if (event.key == 'Enter')
    {
        sendUserMessage();
    }
});

document.addEventListener('click', (event) => {
    if (event.target == glass)
    {
        sendUserMessage();
    }
});
