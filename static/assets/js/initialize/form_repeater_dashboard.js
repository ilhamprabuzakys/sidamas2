$(function () {
    const $repeaters = $('.form-repeater');

    $repeaters.on('submit', (e) => e.preventDefault());

    $repeaters.repeater(getRepeaterConfig({ isFirstItemUndeletable: true }));
});

/* --------------------------
 * FORM REPEATER CUSTOM CONFIG
----------------------------- */
function getRepeaterConfig(config) {
    return {
       isFirstItemUndeletable: config?.isFirstItemUndeletable ?? false,
       show: function () {
            const $formControls = $(this).find(".form-control, .form-select"), $formLabels = $(this).find(".form-label");
            let controlIndex = 0, labelIndex = 0;

            $formControls.each(function (index) {
                const elementID = `form-repeater-${controlIndex}-${labelIndex}`;

                $($formControls[index]).attr("id", elementID);
                $($formLabels[index]).attr("for", elementID);

                labelIndex++;
            });

            controlIndex++;

            $(this).slideDown();
       },
       hide: async function (e) {
           const isFilledIn = $(this).find('input[type="text"], input[type="radio"], input[type="number"]').filter(function() {
               if ($(this).attr('type') === 'radio' || $(this).attr('type') === 'checkbox') {
                   return $(this).is(':checked');
               } else {
                   return $(this).val() !== "";
               }
           }).length > 0;

           if (!isFilledIn) {
               $(this).slideUp(e);
               return;
           }

           const confirmationText = `Apakah anda yakin untuk menghapus data ini? <br>Data yang sudah <b>terisi</b> akan dihapus!`;
           const confirmation = await showSwalConfirm(confirmationText, 'Ya, hapus data');
           confirmation.isConfirmed && $(this).slideUp(e);
       },
   }
}