document.getElementById('send-btn').addEventListener('click', function() {
    console.log("click");
    let userMessage = document.getElementById('user-input').value;

    if (userMessage.trim() === "") return;

    // Menampilkan pesan pengguna di chat box
    let chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div>User: ${userMessage}</div>`;
    document.getElementById('user-input').value = "";

    // Kirim pesan ke server Flask
    fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        // Menampilkan respons chatbot
        let chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<div>Chatbot: ${data.response[0].text}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll ke bawah
    })
    .catch(error => console.error('Error:', error));
});
