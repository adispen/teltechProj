var $currentInput = $usernameInput.focus();

// Sets the client's username
function setUsername () {
    username = cleanInput($usernameInput.val().trim());
    if (username) {
        $loginPage.fadeOut();
        $chatPage.show();
        $loginPage.off('click');
        $currentInput = $inputMessage.focus();

        // Tell the server your username
        socket.emit('add rep', username);
    }
}

// Keyboard events

$(window).keydown(function (event) {
    // When the client hits ENTER on their keyboard
    if (event.which === 13) {
        if (username) {
            sendMessage();
            socket.emit('stop typing');
            typing = false;
        } else {
            setUsername();
        }
    }
});
