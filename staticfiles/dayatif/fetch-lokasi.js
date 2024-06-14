/**
 * @source_url : https://sikawan.surveydm.web.id
 * @description : Data Lokasi Fetcher
 * @author : Ilham
 * @updated : 2024-04-15
 * @requirement : ['create__{lokasi}', 'edit__{lokasi}']
 */

const BASE_API_URL = 'https://sikawan.surveydm.web.id';
let listProvinces = null;

const API_URLS = {
    regencies: BASE_API_URL + '/dashboard/masters/api/v1/list_regencies/?provinsi=',
    districts: BASE_API_URL + '/dashboard/masters/api/v1/list_districts/?kabupaten=',
    villages: BASE_API_URL + '/dashboard/masters/api/v1/list_villages/?kecamatan=',
    provinces: BASE_API_URL + '/dashboard/masters/api/v1/provinces/',
};

const semuaOption = '<option value="">Semua</option>';

/* --------------------------
    * Dropdown Resetter
----------------------------- */
const resetKabupaten = (type) => {
    $(`#${type}__kabupaten`).empty();
    $(`#${type}__kabupaten`).append($(`<option>`, {
        value: '',
        text: '--Pilih kabupaten/kota--',
        disabled: true,
    }));
    $(`#${type}__kabupaten`).prop(`disabled`, true);
    $(`#${type}__kecamatan`).prop(`disabled`, true);
    $(`#${type}__kabupaten`).append(semuaOption);
}

const resetKecamatan = (type) => {
    $(`#${type}__kecamatan`).empty();
    $(`#${type}__kecamatan`).append($('<option>', {
        value: '',
        text: '--Pilih kecamatan--',
        disabled: true
    }));
    $(`#${type}__kecamatan`).prop('disabled', true);
    $(`#${type}__kecamatan`).append(semuaOption);
}

const resetDesa = (type) => {
    $(`#${type}__desa`).empty();
    $(`#${type}__desa`).append($('<option>', {
        value: '',
        text: '--Pilih desa/kelurahan--',
        disabled: true
    }));
    $(`#${type}__desa`).prop('disabled', true);
    $(`#${type}__desa`).append(semuaOption);
}

const dropdownOptions = {
    kabupaten: { callback: resetKabupaten, url: API_URLS.regencies },
    kecamatan: { callback: resetKecamatan, url: API_URLS.districts },
    desa: { callback: resetDesa, url: API_URLS.villages }
};

/* --------------------------
    * Dropdown Data Fetcher
----------------------------- */
const fetchDropdownData = async (url, id, dropdown, type, resetFunction) => {
    if (!id) return;

    resetFunction();

    try {
        const response = await axios.get(url);

        response.data.forEach(value => {
            dropdown.append($('<option>', {
                value: value.id,
                text: value[`nama_${type}`]
            }));
        });

        dropdown.removeAttr('disabled');
    } catch (error) {
        console.error(error);
    }
}

const loadDropdownData = async (type, id, dropdown) => {
    const { callback, url } = dropdownOptions[type];
    await fetchDropdownData(`${url}${id}`, id, dropdown, type, callback);
}

/* --------------------------
    * Setup Data Provinsi
----------------------------- */
const fetchProvinsi = async () => {
    try {
        const response = await axios.get(API_URLS.provinces);
        listProvinces = response.data.results;
    } catch (error) {
        console.error(error);
    }
}

const assignProvinsi = async (type) => {
    const provinsiDropdown = $(`#${type}__provinsi`);

    listProvinces.forEach(value => {
        provinsiDropdown.append($('<option>', {
            value: value.id,
            text: value.nama_provinsi
        }));
    });

    provinsiDropdown.removeAttr('disabled');
}

/* --------------------------
    * Perform Action
----------------------------- */
$(function () {
    (async () => {
        try {
            /* --------------------------
                * Initial Fetch
            ----------------------------- */
            await fetchProvinsi();
            await Promise.all([assignProvinsi('create'), assignProvinsi('edit')]);

            /* --------------------------
                * Event Listener
            ----------------------------- */
            $('#create__provinsi, #edit__provinsi').on('change', async function () {
                const value = $(this).val();
                const type = $(this).attr('id').split('__')[0];
                const isValid = value && value !== '';

                if (!isValid) {
                    resetKabupaten(type);
                    resetKecamatan(type);
                    resetDesa(type);

                    return;
                }

                await loadDropdownData('kabupaten', value, $(`#${type}__kabupaten`));
            });

            $('#create__kabupaten, #edit__kabupaten').on('change', async function () {
                const value = $(this).val();
                const type = $(this).attr('id').split('__')[0];
                const isValid = value && value !== '';

                if (!isValid) {
                    resetKecamatan(type);
                    resetDesa(type);

                    return;
                }

                await loadDropdownData('kecamatan', value, $(`#${type}__kecamatan`));
            });

            $('#create__kecamatan, #edit__kecamatan').on('change', async function () {
                const value = $(this).val();
                const type = $(this).attr('id').split('__')[0];
                const isValid = value && value !== '';

                if (!isValid) {
                    resetDesa(type);

                    return;
                }

                await loadDropdownData('desa', value, $(`#${type}__desa`));
            });
        } catch (error) {
            console.error('Terjadi kesalahan saat memuat data wilayah :', error);
        }
    })();
});