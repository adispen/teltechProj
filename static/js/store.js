var $loginModal = $('#loginModal');

function setUsername () {
    username = cleanInput($usernameInput.val().trim());
    email = cleanInput($emailInput.val().trim());
    if (username && email) {
        $loginModal.modal('toggle');
        $chatPage.show();
        $currentInput = $inputMessage.focus();
        var payload = {
            'username' : username,
            'email' : email,
            'rep' : false
        };

        // Tell the server your username
        socket.emit('add user', payload);
    }

}

$loginModal.on('hidden.bs.modal', function(){
    if (!$chatPage.is(':visible')){
        $('#invite-button').show();
    }
});
$('#invite-button').click(function() {
    $loginModal.modal('toggle');
    $('#invite-button').hide();
});
$('#menu-button').click(function() {
    $('#menu-glyph').toggleClass('glyphicon-plus').toggleClass('glyphicon-minus');
});
