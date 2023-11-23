window.onload = () => {
    const checkReload = () => {
        fetch('/api/updating')
            .then(response => response.json())
            .then(data => {
                if(!data.updating) {
                    window.location = '/';
                }
            });

        setTimeout(checkReload, 5000);
    }

    fetch('/api/update')
        .then(response => response.json())
        .then(data => {
            if(data.updatable) {
                fetch('/api/update', {method: 'POST'})
                    .then(checkReload);
            } else {
                window.location = '/';
            }
        });
};
