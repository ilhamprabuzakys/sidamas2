const allowedExtensions = ['jpg', 'jpeg', 'png', 'webp'];

const editedData = {
    src: '',
};

$('#gambar').on('change', handleUploadGambar);
$('#gambar').attr('accept', allowedExtensions.length > 0 ? '.' + allowedExtensions.join(', .') : '');

$('#edited_gambar').on('change', handleUploadGambar);
$('#edited_gambar').attr('accept', allowedExtensions.length > 0 ? '.' + allowedExtensions.join(', .') : '');

function handleUploadGambar(e) {
    const file = e.target.files[0];
    const fileExtension = file.name.split(".").pop().toLowerCase();
    const preview = document.getElementById('preview_image');
    const editPreview = document.getElementById('edited_preview_image');

    if (!allowedExtensions.includes(fileExtension)) {
        console.error('Invalid file type');
        e.target.value = "";
        const allowedExtensionsText = allowedExtensions.join(', ').toUpperCase();
        const error_text = `File gagal diupload, hanya ekstensi <b>${allowedExtensionsText}</b> yang diizinkan untuk kategori yang dipilih.`;
        showSwalError('Terjadi Kesalahan', error_text, 5000);
        return null;
    }


    if (file.size > 5 * 1024 * 1024) {
        console.error('File size too large');
        e.target.value = "";
        const error_text = `File yang anda upload <b>terlalu besar</b>, maksimal hanya <b>5MB</b>`;
        showSwalError('Terjadi Kesalahan', error_text, 5000);
        return null;
    }

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
            editPreview.src = e.target.result;
        };

        reader.readAsDataURL(file);

        $('.clear_gambar_icon').removeClass('d-none');
    }

    return file;
};

$('#createModal').on('hidden.bs.modal', function () {
    $('.clear_gambar_icon').addClass('d-none');
});

$('#editModal').on('hidden.bs.modal', function () {
    $('.clear_gambar_icon').addClass('d-none');
});

function clearImage() {
    const input = document.getElementById('gambar');
    const preview = document.getElementById('preview_image');

    input.value = '';
    preview.src = '';

    $('.clear_gambar_icon').addClass('d-none');
}

function clearEditedImage() {
    const input = document.getElementById('edited_gambar');
    const preview = document.getElementById('edited_preview_image');

    input.value = '';
    preview.src = editedData.src;

    $('.clear_gambar_icon').addClass('d-none');
}

$('#createModal .clear_gambar_icon').on('click', clearImage);
$('#editModal .clear_gambar_icon').on('click', clearEditedImage);

async function handlePost(e) {
    e.preventDefault();

    showSwalLoading();

    const modal = $('#createModal');
    const form = modal.find('#formCreate');
    const formData = new FormData();

    const judul = form.find('#judul').val();
    const kategori = form.find('#kategori').val();
    const status = form.find(`input[name="status"]:checked`).val();
    const tags = form.find('#tags').val();
    const gambar_utama = form.find('#gambar')[0].files[0];

    formData.append('judul', judul);
    formData.append('kategori', kategori);
    formData.append('status', status);
    formData.append('gambar_utama', gambar_utama);

    const tagsValue = JSON.parse(tags).map(item => item.value).join(',');

    const isi_berita = create_berita_editor.getData();

    const payload = { judul, kategori, status, tagsValue, gambar_utama, isi_berita };


    console.log('Payload :', payload);

    formData.append('tags', tagsValue);
    formData.append('isi_berita', isi_berita);

    try {
        const response = await axios.post('/dashboard/berita/api/v1/', formData, {
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
}

async function handleEdit(id) {
    const response = await axios.get(`/dashboard/berita/api/v1/${id}/`);

    console.log(`Response saat fetch detail ID ${id}: `, response.data);

    const data = response.data;
    const modal = $('#editModal');
    const form = modal.find('#formUpdate');

    modal.find('#target_edited').html(data.judul);
    form.find('#edited_id').val(id);

    form.find('#edited_judul').val(data.judul);
    form.find('#edited_kategori').val(data.kategori.id).trigger('change');
    form.find('#edited_tags').val(data.tags);
    form.find(`input[name="edited_status"][value="${data.status}"]`).prop('checked', true);
    edit_berita_editor.setData(data.isi_berita);

    const url = new URL(data.gambar_utama);
    const path_file = url.pathname;

    form.find('#edited_preview_image').attr('src', path_file);

    editedData.src = path_file;

    modal.modal('show');
};

async function handleUpdate(e) {
    e.preventDefault();

    showSwalLoading();

    const modal = $('#editModal');
    const form = modal.find('#formUpdate');
    const formData = new FormData();

    const edited_id = form.find('#edited_id').val();
    const judul = form.find('#edited_judul').val();
    const kategori = form.find('#edited_kategori').val();
    const status = form.find(`input[name="edited_status"]:checked`).val();
    const tags = form.find('#edited_tags').val();

    const gambar_utama = form.find('#edited_gambar')[0].files[0] ?? null;

    formData.append('judul', judul);
    formData.append('kategori', kategori);
    formData.append('status', status);

    if (gambar_utama) formData.append('gambar_utama', gambar_utama);

    const tagsValue = JSON.parse(tags).map(item => item.value).join(',');

    const isi_berita = edit_berita_editor.getData();

    const payload = { judul, kategori, status, tagsValue, gambar_utama, isi_berita };

    console.log('Payload :', payload);

    formData.append('tags', tagsValue);
    formData.append('isi_berita', isi_berita);

    try {
        const response = await axios.patch(`/dashboard/berita/api/v1/${edited_id}/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });

        console.log('Response saat update : ', response);

        modal.modal('hide');

        reloadTable(table);

        showSwalSuccess('Berhasil', `Data berita <b>${judul}</b> berhasil <b>ditambahkan</b>`, 3000);
        // toast('success', 'Data berhasil ditambahkan!');
    } catch (error) {
        console.log('Terjadi kesalahan : ', error);
        showSwalGenericError();
    }
}