const messages = document.querySelectorAll('.chat__message_text');

messages.forEach(message => {
    const width = message.offsetWidth + 29;
    message.parentElement.style.width = `${width}px`
});
