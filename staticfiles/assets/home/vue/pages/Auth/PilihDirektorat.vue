<template>
    <section id="pilih-direktorat">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 d-flex justify-content-center">
                    <div>
                        <h1 class="headline text-center">Sistem Informasi DAYAMAS</h1>
                        <h4 class="text-center text-gray-400">Pelaporan</h4>
                        <div id="button-pilih-role" class="d-flex mt-5 gap-3">
                            <button class="btn btn-psm" type="button" @click="loginPSM()">
                                <i class="fas fa-arrow-right-from-bracket"></i>
                                Direktorat Peran Serta Masyarakat
                            </button>
                            <button class="btn btn-dayatif" type="button" @click="loginDayatif()">
                                <i class="fas fa-arrow-right-from-bracket"></i>
                                Direktorat Pemberdayaan Alternatif
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
export default {
    computed: {
        apiURL() {
            return `${window.location.origin}/accounts/api/v1/pilih-direktorat/`;
        },
        headers() {
            return getHeaders();
        },
        api() {
            return axios.create({
                baseURL: this.apiURL,
                headers: this.headers,
            });
        },
    },

    methods: {
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
                        this.sendData("dayatif");
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
                    }).then((result) => { });

                    this.sendData("psm");
                }
            });
        },
        sendData(direktorat) {
            this.api
                .post("", { direktorat: direktorat })
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
        redirectToDashboard() {
            setTimeout(() => {
                console.log('mengalihkan ke dashboard ...');
                window.location.replace("/dashboard");
            }, 1000);
        },
    },
};
</script>
<style scoped>
main {
    background-image: url("../../images/auth/bg-pilih-role.png");
    background-size: cover;
    /* atau contain, sesuai kebutuhan */
    background-repeat: no-repeat;
    height: 60vh;
}

#pilih-direktorat {
    margin: 10rem 0;
}

#pilih-direktorat .headline {
    color: #05a3ae !important;
}

#pilih-direktorat .title h2 {
    text-transform: none;
}

.text-gray-400 {
    color: #bdbdbd;
}

/* BUTTON */

.btn .btn-dayatif i {
    color: #03b3be;
}

.btn.btn-psm,
.btn.btn-dayatif {
    border-radius: 30px;
    -webkit-border-radius: 30px;
    -moz-border-radius: 30px;
    -ms-border-radius: 30px;
    -o-border-radius: 30px;
    font-weight: 500;
    padding: 10px 20px;
    text-transform: uppercase;
}

.btn.btn-dayatif {
    background-color: #fff0c8 !important;
    color: #03b3be !important;
}

.btn.btn-dayatif:hover {
    background-color: #e4d6af !important;
}

.btn.btn-dayatif:focus {
    background-color: #e4d6af !important;
}

.btn.btn-dayatif:active {
    background-color: #e4d6af !important;
}

.btn.btn-psm {
    background-color: #ebbd86 !important;
    color: #fff0c8 !important;
}

.btn.btn-psm:hover {
    background-color: #c7a172 !important;
}

.btn.btn-psm:focus {
    background-color: #c7a172 !important;
}

.btn.btn-psm:active {
    background-color: #c7a172 !important;
}
</style>