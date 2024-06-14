document.addEventListener("DOMContentLoaded", function () {
    /***========================================================
     * KEGIATAN INPUT DATE RANGE DEFAULT FORMULA (NOW to NOW+2)
    ========================================================***/
    // Mengambil elemen input date dari container dengan class 'date-plus-two-day'
    const dateContainer = document.querySelector(".date-plus-two-day");
    let dateInputs = dateContainer && dateContainer.querySelectorAll('input[type="date"]');

    if (dateInputs && dateInputs.length === 2) {
        // Mendapatkan tanggal hari ini
        let today = new Date();
        let todayFormatted = today.toISOString().split("T")[0];

        // Mengisi nilai date pertama dengan today
        dateInputs[0].value = todayFormatted;

        // Mengisi nilai date kedua dengan today + 2 days
        let twoDaysLater = new Date(today);
        twoDaysLater.setDate(today.getDate() + 2);
        let twoDaysLaterFormatted = twoDaysLater.toISOString().split("T")[0];
        dateInputs[1].value = twoDaysLaterFormatted;
    }

    const currentYear = new Date().getFullYear();

    /***============================
    * KEGIATAN HEADLINE CURRENT YEAR
    ============================***/
    if (document.querySelector("#__data #headline .text-center")) {
        document.querySelector("#__data #headline .text-center").innerHTML +=
            " TAHUN " + currentYear;
    }

    /***=======================================================
    * KEGIATAN HEADLINE LIMIT INPUT DATE ONLY FOR CURRENT YEAR
    =======================================================***/
    const inputDates = document.querySelectorAll("input[type='date']");

    inputDates && inputDates.forEach(function (inputDate) {
        inputDate.setAttribute("min", currentYear + "-01-01");
        inputDate.setAttribute("max", currentYear + "-12-31");
    });

    /***=======================================================
    * KEGIATAN LIMIT INPUT DOKUMENTASI
    =======================================================***/
    const inputFilesAll = document.querySelectorAll("input[type='file']:not(.input-image)");
    const inputFilesAdd = document.querySelectorAll("input[type='file']:not(.input-image):not(#edit__dokumentasi)");

    let allowedExt = ['.xlsx', '.pdf', '.docx'];
    let keteranganFile = `<li>PDF/DOCX/XLSX : <b>2MB</b></li>`;

    /*
    if (window.location.href.includes('psm')) {
        allowedExt = allowedExt.concat(['.jpeg', '.jpg', '.png']);
        keteranganFile += `<li>Gambar : <b>2MB</b></li>`;
    }
    */

    inputFilesAll && inputFilesAll.forEach(function (inputFile) {
        inputFile.setAttribute("accept", allowedExt);
    });

    inputFilesAdd && inputFilesAdd.forEach(function (inputFile) {
        const helperElement = document.createElement('div');
        helperElement.classList.add('dokumentasi_helper');

        helperElement.innerHTML = `
            <div class="text-muted mt-2">Kriteria file :</div>
            <ul class="text-muted">
                <li>Format file yang diizinkan hanya : <b>${allowedExt.join(', ')}</b></li>
                <li>Ukuran file yang diizinkan :
                    <ul>
                        ${keteranganFile}
                    </ul>
                </li>
            </ul>
        `;

        inputFile.parentNode.insertBefore(helperElement, inputFile.nextSibling);
    });

    $('input[type="file"]:not(.input-image)').change(function() {
        const fileName = $(this).val();
        const accept = $(this).attr('accept');
        const fileExt = fileName.split('.').pop().toLowerCase();
        const file = $(this).prop('files')[0];
        const fileSize = (file.size / 1024 / 1024).toFixed(2);

        const isExtensionValid = validateFileExtension(fileExt, accept);
        const isSizeValid = validateFileSize(fileExt, fileSize);

        if (!isExtensionValid || !isSizeValid) $(this).val(null);
    });

});

/* ==========================
 * KEGIATAN - INPUT FILE
============================= */
function validateFileExtension(extension, accept) {
    if (accept && accept.indexOf(extension) === -1) {
        const allowedFormats = accept.toUpperCase().split(',');

        const formats = allowedFormats.map(function(format) {
            return format.trim().replace('.', '');
        });

        const allowedFormatsString = formats.join(', ');

        showSwalError('Terjadi Kesalahan', `File yang Anda upload <b>tidak valid</b>. Format file yang diizinkan hanya : <br> <b>${allowedFormatsString}</b>`);

        return false;
    }
    return true;
}

function validateFileSize(extension, size) {
    let maxSize;

    extension = extension.toUpperCase();

    if (['PDF', 'DOCX', 'XLSX'].includes(extension)) {
        maxSize = 2;
    } else if (['JPG', 'JPEG', 'PNG'].includes(extension)) {
        maxSize = 2;
    }

    if (size > maxSize) {
        showSwalError('Terjadi Kesalahan', `Ukuran file yang Anda upload <b>${size}MB</b> melebihi batas maksimum<br>yang diizinkan hanya : hanya <b>${maxSize}MB</b>.`);

        return false;
    }
    return true;
}

/* ==========================
 * KEGIATAN - INPUT DATE
============================= */
document.addEventListener('show.bs.modal', function (event) {
    const modal = event.target;

    const rangeDateParent = modal.querySelector('.range_date');

    if (!rangeDateParent) return;
    const dateInputs = rangeDateParent.querySelectorAll('input[type="date"]');

    if (!dateInputs.length >= 2) return;

    const startDateInput = dateInputs[0];
    const endDateInput = dateInputs[1];

    const currentDate = new Date().toISOString().split('T')[0];

    startDateInput.max = currentDate;
    endDateInput.max = currentDate;

    const isEditable = !rangeDateParent.classList.contains('edit');

    endDateInput.disabled = isEditable;

    endDateInput.addEventListener('input', function () {
        const endDateValue = endDateInput.value;

        if (endDateValue) {
            startDateInput.max = endDateValue;
        }
    });

    startDateInput.addEventListener('input', function () {
        const startDateValue = startDateInput.value;

        if (startDateValue === currentDate) {
            endDateInput.disabled = true;
            endDateInput.value = '';
        } else {
            endDateInput.disabled = false;
            endDateInput.min = startDateValue;
        }
    });

    startDateInput.addEventListener('change', function () {
        if (startDateInput.value === '') {
            endDateInput.value = '';
            endDateInput.disabled = true;
        }
    });

    endDateInput.addEventListener('change', function () {
        const startDateValue = startDateInput.value;
        const endDateValue = endDateInput.value;

        if (endDateValue === startDateValue) {
            endDateInput.value = '';
        }
    });
});

function getTanggalKegiatan(tanggal_awal, tanggal_akhir) {
    const start = moment(tanggal_awal);
    const startDate = start.format('D');
    const startMonth = start.format('MMMM');
    const startYear = start.format('YYYY');

    if (tanggal_akhir) {
        const end = moment(tanggal_akhir);
        const endDate = end.format('D');
        const endMonth = end.format('MMMM');
        const endYear = end.format('YYYY');

        if (startMonth === endMonth && startYear === endYear) {
            return `${startDate} - ${endDate} ${startMonth} ${startYear}`;
        } else if (startYear !== endYear) {
            return `${start.format('D MMMM YYYY')} - ${end.format('D MMMM YYYY')}`;
        } else {
            return `${start.format('D MMMM')} - ${end.format('D MMMM YYYY')}`;
        }
    } else {
        return start.format('D MMMM YYYY');
    }
}


function formatDate(dateString) {
    const [year, month, day] = dateString.split('-');
    return new Date(year, month - 1, day);
}