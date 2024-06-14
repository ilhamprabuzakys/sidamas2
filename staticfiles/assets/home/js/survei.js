// Pertanyaan diambil dari daftar pertanyaan pada kuisioner *Tes Urine*
const jawabanSurvei = [];
let onGoing = false;
let jawabanJenisKelamin = "";
let jawabanRentangUsia = "";
let jawabanPendidikanTerakhir = "";

const daftarPertanyaan = [
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang kesesuaian persyaratan pelayanan dengan jenis pelayanannya?",
        jawaban: [
            { opsi: "Tidak sesuai", nilai: "1" },
            { opsi: "Kurang sesuai", nilai: "2" },
            { opsi: "Sesuai", nilai: "3" },
            { opsi: "Sangat sesuai", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pemahaman Saudara tentang kemudahan prosedur pelayanan yang diberikan?",
        jawaban: [
            { opsi: "Tidak paham", nilai: "1" },
            { opsi: "Kurang paham", nilai: "2" },
            { opsi: "Paham", nilai: "3" },
            { opsi: "Sangat paham", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang kecepatan waktu dalam memberikan pelayanan?",
        jawaban: [
            { opsi: "Tidak cepat", nilai: "1" },
            { opsi: "Kurang cepat", nilai: "2" },
            { opsi: "Cepat", nilai: "3" },
            { opsi: "Sangat cepat", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang kewajaran biaya/tarif dalam pelayanan?",
        jawaban: [
            { opsi: "Sangat mahal", nilai: "1" },
            { opsi: "Cukup mahal", nilai: "2" },
            { opsi: "Murah", nilai: "3" },
            { opsi: "Gratis", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Petugas tidak pernah meminta imbalan dan melakukan pungutan liar?",
        jawaban: [
            { opsi: "Tidak setuju", nilai: "1" },
            { opsi: "Kurang setuju", nilai: "2" },
            { opsi: "Setuju", nilai: "3" },
            { opsi: "Sangat Setuju", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang kesesuaian produk pelayanan antara yang tercantum dalam standar pelayanan dengan hasil yang diberikan?",
        jawaban: [
            { opsi: "Tidak sesuai", nilai: "1" },
            { opsi: "Kurang sesuai", nilai: "2" },
            { opsi: "Sesuai", nilai: "3" },
            { opsi: "Sangat sesuai", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang kompetensi/kemampuan petugas dalam pelayanan?",
        jawaban: [
            { opsi: "Tidak kompeten", nilai: "1" },
            { opsi: "Kurang kompeten", nilai: "2" },
            { opsi: "Kompeten", nilai: "3" },
            { opsi: "Sangat kompeten", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang perilaku petugas dalam pelayanan terkait kesopanan dan keramahan?",
        jawaban: [
            { opsi: "Tidak sopan dan ramah", nilai: "1" },
            { opsi: "Kurang sopan dan ramah", nilai: "2" },
            { opsi: "Sopan dan ramah", nilai: "3" },
            { opsi: "Sangat sopan dan ramah", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang penanganan pengaduan pengguna layanan?",
        jawaban: [
            { opsi: "Tidak ada", nilai: "1" },
            { opsi: "Ada tetapi tidak berfungsi", nilai: "2" },
            { opsi: "Berfungsi kurang maksimal", nilai: "3" },
            { opsi: "Dikelola dengan baik", nilai: "4" },
        ],
    },
    {
        pertanyaan:
            "Bagaimana pendapat Saudara tentang kualitas sarana dan prasarana?",
        jawaban: [
            { opsi: "Buruk", nilai: "1" },
            { opsi: "Cukup", nilai: "2" },
            { opsi: "Baik", nilai: "3" },
            { opsi: "Sangat baik", nilai: "4" },
        ],
    },
];

window.addEventListener('beforeunload', function () {
    if (onGoing == true) {
        return "Apakah Anda yakin?";
    }
});

document.querySelectorAll("img").forEach(function (img) {
    img.setAttribute("draggable", "false");

    // Membuat elemen overlay
    var overlay = document.createElement("div");
    overlay.className = "image-overlay";

    // Menambahkan overlay ke dalam elemen gambar
    img.parentNode.insertBefore(overlay, img);

    img.addEventListener("contextmenu", function (e) {
        e.preventDefault();
        console.log("tidak boleh right click!");
    });

    img.addEventListener("touchstart", function (e) {
        touchStartTime = new Date().getTime();
    });

    img.addEventListener("touchend", function (e) {
        var touchEndTime = new Date().getTime();
        var touchDuration = touchEndTime - touchStartTime;

        // Menentukan durasi tekan lama (misal: 500ms)
        var longPressDuration = 500;

        if (touchDuration >= longPressDuration) {
            e.preventDefault(); // Mencegah pop-up detail gambar muncul
            console.log("Tekan lama dinonaktifkan");
        }
    });
});

// Mendapatkan token CSRF dari cookie
const csrftoken = getCookie("csrftoken");
// Menambahkan token CSRF ke headers
const headers = {
    "X-CSRFToken": csrftoken,
};
const api = axios.create({
    baseURL: "http://127.0.0.1:8000/survey/api/v1/",
    headers: headers,
});

let posisiPertanyaan = 0;
let sedangMenjawab = false;

function muatSurvei() {
    const pertanyaanSekarang = daftarPertanyaan[posisiPertanyaan];

    $("#survei-container").addClass("fade-out");
    $("#daftar-pilihan").addClass("fade-out");

    setTimeout(() => {
        $("#survei-container").removeClass("fade-out");
        $("#daftar-pilihan").removeClass("fade-out");

        // document.getElementById('questionNumber').innerText = `Pertanyaan #${posisiPertanyaan + 1}`;
        document.querySelector("#survei-container #questionText").innerText =
            pertanyaanSekarang.pertanyaan;

        const opsi = pertanyaanSekarang.jawaban;
        document.getElementById("option1").innerText = opsi[0].opsi;
        document.getElementById("option2").innerText = opsi[1].opsi;
        document.getElementById("option3").innerText = opsi[2].opsi;
        document.getElementById("option4").innerText = opsi[3].opsi;
    }, 500);
}

function lanjutkanJenisKelamin() {
    /* Mendapatkan nilai dari radio button jenis_kelamin yang dipilih */
    const selectedJenisKelamin = document.querySelector(
        'input[name="jenis_kelamin"]:checked'
    );

    /* Pengecekan jika user tidak memilih satu pun radio button */
    if (!selectedJenisKelamin) {
        /* Menampilkan pesan error jika user tidak memilih opsi */
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Tolong pilih jenis kelamin anda.",
            showConfirmButton: true,
            confirmButtonText: "Oke",
            timer: 4000,
        });
    } else {
        /* Menyimpan nilai yang dipilih ke dalam variabel jawabanJenisKelamin */
        jawabanJenisKelamin = selectedJenisKelamin.value;

        /* Melakukan operasi selanjutnya jika diperlukan */
        /* Contoh: Menampilkan yang dipilih dalam console */
        // console.log('Jenis Kelamin yang Dipilih:', jawabanJenisKelamin);

        /* Melanjutkan ke langkah berikutnya */
        $("#jenis_kelamin-container").addClass("d-none");
        $("#usia-container").removeClass("d-none");
    }
}

function lanjutkanRentangUsia() {
    /* Mendapatkan nilai dari radio button rentang_usia yang dipilih */
    const selectedRentangUsia = document.querySelector(
        'input[name="rentang_usia"]:checked'
    );

    /* Pengecekan jika user tidak memilih satu pun radio button */
    if (!selectedRentangUsia) {
        /* Menampilkan pesan error jika user tidak memilih opsi */
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Tolong pilih rentang usia anda.",
            showConfirmButton: true,
            confirmButtonText: "Oke",
            timer: 4000,
        });
    } else {
        /* Menyimpan nilai yang dipilih ke dalam variabel jawabanRentangUsia */
        jawabanRentangUsia = selectedRentangUsia.value;

        /* Melakukan operasi selanjutnya jika diperlukan */
        /* Contoh: Menampilkan opsi yang dipilih dalam console */
        // console.log('Rentang Usia yang Dipilih:', jawabanRentangUsia);

        /* Melanjutkan ke langkah berikutnya */
        $("#usia-container").addClass("d-none");
        $("#pendidikan_terakhir-container").removeClass("d-none");
    }
}

function lanjutkanPendidikanTerakhir() {
    /* Mendapatkan nilai dari radio button yang dipilih */
    const selectedPendidikanTerakhir = document.querySelector(
        'input[name="pendidikan_terakhir"]:checked'
    );

    /* Pengecekan jika user tidak memilih satu pun radio button */
    if (!selectedPendidikanTerakhir) {
        /* Menampilkan pesan error jika user tidak memilih opsi */
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Tolong pilih pendidikan terakhir anda.",
            showConfirmButton: true,
            confirmButtonText: "Oke",
            timer: 4000,
        });
    } else {
        /* Menyimpan nilai yang dipilih ke dalam variabel jawabanPendidikanTerakhir */
        jawabanPendidikanTerakhir = selectedPendidikanTerakhir.value;

        /* Melakukan operasi selanjutnya jika diperlukan */
        /* Contoh: Menampilkan opsi yang dipilih dalam console */
        // console.log('Pendidikan Terakhir yang Dipilih:', jawabanPendidikanTerakhir);

        /* Melanjutkan ke langkah berikutnya */
        $("#pendidikan_terakhir-container").addClass("d-none");
        $("#survei-container").removeClass("d-none");
    }
}

function jawab(nilaiDipilih) {
    if (sedangMenjawab) return;

    sedangMenjawab = true;

    const opsiDipilih = parseInt(nilaiDipilih) - 1;

    const tampunganJawaban = daftarPertanyaan[posisiPertanyaan];
    const jawaban = {
        no: posisiPertanyaan + 1,
        jawaban: opsiDipilih + 1,
        bobot: tampunganJawaban.jawaban[opsiDipilih].nilai,
        pilihan: String.fromCharCode(97 + opsiDipilih),
    };

    jawabanSurvei.push(jawaban);

    posisiPertanyaan++;

    if (posisiPertanyaan < daftarPertanyaan.length) {
        muatSurvei();
        /* Resetting the hover effect on card */
        document.querySelectorAll("#daftar-pilihan .card").forEach((card) => {
            card.style.transition = "none";
            card.style.marginBottom = "0";
        });
    } else {
        $("#survei-container").addClass("d-none");
        $("#selesai-container").removeClass("d-none");
        hitungDanTampilkanHasil();
        onGoing = false;
    }

    // Menetapkan kembali hover effect setelah sedikit waktu
    setTimeout(() => {
        document.querySelectorAll(".card").forEach((card) => {
            card.style.transition = ""; // Mengembalikan transisi ke nilai default
            card.style.marginBottom = ""; // Mengembalikan margin-bottom ke nilai default
        });
        sedangMenjawab = false;
    }, 800); // Dikasih delay
}

function kirimDataResponden() {
    const data = {
        rentang_usia: jawabanRentangUsia,
        pendidikan_terkahir: jawabanPendidikanTerakhir,
        jenis_kelamin: jawabanJenisKelamin,
    };

    api.post("tbl_data_responden/", data)
        .then((response) => {
            console.log("Data responden berhasil dibuat:", response.data);
            const idRespondenBaru = response.data.id;
            // console.log('Data responden berhasil dikirim. ID Responden Baru:', idRespondenBaru);

            // Setelah mendapatkan ID responden, kirim hasil survei
            kirimHasil(idRespondenBaru);
        })
        .catch((error) => {
            console.error("Gagal mengirim data:", error);
        });
}

function kirimHasil(idDataResponden) {
    const hasilSurvei = jawabanSurvei.map((jawaban) => {
        return {
            no: jawaban.no,
            jawaban: jawaban.jawaban,
            bobot: jawaban.bobot,
            pilihan: jawaban.pilihan,
        };
    });

    const arrayNilaiJawaban = hasilSurvei.map((jawaban) =>
        parseInt(jawaban.bobot, 10)
    );
    const sigmaNilai = arrayNilaiJawaban.reduce((a, b) => a + b, 0);

    const dataHasilSurvei = {
        array_nilai_jawaban: arrayNilaiJawaban.join(","),
        data_mentahan: JSON.stringify(hasilSurvei),
        sigma_nilai: sigmaNilai,
        id_data_responden: idDataResponden, // Gunakan ID responden yang baru dibuat
    };

    api.post("tbl_isi_survey/", dataHasilSurvei)
        .then((response) => {
            console.log("Data hasil survei berhasil dikirim:", response.data);
        })
        .catch((error) => {
            console.error("Gagal mengirim data hasil survei:", error);
        });
}

// Fungsi untuk mendapatkan nilai cookie
function getCookie(name) {
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
}

function lihatHasilJawaban() {
    const hasilSurvei = jawabanSurvei.map((jawaban) => {
        return {
            no: jawaban.no,
            jawaban: jawaban.jawaban,
            bobot: jawaban.bobot,
            pilihan: jawaban.pilihan,
        };
    });

    // const hasilSurveiJSON = JSON.stringify(hasilSurvei);
    console.log("Hasil Survei:", hasilSurvei);
}

function hitungDanTampilkanHasil() {
    lihatHasilJawaban();
    kirimDataResponden();
}

function mulaiSurvei() {
    onGoing = true;
    $("#mulai-container").addClass("d-none");
    $("#jenis_kelamin-container").removeClass("d-none");
    muatSurvei();
}

function bukaSurvei(event) {
    event.preventDefault();

    let kode = document.querySelector("#input-code").value;

    Swal.fire({
        title: "Mengecek data",
        html: "Sedang mengecek kode anda",
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading();
            setTimeout(() => {
                if (kode == "") {
                    Swal.fire({
                        title: "Gagal",
                        html: `Tolong masukkan kode survei anda.`,
                        icon: "error",
                        confirmButtonText: "OK",
                    });
                } else {
                    if (kode != "abc") {
                        Swal.fire({
                            title: "Gagal",
                            html: `Survei dengan kode <b>${kode}</b> tidak ditemukan.`,
                            icon: "error",
                            confirmButtonText: "OK",
                        });
                    } else {
                        Swal.fire({
                            title: "Berhasil",
                            text: "Survei ditemukan, survei akan segera ditampilkan.",
                            icon: "success",
                            confirmButtonText: "OK",
                            timer: 1000,
                        });
                        document.querySelector("#input-code").value = "";
                        setTimeout(() => {
                            $("#masukan-container").addClass("d-none");
                            $("#mulai-container").removeClass("d-none");
                        }, 1000);
                    }
                }
            }, 1000);
        },
    });
}

function keluar() {
    // $('#masukan-container').removeClass('d-none');
    $("#mulai-container").removeClass("d-none");
    $("#survei-container").addClass("d-none");
    $("#selesai-container").addClass("d-none");
    posisiPertanyaan = 0;

    // Reset radio button untuk jenis_kelamin
    resetRadioButtons("jenis_kelamin");

    // Reset radio button untuk rentang_usia
    resetRadioButtons("rentang_usia");

    // Reset radio button untuk pendidikan_terakhir
    resetRadioButtons("pendidikan_terakhir");

    const btnMulai = document.querySelectorAll(
        ".btn-mulai:not(#mulai-container .btn-mulai)"
    );
    btnMulai.forEach((btn) => {
        btn.classList.add("disabled");
    });
}

function resetRadioButtons(name) {
    const radioButtons = document.querySelectorAll(
        `input[type="radio"][name="${name}"]`
    );

    radioButtons.forEach((radio) => {
        radio.checked = false;
    });
}

function hitungNilai() {
    const totalNilai = jawabanSurvei.reduce(
        (acc, jawaban) => acc + parseInt(jawaban.bobot),
        0
    );
    const rataRata = totalNilai / daftarPertanyaan.length;

    /*
      Untuk perhitungan harus berdasarkan lebih dari 2 pengisian
   */
    const NRRTertimbang = rataRata * 0.11;
    const IKM = NRRTertimbang * 25;
    let MutuPelayanan = "";

    /*
   Mutu Pelayanan :
   A (Sangat Baik)			: 88,31 - 100,00
   B (Baik)			: 76,61 - 88,30
   C (Kurang Baik)			: 65,00 - 76,60
   D (Tidak Baik)			: 25,00 - 64,99
   */

    if (IKM >= 88.31) {
        MutuPelayanan = "A (Sangat Baik)";
    } else if (IKM >= 76.61) {
        MutuPelayanan = "B (Baik)";
    } else if (IKM >= 65.0) {
        MutuPelayanan = "C (Kurang Baik)";
    } else {
        MutuPelayanan = "D (Tidak Baik)";
    }

    console.log("Total Nilai:", totalNilai);
    console.log("Rata-rata:", rataRata);
    console.log("NRR tertimbang per unsur:", NRRTertimbang);
    console.log("IKM:", IKM);
    console.log("Mutu Pelayanan:", MutuPelayanan);
}


// window.addEventListener("load", (event) => {
//     // do stuff
//     // console.log("halo");
//     $('input[name="jenis_kelamin"]').change(function () {
//         console.log("Ngeganti choice jenis_kelamin");
//         $(this)
//             .closest("#jenis_kelamin-container")
//             .find(".btn-mulai")
//             .removeClass("disabled");
//     });

//     // Lakukan hal yang sama untuk rentang usia dan pendidikan terakhir
//     $('input[name="rentang_usia"]')
//         .change(function () {
//             console.log("Ngeganti choice rentang_usia");
//             $(this)
//                 .closest("#usia-container")
//                 .find(".btn-mulai")
//                 .removeClass("disabled");
//         })
//         .trigger("change"); // Trigger change event on page load

//     $('input[name="pendidikan_terakhir"]').change(function () {
//         console.log("Ngeganti choice pendidikan_terakhir");
//         $(this)
//             .closest("#pendidikan_terakhir-container")
//             .find(".btn-mulai")
//             .removeClass("disabled");
//     });

//     // Tambahkan kode ini untuk memulai dengan tombol btn-mulai yang disabled
//     $(".btn-mulai").not("#mulai-container .btn-mulai").addClass("disabled");
// });
