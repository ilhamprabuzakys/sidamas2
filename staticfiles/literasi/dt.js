const columns = [
    {
        data: null,
    },
    {
        data: "judul",
        render: function (data, type, row) {
            return `${data}`;
        },
    },
    {
        data: "dokumen",
        render: function (data, type, row) {
            if (data) {
                return `
            <div class="text-center">
                <a href="${data}" class="badge bg-primary text-white" target="_blank">
                    <i class="fas fa-download me-2"></i>
                    Unduh dokumen
                </a>
            </div>`;
            } else {
                return `<div class="text-center"><a class="text-decoration-none">Kosong</a></div>`;
            }
        },
    },
    {
        data: "kategori",
        render: function (data, type, row) {
            return `<div class="text-center"><a class="text-decoration-none text-primary text-capitilize">${data}</a></div>`;
        },
    },
    {
        data: "status",
        render: function (data, type, row) {
            let output = `<div class="text-center">`;
            let published_output = `<a href="javascript:void(0)" class="badge bg-success">
            <i class="fas fa-check-double me-2"></i>
            PUBLISHED
        </a>`;

            let archived_output = `<a href="javascript:void(0)" class="badge bg-primary">
            <i class="fas fa-archive me-2"></i>
            ARCHIVED
        </a>`;

            let draft_output = `<a href="javascript:void(0)" class="badge bg-secondary">
            <i class="fas fa-pen-to-square me-2"></i>
            DRAFT
        </a>`;

            switch (data) {
                case "published":
                    output += published_output;
                    break;
                case "archived":
                    output += archived_output;
                    break;
                case "draft":
                    output += draft_output;
                    break;
                default:
                    output += draft_output;
            }

            output += `</div>`;
            return output;
        },
    },
    {
        data: "created_by.username",
        render: function (data, type, row) {
            return `<div class="text-center"><a class="text-decoration-none">${data}</a></div>`;
        },
    },
    {
        data: "created_at",
        render: function (data, type, row) {
            var formattedDate = moment(data).format("D MMMM YYYY");
            return `<div class="text-center"><a class="text-decoration-none">${formattedDate}</a></div>`;
        },
    },
    {
        data: "id",
        render: function (data, type, row) {
            const options = JSON.stringify({ id: data, name: 'literasi', detail_name: row.judul, apiURL: '/dashboard/literasi/api/v1' });

            return `
            <div class="list-button gx-3 text-uppercase">
                <div>
                    <a href="javascript:void(0);" onclick="handleDetail(${data})"
                        class="badge bg-primary text-white text-decoration-none mb-1"><i
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
            </div>`;
        },
    },
];

const table = $("#__table").DataTable({
    language: dt_lang_config(),
    serverSide: true,
    searching: true,
    responsive: true,
    pageLength: 10,
    ajax: {
        url: `/dashboard/literasi/api/v1/?format=datatables`,
        dataSrc: "data",
    },
    ordering: true,
    columns: columns,
    createdRow: function (row, data, dataIndex) {
        $(row).attr("data-id", data.id);
        $(row).attr("data-row-index", dataIndex);
    },
    initComplete: function (settings, json) {
        console.log("Hasil fetch data : ", json);
    },
    columnDefs: [
        dt_row_pagination(),
        {
            searchable: false,
            targets: 7,
        },
    ],
});
