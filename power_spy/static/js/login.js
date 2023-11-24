window.onload = () => {
    const passwordField = document.getElementById('password');
    const form = document.getElementById('form');

    form.onsubmit = e => {
        e.preventDefault();

        fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({password: passwordField.value})
        })
            .then(response => response.json())
            .then(data => {
                if(data.success) {
                    window.location = '/'
                }
            })
    }
}
