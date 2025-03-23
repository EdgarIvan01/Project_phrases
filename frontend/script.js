function getQuote() {
    fetch('http://localhost:5000/get-quote')  
        .then(response => response.json())    
        .then(data => {
            document.getElementById('quote').textContent = data.quote;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('quote').textContent = "Error al obtener la frase.";
        });
}