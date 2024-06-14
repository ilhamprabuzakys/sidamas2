function login() {
    // event.preventDefault();
    let username = document.querySelector("#username").value;
    let password = document.querySelector("#password").value;

    Swal.fire({
        title: "Mengecek data",
        icon: "info",
        timer: 1000,
        html: "Mengecek kredensials yang anda masukan ...",
        didOpen: () => {
            Swal.showLoading();
        },
    }).then((result) => {
        if (result.dismiss === Swal.DismissReason.timer) {
            fetch("http://127.0.0.1:8000/account/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": document.querySelector(
                        'input[name="csrfmiddlewaretoken"]'
                    ).value,
                },
                body: new URLSearchParams({
                    username: username,
                    password: password,
                }),
            })
                .then((data) => {
                    if (data.redirected) {
                        // Jika login berhasil, redirect ke halaman yang ditentukan
                        Swal.fire({
                            title: "Berhasil",
                            text: "Selamat anda berhasil login, akan segera dialihkan.",
                            icon: "success",
                            confirmButtonText: "OK",
                            timer: 1000,
                        });
                        setTimeout(() => {
                            window.location.href = "/account/pilih-akun";
                        }, 1000);
                    } else {
                        Swal.fire({
                            title: "Gagal",
                            html: `Data akun yang anda masukan tidak ditemukan.`,
                            icon: "error",
                            confirmButtonText: "OK",
                        });
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    // Handle error jika terjadi kesalahan dalam request
                    Swal.fire({
                        title: "Error",
                        text: "Terjadi kesalahan saat mencoba login.",
                        icon: "error",
                        confirmButtonText: "OK",
                    });
                });
        }
    });
}

const loginForm = document.querySelector("#loginForm");
loginForm.addEventListener("submit", function (event) {
    event.preventDefault();
    login();
});
