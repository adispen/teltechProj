var $emailInput = $('.emailInput'); // Input for email if on main page
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
            'email' : email
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

$(window).keydown(function (event) {
    // When the client hits ENTER on their keyboard
    if (event.which === 13) {
        if (username) {
            sendMessage();
            socket.emit('stop typing');
            typing = false;
        } else {
            // Check if fields are both filled in
            if ($emailInput.val() === '' || $usernameInput.val() === ''){
                alert('Please fill out both fields');
            } else {
                setUsername();
            }
        }
    }
});
