const columns = [
    {
        data: 'judul',
        render: function (data, type, row) {
            const output = `<div class="detail_literasi">
                <h5>
                    ${data}
                </h5>
                <div class="detail_uploader">
                    Diunggah oleh:
                    <span class="text-muted text-uppercase">${row.created_by.first_name} ${row.created_by.last_name},
                        <span class="text-dark">DEPUTI BIDANG PEMBERDAYAAN MASYARAKAT BNN</span></span>
                </div>
            </div>`;

            return `${output}`;
        }
    },
    {
        data: 'jumlah_diunduh',
        render: function (data, type, row) {
            let output = `<span class="text-secondary">[<span class="text-dark">${data}</span><i
            class="fas fa-download ms-1 text-primary"></i>]</span>`;

            return `${output}`;
        }
    },
    {
        data: 'id',
        render: function (data, type, row) {
            return `
                <span onclick="handleDetail(${data})"
                class="btn btn-success w-100 btn-sm"><i class="fas fa-book-open"></i></span>
            `;
        }
    }];

const table = $('#__table').DataTable({
    language: dt_lang_config(),
    serverSide: true,
    searching: true,
    responsive: true,
    pageLength: 10,
    ajax: {
        url: '/dashboard/literasi/api/v1/?format=datatables&ordering=judul',
        dataSrc: 'data'
    },
    ordering: true,
    order: [[1, 'asc']],
    columns: columns,
    initComplete: function (settings, json) {
        console.log('Hasil fetch data : ', json);
    },
    columnDefs: [{
        orderable: false,
        targets: [0, 1, 2]
    }]
});