/* const columns = [
    {
        data: null,
    },
    {
        data: "judul",
        render: function (data, type, row) {
            return `<div class="text-start"><span class="">${data}</span></div>`;
        },
    },
    {
        data: "kategori.nama",
        render: function (data, type, row) {
            return `<div class="text-start"><span class="">${data}</span></div>`;
        },
    },
    {
        data: "status",
        render: function (data, type, row) {

            const statusIconList = {
                'pending': 'far fa-clock',
                'published': 'fas fa-check-double',
                'draft': 'fas fa-edit',
                'archived': 'fas fa-box-archive',
            };

            const statusBGList = {
                'pending': 'bg-primary',
                'published': 'bg-success',
                'draft': 'bg-warning',
                'archived': 'bg-danger',
            };

            const status_icon = statusIconList[data] || 'fas fa-edit';
            const status_bg = statusBGList[data] || 'bg-primary';

            return `<div class="text-center"><span class="badge ${status_bg} text-white"><i class="${status_icon} me-2"></i>${data.toUpperCase()}</span></div>`;
        },
    },
    {
        data: "created_by.username",
        render: function (data, type, row) {
            return `<div class="text-center"><span class="">${data ?? '-'}</span></div>`;
        },
    },
    {
        data: "created_at",
        render: function (data, type, row) {
            const formattedDate = moment(data).format('D MMMM YYYY');
            return `<div class="text-center"><a class="text-decoration-none">${formattedDate}</a></div>`;
        },
    },
    {
        data: "id",
        render: function (data, type, row) {
            const options = JSON.stringify({ id: data, name: 'berita', detail_name: row.judul, apiURL: '/dashboard/berita/api/v1' });
            const detailURL = `/berita/${row.slug}/`;

            return `
            <div class="list-button gx-3 text-uppercase">
                <div>
                    <a href="${detailURL}" class="badge bg-primary text-white text-decoration-none mb-1"><i
                            class="fas fa-eye me-2"></i>Lihat</a>
                </div>
                <div>
                    <a href="javascript:void(0);" onclick="handleEdit(${data})"
                        class="badge bg-success text-white text-decoration-none mb-1"><i
                            class="fas fa-pen-to-square me-2"></i>Edit</a>
                </div>
                <div>
                    <a href="javascript:void(0);" class="badge bg-danger text-white text-decoration-none mb-1" onclick='handleDelete(${options})'><i
                            class="fas fa-trash-alt me-2"></i>Hapus</a>
                </div>
            </div>
            `;
        },
    },
]; */

/* const table = $('#__table').DataTable({
    language: dt_lang_config(),
    serverSide: true,
    searching: true,
    responsive: true,
    pageLength: 5,
    ajax: {
        url: `/dashboard/berita/api/v1/?format=datatables`,
        dataSrc: 'data'
    },
    ordering: true,
    columns: columns,
    initComplete: function (settings, json) {
        console.log('Hasil fetch data : ', json);
    },
    columnDefs: [dt_row_pagination()]
}); */