var $currentInput = $usernameInput.focus();

// Sets the client's username
function setUsername () {
    username = cleanInput($usernameInput.val().trim());
    email = cleanInput($emailInput.val().trim());
    if (username && email) {
        $loginPage.fadeOut();
        $chatPage.show();
        $loginPage.off('click');
        $currentInput = $inputMessage.focus();
        var payload = {
            'username' : username,
            'email' : email,
            'rep' : true
        };

        // Tell the server your username
        socket.emit('add user', payload);
    }
}
