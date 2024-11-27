function fetchData() {
    const category = document.getElementById('category').value;
    const endpoint = category ? `/data/${category}` : '/data';

    fetch(`http://127.0.0.1:5000${endpoint}`)
        .then(response => response.json())
        .then(data => displayData(data))
        .catch(error => console.error('Error:', error));
}

function displayData(data) {
    const display = document.getElementById('data-display');
    display.innerHTML = '';

    if (data.length === 0) {
        display.innerHTML = '<p>No hay datos para mostrar.</p>';
        return;
    }

    data.forEach(item => {
        const entry = document.createElement('div');
        entry.textContent = JSON.stringify(item);
        display.appendChild(entry);
    });
}
