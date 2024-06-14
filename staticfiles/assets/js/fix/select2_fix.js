// FIX SELECT 2 ON MODAL
$('.modal').on('shown.bs.modal', function () {
    if ($(this).find('.modal-dialog-scrollable .modal-body').find('select.select2').length > 0) {
        $(this).find('.modal-dialog-scrollable .modal-body').css('overflow-x', 'hidden');
    }
});

// FIX OVERFLOW-X AXIS INSIDE SCROLLABLE DIALOG MODAL
$('.modal').on('hidden.bs.modal', function () {
    $(this).find('.modal-dialog-scrollable .modal-body').css('overflow-x', '');
});