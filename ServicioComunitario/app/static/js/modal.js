  const btn_reserva = document.getElementById('btn_reserva');
    const container_reserva = document.querySelector('.container-reserva');
    const btn_cerrarR = document.getElementById('btn-cerrarReserva');

    btn_reserva.addEventListener('click', () => {
        container_reserva.style.visibility = 'visible';
        container_reserva.style.opacity = '1';
    });

    btn_cerrarR.addEventListener('click', () => {
        container_reserva.style.visibility = 'hidden';
        container_reserva.style.opacity = '0';
    });

    container_reserva.addEventListener('click', (e) => {
        if (e.target.classList.contains('container-reserva')) {
            container_reserva.style.visibility = 'hidden';
            container_reserva.style.opacity = '0';
        }
    });