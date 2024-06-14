/**
 * Toastr JS - Global Configuration
 */
toastr.options = {
    maxOpened: 1,
    autoDismiss: !0,
    closeButton: true,
    debug: false,
    newestOnTop: true,
    progressBar: true,
    positionClass: "toast-top-right",
    preventDuplicates: true,
    onclick: null,
};

/**
 * Toastr helper function
 */
var toast = (type, title, message) => toastr[type](message, title);

/**
 * Sweet Alert - Built In Toast
 */
const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
        toast.onmouseenter = Swal.stopTimer;
        toast.onmouseleave = Swal.resumeTimer;
    }
});


var hideSwal = () => Swal.close();

function showSwalLoading() {
    Swal.fire({
        title: 'Tunggu sebentar',
        icon: 'info',
        html: `Sedang <b>memproses</b> permintaan anda  ...`,
        showConfirmButton: true,
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading();
        },
    });
}

function showSwalConfirm(text, confirmButtonText) {
    return Swal.fire({
        title: 'Apakah anda yakin',
        html: text,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: confirmButtonText ? confirmButtonText : 'Ya, hapus data',
        cancelButtonText: 'Batalkan',
    });
}

function showSwal(icon = 'success', title = 'Berhasil', text, timer=0, confirmButtonText='OK') {
    Swal.fire({
        title: title,
        html: text,
        icon: icon,
        confirmButtonText: confirmButtonText,
        timer: timer,
    });
}

function showSwalSuccess(title, text, timer) {
    Swal.fire({
        title: title,
        html: text,
        icon: 'success',
        confirmButtonText: 'OK',
        timer: timer ?? 0,
    });
}

function showSwalError(title, text, timer) {
    Swal.fire({
        title: title,
        html: text,
        icon: 'error',
        confirmButtonText: 'OK',
        timer: timer ?? 0,
    });
}

function showSwalInfo(title, text) {
    Swal.fire({
        title: title,
        html: text,
        icon: 'info',
        confirmButtonText: 'Saya mengerti',
        timer: 0,
    });
}

var showSwalGenericError = () => showSwalError("Terjadi kesalahan", `Terjadi kesalahan tidak diketahui, tolong kontak <strong>developer</strong> untuk mengatasi masalah ini.`);