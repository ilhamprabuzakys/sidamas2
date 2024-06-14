const Form = {
    props: {
        method: { type: String, default: "POST" },
        action: { type: String, default: "" },
        for: { type: String, default: "" },
    },
    template: `
        <form :action="action" :method="method" @submit.prevent="getSubmitHandler()" >
            <slot></slot>
        </form>
    `,
    methods: {
        getSubmitHandler() {
            if (this.for == "login") {
                return this.handleLogin();
            }
            return false;
        },
        handleLogin() {
            let usernameEl = document.querySelector("#username");
            let passwordEl = document.querySelector("#password");

            let username = usernameEl.value.trim();
            let password = passwordEl.value.trim();

            if (username.includes(" ")) {
                Swal.fire({
                    title: "Terjadi kesalahan",
                    html: `Username tidak boleh mengandung <strong>spasi</strong>.`,
                    icon: "error",
                    confirmButtonText: "OK",
                });
                return;
            }

            Swal.fire({
                title: "Mengecek data",
                icon: "info",
                html: `Mengecek <b>data kredensials</b> yang anda masukan ...`,
                didOpen: () => {
                    Swal.showLoading();
                },
            }).then((result) => {
                if (result.dismiss === Swal.DismissReason.timer) {
                }
            });

            fetch(window.location.origin + "/accounts/login/", {
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
                            html: `Anda <strong>berhasil</strong> login, akan segera dialihkan.`,
                            icon: "success",
                            confirmButtonText: "OK",
                            timer: 1000,
                        });
                        setTimeout(() => {
                            window.location.href = "/accounts/pilih-direktorat";
                        }, 1000);
                    } else {
                        Swal.fire({
                            title: "Terjadi kesalahan",
                            html: `Data yang anda masukan <strong>tidak valid</strong> atau <strong>tidak ditemukan</strong>!`,
                            icon: "error",
                            confirmButtonText: "OK",
                        });

                        usernameEl.value = "";
                        passwordEl.value = "";
                    }
                })
                .catch((error) => {
                    // console.error("Error:", error);
                    Swal.fire({
                        title: "Terjadi kesalahan",
                        html: `Data yang anda masukan <strong>tidak valid</strong> atau <strong>tidak ditemukan</strong>!`,
                        icon: "error",
                        confirmButtonText: "OK",
                    });

                    usernameEl.value = "";
                    passwordEl.value = "";
                });
        },
    },
};

export default Form;
