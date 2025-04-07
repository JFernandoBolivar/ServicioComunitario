const btn_exit = document.getElementById("btn_exit");

if (btn_exit) {
    btn_exit.addEventListener("click", function (e) {
        e.preventDefault();

        Swal.fire({
            title: '¿Quieres salir del sistema?',
            text: "La sesión actual se cerrará y saldrás del sistema",
            color: '#fff',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, salir',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                let url = this.getAttribute("href");
                window.location.href = url;
            }
        });
    });
}



const exitoElements = document.querySelectorAll(".exito");

exitoElements.forEach(function(exito) {
    exito.addEventListener("click", function (e) {
        e.preventDefault();

        Swal.fire({
            title: "Reserva realizada!",
            color: '#fff',
            icon: "success",
            draggable: true
        });
    });
});





document.addEventListener('DOMContentLoaded', function() {
    const errorElements = document.querySelectorAll("#error");

    errorElements.forEach(function(error) {
        error.addEventListener("click", function (e) {
            e.preventDefault();

            Swal.fire({
                title: "Error al realizar la reserva",
                text: "Primero debe iniciar sesión",
                color: '#fff',
                icon: "error",
                draggable: true
            });
        });
    });
});


const registC = document.querySelectorAll(".RegistC");

exitoElements.forEach(function(exito) {
    exito.addEventListener("click", function (e) {
        e.preventDefault();

        Swal.fire({
            title: "Registrado Exitosamente!",
            color: '#fff',
            icon: "success",
            draggable: true
        });
    });
});

