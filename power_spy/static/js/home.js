window.onload = () => {
    const powerButton = document.getElementById('powerButton');
    const holdButton = document.getElementById('holdButton');

    const updateStatus = () => {
        fetch('/api/power')
            .then(response => response.json())
            .then(data => {
                if(data.status) {
                    powerButton.classList.remove('is-warning', 'is-danger');
                    powerButton.classList.add('is-success');

                    powerButton.innerHTML = '😄';
                    powerButton.disabled = true;
                } else {
                    powerButton.classList.remove('is-warning', 'is-success');
                    powerButton.classList.add('is-danger');

                    powerButton.innerHTML = '😓';
                    powerButton.disabled = false;
                }

                setTimeout(updateStatus, 1000);
            });
    };

    updateStatus();

    powerButton.onclick = () => {
        fetch('/api/power', {method: 'POST'});
        powerButton.disabled = true;
    };

    holdButton.onclick = () => {
        fetch('/api/reboot', {method: 'GET'});
        holdButton.disabled = true;
    }
}
