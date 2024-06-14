/**
 * Append an asterisk to the required label
 */
document.querySelectorAll("label.required").forEach((label) => {
    const supElement = document.createElement("sup");
    supElement.className = "ms-0-15r text-danger";
    supElement.textContent = "*";

    label.appendChild(supElement);
});

/**
 * Append an optional text to the label
 */
document.querySelectorAll("label.optional").forEach((label) => {
    const supElement = document.createElement("span");
    supElement.className = "ms-2 text-muted";
    supElement.textContent = "(Opsional)";

    label.appendChild(supElement);
});


/* --------------------------
 * Form Reset functionallity
----------------------------- */
$(function () {
    // Reset
    function resetForm(form) {
        if (!form || typeof form.hasClass !== 'function') { return; }

        // If using form object
        if (form.hasClass('dont-reset') || form.hasClass('filter-form')) {
            // console.log('Form not resetted because it\'s forbidden ...');
            form.find('.select2').val(null).trigger('change');
            return;
        }

        form.find('.select2').val(null).trigger('change');
        form.find('input[type="text"]').val('');
        form.find('input[type="number"]').val(0);
        form.find('input[type="textarea"]').val('');
        form.find('input[type="checkbox"]').prop('checked', false);
        form.find('input[type="file"]').val(null);

        // console.log('Resetted this form :', form);

        form.trigger('reset');
    }


    $('.modal').on('hidden.bs.modal', function () {
        const form = $(this).closest('form');
        // console.log('Form awal :', form);

        if (form) {
            resetForm(form);
        }
    });


    $('[type="reset"]').on('click', function () {
        let form = $(this).closest('form')[0];
        if (!form) return;
        resetForm(form);
    });
});

/* --------------------------
 * Cleave JS
----------------------------- */
if (window.Cleave) {
    // Phone number
    const phone = document.querySelector('.cleave-phone');
    phone && new Cleave(phone, {
        phone: true,
        phoneRegionCode: "ID",
    });

    const ikp = document.querySelectorAll('.cleave-ikp');
    if (ikp.length > 0) {
        ikp.forEach(element => {
            new Cleave(element, {
                delimiters: [","],
                blocks: [1, 2],
                numericOnly: true,
                min: 0,
                max: 4,
            });
        });
    }
}

/* --------------------------
 * Input Masks
----------------------------- */
$(function() {
    /* --------------------------
    * Bootstrap Max-Min Length
    ----------------------------- */
    const inputMaxLengths = $('input').filter(function() { return $(this).attr('maxlength'); });

    if (inputMaxLengths) {
        inputMaxLengths.each(function (index, element) {
            const maxLength = $(element).attr("maxlength");

            if ($(element).attr('type') === 'number') {
                $(element).attr('type', 'text');
                // $(element).inputmask({ mask: '9'.repeat(maxLength) });
                $(element).maxlength({
                    validate: !0,
                    alwaysShow: false,
                    threshold: maxLength,
                    warningClass: "text-white",
                    limitReachedClass: "text-white",
                    separator: '',
                    preText: '',
                    postText: '',
                })
            }

            if ($(element).attr('type') === 'text') {
                $(element).maxlength({
                    validate: !0,
                    alwaysShow: false,
                    threshold: maxLength,
                    warningClass: "text-white",
                    limitReachedClass: "text-white",
                    separator: '',
                    preText: '',
                    postText: '',
                })
            }
        });
    }

    $('.mask-currency').inputmask({
        alias: 'currency',
        groupSeparator: '.',
        autoGroup: true,
        digits: 0,
        allowMinus: false,
        rightAlign: false,
        placeholder: '0'
    });


    $('.mask-hasil-nilai').inputmask({
        mask: ["9,99"],
        greedy: false,
        numericInput: false,
        rightAlign: false,
    }).on('input', function() {
        const value = parseFloat($(this).val().replace(',', '.'));
        const checkingState = isNaN(value) || value < 1 || value > 4;

        if (!checkingState) return;

        if (value > 4) {
            $(this).val('4,00');
        } else if (value < 1) {
            $(this).val('1,00');
        } else {
            $(this).val('');
        }
    });

    $('.mask-phone').inputmask({
        mask: '9999-9999-9999',
        clearIncomplete: true,
        rightAlign: false,
    }).on('input', function() {
        const phoneNumber = $(this).val();
        if (phoneNumber && phoneNumber[0] !== '0') $(this).val('');
    });

    $('.mask-email').inputmask({
        mask: '*{1,}@*{1,}',
        placeholder: 'example@domain.com',
        clearIncomplete: true,
        rightAlign: false,
    });
});


/* --------------------------
 * FORM VALIDATION
----------------------------- */
const isValidEmail = (email) => /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/.test(email);