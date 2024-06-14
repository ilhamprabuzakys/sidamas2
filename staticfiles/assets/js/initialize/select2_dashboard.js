/***=======================================================
* DASHBOARD
* CREATE A NEW INSTANCE OF SELECT 2 USING ONLY A CLASSNAME
========================================================***/
$(function () {
    $("select:is(.select2):not(.no-search, .no-placeholder)").each(function () {
        $(this).select2({
            placeholder: $(this).find('option:first').text(),
            dropdownParent: $(this).parent(),
            allowClear: false,
            language: {
                noResults: function () {
                    return `<span style="padding: 12px 15px">Hasil tidak ditemukan</span>`;
                },
            },
            escapeMarkup: function (markup) {
                return markup;
            }
        });
    });

    $("select:is(.select2):is(.no-placeholder)").each(function () {
        $(this).select2({
            dropdownParent: $(this).parent(),
            allowClear: false,
            language: {
                noResults: function () {
                    return `<span style="padding: 12px 15px">Hasil tidak ditemukan</span>`;
                },
            },
            escapeMarkup: function (markup) {
                return markup;
            }
        });
    });

    $("select:is(.select2):is(.no-search)").each(function () {
        $(this).select2({
            dropdownParent: $(this).parent(),
            minimumResultsForSearch: Infinity,
            allowClear: false,
            language: {
                noResults: function () {
                    return `<span style="padding: 12px 15px">Hasil tidak ditemukan</span>`;
                },
            },
            escapeMarkup: function (markup) {
                return markup;
            }
        });
    });
});
