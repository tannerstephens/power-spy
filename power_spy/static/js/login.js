window.onload = () => {
    const passwordField = document.getElementById('password');
    const form = document.getElementById('form');
    const invalid = document.getElementById('invalid');

    form.onsubmit = e => {
        e.preventDefault();

        invalid.classList.add('is-invisible')

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
                } else {
                    invalid.classList.remove('is-invisible')
                }
            })
    }
}
