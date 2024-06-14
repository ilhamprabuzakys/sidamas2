/**
 * Datatable language configuration.
 */
const dt_lang_config = () => ({
    sEmptyTable: 'Tidak ada data yang tersedia pada tabel ini',
    sProcessing: 'Sedang memproses...',
    sLengthMenu: 'Tampilkan _MENU_ entri',
    sZeroRecords: 'Tidak ditemukan data yang sesuai',
    sInfo: 'Menampilkan _START_ sampai _END_ dari _TOTAL_ entri',
    sInfoEmpty: 'Menampilkan 0 sampai 0 dari 0 entri',
    sInfoFiltered: '(disaring dari _MAX_ entri keseluruhan)',
    sInfoPostFix: '',
    sSearch: 'Pencarian:',
    sUrl: '',
    oPaginate: {
        sFirst: `<i class="fas fa-angle-double-left"></i>`,
        sPrevious: `<i class="fas fa-angle-left"></i>`,
        sNext: `<i class="fas fa-angle-right"></i>`,
        sLast: `<i class="fas fa-angle-double-right"></i>`,

        // sFirst: 'Awal',
        // sPrevious: 'Sebelumnya',
        // sNext: 'Berikutnya',
        // sLast: 'Akhir'
    },
});

/**
 * DataTable get row pagination configuration.
 */
const dt_row_pagination = () => ({
    targets: 0,
    render: function (data, type, row, meta) {
        const page = table.page.info().page;
        const length = table.page.info().length;
        const index = (page * length) + meta.row + 1;
        return index;
    }
});

/**
 * Reloading DataTable instance.
 */
const reloadAllDataTables = () => {
    if (typeof table !== 'undefined') {
        table.ajax.reload();
    }
    if (typeof childTable !== 'undefined') {
        childTable.ajax.reload();
    }
    // const tables = $.fn.dataTable.tables(true);

    // $(tables).each(function() {
    //     const dataTable = $(this).dataTable().api();
    //     dataTable.ajax.reload(null, false);
    // });
}

const reloadTable = (table) => table?.ajax?.reload();
const reloadDT = () => reloadAllDataTables();

/**
 * DataTable filter options string formatting.
 */
const convertToTitleCaseAndReplaceSpace = (input) => {
    if (!input) return;

    return input.split(' ').map(word => {
        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    }).join('+');
}

/**
 * DataTable processing event combined with BlockUI.
 */
$(document).on('processing.dt', function (e, settings, processing) {
    if (!processing) {
        unblock($(settings.nTable).parent());
        return;
    }

    block($(settings.nTable).parent());
});
