var s = '';

function getURL() {
    let modified_url = `/dashboard/berita/api/v1/?format=datatables`;
    if (s != '') {
        s = convertToTitleCaseAndReplaceSpace(s);
        modified_url += `&s=${s}`;
    } else {
        modified_url = '/dashboard/berita/api/v1/?format=datatables';
    }
    return modified_url;
}

$(function () {
    let timeoutId;

    $('#__table_wrapper input[type="search"]').on('keyup', function () {
        table.settings()[0].jqXHR.abort();

        clearTimeout(timeoutId);

        timeoutId = setTimeout(function () {

            s = $(this).val();

            const url = getURL();

            console.log('URL:', url);

            table.ajax.url(url).load();
        }.bind(this), 500);
    });

});