
<template>
    <p class="card-text text-center p-2">Masukan nama pengguna anda untuk masuk kedalam aplikasi Sistem Informasi DAYAMAS
    </p>
    <form method="POST" id="__form_login" @submit.prevent="login()">
        <InputGroup label="Nama Pengguna" placeholder="Nama Pengguna Anda" type="text" icon="fas fa-user" name="username"
            v-model="username" required></InputGroup>
        <InputGroup label="Kata Sandi" placeholder="Kata Sandi Anda" type="password" icon="fas fa-lock" name="password"
            current-password v-model="password" required></InputGroup>

        <div class="text-end">
            <span id="forgot-password-text">Lupa Kata Sandi? Klik <a @click="handleForgotPassword()"
                    href="javascript:;">disini</a></span>
        </div>

        <Button type="submit" icon="fa-solid fa-arrow-right-to-bracket">Masuk</Button>
    </form>
</template>
<script setup>
import Button from "../../components/forms/Button.vue";
import InputGroup from "../../components/forms/InputGroup.vue";
import { ref } from 'vue';

const username = ref('');
const password = ref('');

</script>
<script>
export default {
    data() {
        return {
            apiURL: `${window.location.origin}/accounts/login/`
        }
    },
    methods: {
        async login() {
            const trimmedUsername = username.value.trim();
            const trimmedPassword = password.value.trim();

            function resetValue() {
                username.value = '';
                password.value = '';
            }

            Swal.fire({
                title: "Mengecek data",
                icon: "info",
                html: `Mengecek <b>data kredensials</b> yang anda masukan ...`,
                didOpen: () => {
                    Swal.showLoading();
                },
            });

            try {
                const response = await fetch(this.apiURL, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-CSRFToken": getXCSRFToken(),
                    },
                    body: new URLSearchParams({
                        username: trimmedUsername,
                        password: trimmedPassword,
                    }),
                });

                if (response.redirected) {
                    console.log('Response: ', response);
                    resetValue();

                    // Mendapatkan nilai param next? dari URL saat ini
                    const urlParams = new URLSearchParams(window.location.search);
                    const nextParam = urlParams.get('next');

                    Swal.fire({
                        title: "Berhasil",
                        html: `Anda <strong>berhasil</strong> login, akan segera dialihkan.`,
                        icon: "success",
                        confirmButtonText: "OK",
                        timer: 1000,
                    });

                    setTimeout(() => {
                        console.log('Memvalidasi akun anda ...');
                        window.location.href = "/accounts/check-login/" + (nextParam ? `?next=${nextParam}` : '');;
                        }, 1000);
                } else {
                    console.warn('Response: ', response);
                    throw new Error("Data yang anda masukan tidak valid atau tidak ditemukan!");
                }
            } catch (error) {
                console.error("Error:", error);

                Swal.fire({
                    title: "Terjadi kesalahan",
                    html: `Data yang anda masukan <strong>tidak valid</strong> atau <strong>tidak ditemukan</strong>!`,
                    icon: "error",
                    confirmButtonText: "OK",
                });

                resetValue();
            }
        },
        handleForgotPassword() {
            Swal.fire({
                title: "Lupa password anda?",
                html: `Kontak <strong>puslitdatin</strong> untuk mendapatkan <strong>password</strong> anda kembali!`,
                icon: "info",
                confirmButtonText: "Hubungi Puslitdatin.",
                showCancelButton: true,
                cancelButtonText: "Batalkan"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = "https://puslitdatin.bnn.go.id/kontak/#fws_65ab64f055da2";
                }
            });
        }
    }
};
</script>