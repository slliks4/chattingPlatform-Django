window.addEventListener('beforeunload', function() {
    var chatContainer = document.getElementById('chat-container');
    if (chatContainer) {
        localStorage.setItem('chatScrollPosition', chatContainer.scrollTop);
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var chatContainer = document.getElementById('chat-container');
    if (chatContainer) {
        var scrollPosition = localStorage.getItem('chatScrollPosition');
        if (scrollPosition !== null) {
            chatContainer.scrollTop = parseInt(scrollPosition, 10);
            localStorage.removeItem('chatScrollPosition'); // Clear the stored position
        }
    }
});