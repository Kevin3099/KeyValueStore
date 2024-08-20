document.getElementById('setForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const key = document.getElementById('setKey').value;
    const value = document.getElementById('setValue').value;
    const response = await fetch(`/store/${key}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: value }),
    });
    const result = await response.json();
    document.getElementById('setResult').textContent = JSON.stringify(result);
});

document.getElementById('getForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const key = document.getElementById('getKey').value;
    const response = await fetch(`/store/${key}`, {
        method: 'GET',
    });
    const result = await response.json();
    document.getElementById('getResult').textContent = JSON.stringify(result);
});

document.getElementById('deleteForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const key = document.getElementById('deleteKey').value;
    const response = await fetch(`/store/${key}`, {
        method: 'DELETE',
    });
    const result = await response.json();
    document.getElementById('deleteResult').textContent = JSON.stringify(result);
});
