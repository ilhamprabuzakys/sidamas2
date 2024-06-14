const ButtonDirektorat = {
    props: {
        direktorat: {
            type: String,
            required: true,
            validator: (value) => ["psm", "dayatif"].includes(value),
        },
    },
    computed: {
        apiURL() {
            return `${window.location.origin}/accounts/api/v1/pilih-direktorat/`;
        },
        csrftoken() {
            return this.getCookie("csrftoken");
        },
        headers() {
            return {
                "X-CSRFToken": this.csrftoken,
            };
        },
        api() {
            return axios.create({
                baseURL: this.apiURL,
                headers: this.headers,
            });
        },
        getDetailDirektorat() {
            return this.direktorat === "psm"
                ? "Direktorat Peran Serta Masyarakat"
                : "Direktorat Pemberdayaan Alternatif";
        },
    },
    template: `
      <button :class="getClass()" type="button" @click="handleClick()">
        <i class="fas fa-arrow-right-from-bracket"></i>
        {{ getDetailDirektorat }}
      </button>
    `,
    methods: {
        getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== "") {
                var cookies = document.cookie.split(";");
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Mengecek apakah cookie memiliki nama yang sesuai
                    if (cookie.substring(0, name.length + 1) === name + "=") {
                        cookieValue = decodeURIComponent(
                            cookie.substring(name.length + 1)
                        );
                        break;
                    }
                }
            }
            return cookieValue;
        },
        getClass() {
            return `btn btn-${this.direktorat.toLowerCase()}`;
        },
        loginDayatif() {
            Swal.fire({
                title: "Apakah anda yakin?",
                html: `Anda akan login sebagai direktorat <b>DAYATIF</b>?`,
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Ya, saya yakin!",
                cancelButtonText: "Batalkan",
            }).then((result) => {
                if (result.isConfirmed) {
                    Swal.fire({
                        title: "Tunggu sebentar!",
                        icon: "info",
                        timer: 1000,
                        html: "Mengalihkan ke halaman <b>Dashboard Dayatif</b> ...",
                        didOpen: () => {
                            Swal.showLoading();
                        },
                    }).then((result) => {
                        this.sendData();
                    });
                }
            });
        },
        loginPSM() {
            Swal.fire({
                title: "Apakah anda yakin?",
                html: `Anda akan login sebagai direktorat <b>PSM</b>?`,
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Ya, saya yakin!",
                cancelButtonText: "Batalkan",
            }).then((result) => {
                if (result.isConfirmed) {
                    Swal.fire({
                        title: "Tunggu sebentar!",
                        icon: "info",
                        html: "Mengalihkan ke halaman <b>Dashboard PSM</b> ...",
                        didOpen: () => {
                            Swal.showLoading();
                        },
                    }).then((result) => {});

                    this.sendData();
                }
            });
        },
        sendData() {
            this.api
                .post("", {direktorat: this.direktorat})
                .then((response) => {
                    console.log("Response:", response.data);
                    
                    Swal.fire({
                        title: "Berhasil",
                        html: `Anda <strong>berhasil</strong> login, akan segera dialihkan.`,
                        icon: "success",
                        confirmButtonText: "OK",
                        timer: 1000,
                    });

                    this.redirectToDashboard();
                })
                .catch((error) => {
                    Swal.fire({
                        title: "Terjadi kesalahan",
                        html: `Tidak dapat memperbarui data direktorat anda, kontak <strong>developer</strong> untuk masalah lebih lanjut.`,
                        icon: "error",
                        confirmButtonText: "OK",
                    });
                    console.error("Gagal mengirim data:", error);
                });
        },
        handleClick() {
            if (this.direktorat === "psm") {
                this.loginPSM();
            } else {
                this.loginDayatif();
            }
        },

        redirectToDashboard() {
            setTimeout(() => {
                console.log('mengalihkan ke dashboard ...');
                window.location.replace("/dashboard");
            }, 1000);
        },
    },


};

export default ButtonDirektorat;
