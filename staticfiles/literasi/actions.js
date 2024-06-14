var dokumen_file = null;
var selected_kategori = null;
var allowedExtensions = [];

$('#dokumen').on('change', handleUploadDokumen);
$('#edit_dokumen').on('change', handleUploadDokumen);
$('#kategori').on('change', handleChangeKategori);
$('#edit_kategori').on('change', handleChangeKategori);

function handleChangeKategori(e) {
    selected_kategori = $(this).val();

    switch (selected_kategori) {
        case 'buku':
            allowedExtensions = ['pdf'];
            break;
        case 'audio':
            allowedExtensions = ['mp3'];
            break;
        case 'video':
            allowedExtensions = ['mp4', 'mkv'];
            break;
        default:
            // Defaultnya, tidak ada filter ekstensi
            allowedExtensions = [];
            break;
    }
    // Menyimpan nilai accept attribute
    var acceptValue = allowedExtensions.length > 0 ? '.' + allowedExtensions.join(', .') : '';

    $('#dokumen').attr('accept', acceptValue);
    $('#edit_dokumen').attr('accept', acceptValue);
}

function handleUploadDokumen(e) {
    // Mengambil ekstensi file
    const file = e.target.files[0];
    const fileExtension = file.name.split(".").pop().toLowerCase();

    // Mengecek ekstensi file
    if (!allowedExtensions.includes(fileExtension)) {
        console.error('Invalid file type');
        e.target.value = "";
        let allowedExtensionsText = allowedExtensions.join(', ').toUpperCase();
        let error_text = `File gagal diupload, hanya ekstensi <b>${allowedExtensionsText}</b> yang diizinkan untuk kategori yang dipilih.`;
        showSwalError('Terjadi Kesalahan', error_text, 5000);
        return null;
    }


    // Mengecek ukuran file
    if (file.size > 5 * 1024 * 1024) {
        console.error('File size too large');
        e.target.value = "";
        let error_text = `File yang anda upload <b>terlalu besar</b>, maksimal hanya <b>5MB</b>`;
        showSwalError('Terjadi Kesalahan', error_text, 5000);
        return null;
    }

    dokumen_file = file;
    return file;
};

async function handlePost(e) {
    e.preventDefault();

    showSwalLoading();

    const modal = $('#createModal');
    const form = modal.find('#formCreate');
    const formData = new FormData();

    let judul = form.find('#judul').val();
    let kategori = form.find('#kategori').val();
    let status = form.find(`input[name="status"]:checked`).val();
    let dokumen = form.find('#dokumen')[0].files[0];

    formData.append('judul', judul);
    formData.append('kategori', kategori);
    formData.append('status', status);

    formData.append('dokumen', dokumen);

    try {
        const response = await axios.post('/dashboard/literasi/api/v1/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });

        console.log('Response saat post : ', response);
        modal.modal('hide');
        reloadTable(table);

        showSwalSuccess('Berhasil', `Data literasi <b>${judul}</b> berhasil <b>ditambahkan</b>`, 3000);
        // toast('success', 'Data berhasil ditambahkan!');
    } catch (error) {
        console.log('Terjadi kesalahan : ', error);
        showSwalGenericError();
    }
};

async function handleEdit(id) {
    const response = await axios.get(`/dashboard/literasi/api/v1/${id}/`);

    console.log(`Response saat fetch detail ID ${id}: `, response.data);

    const data = response.data;
    const modal = $('#editModal');
    const form = modal.find('#formUpdate');

    modal.find('#target_edited').html(data.judul);
    form.find('#edited_id').val(id);

    form.find('#edit_judul').val(data.judul);
    form.find('#edit_kategori').val(data.kategori).trigger('change');

    const url = new URL(data.dokumen);
    const path_dokumen = url.pathname;

    form.find(`input[name="status"][value="${data.status}"]`).prop('checked', true);
    form.find('#file_path').attr('href', path_dokumen);
    form.find('#file_path').html(path_dokumen);

    modal.modal('show');
};

async function handleUpdate(e) {
    e.preventDefault();

    showSwalLoading();

    const id = $('#edited_id').val();

    const modal = $('#editModal');
    const form = modal.find('#formUpdate');
    const formData = new FormData();

    let judul = form.find('#edit_judul').val();
    let kategori = form.find('#edit_kategori').val();
    let status = form.find(`input[name="status"]:checked`).val();
    let dokumen = form.find('#edit_dokumen')[0].files[0];

    formData.append('judul', judul);
    formData.append('kategori', kategori);
    formData.append('status', status);

    if (dokumen) { formData.append('dokumen', dokumen); }

    try {
        const response = await axios.put(`/dashboard/literasi/api/v1/${id}/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });

        console.log(`Response saat update Data ID-${id} : `, response);

        modal.modal('hide');
        reloadTable(table);

        showSwalSuccess('Berhasil', `Data literasi <b>${judul}</b> berhasil <b>diperbarui</b>`, 3000);
        // toast('success', 'Data berhasil diperbarui!');
    } catch (error) {
        console.log('Terjadi kesalahan : ', error);
        showSwalGenericError();
    }
};

async function handleDetail(id) {
    const response = await axios.get(`/dashboard/literasi/api/v1/${id}/`);

    console.log(`Response saat fetch detail ID ke-${id}:`, response.data);

    const data = response.data;
    const modal = $('#detailModal');
    let wadah = modal.find('#wadah');

    modal.find('#target_detail').html(data.judul);
    wadah.attr('src', data.dokumen);

    modal.modal('show');
}