/* --------------------------
 * SHORTCUT HTTP REQUEST
----------------------------- */
/**
 * Handle Delete Request
 *
 * @param {Object} config Configuration for the request
 *
 * @returns {Boolean}
 */
async function handleDelete(config) {
    /*
     * Configuration Parameters
     * ==========================
     *
     * id: ID of the record being deleted
     * name: Name of the record being deleted
     * apiURL: URL of the API endpoint
     * usingDT: Boolean indicating whether the response is using DataTables, if true it will automatically reload the DataTable
     *
     */

    const id = config?.id;
    const detailName = config?.detail_name ?? '';
    const name = config?.name;
    const apiURL = config?.apiURL;
    const usingDT = config?.usingDT ?? true

    const additionalConfirmInfo = detailName == '' ? 'yang dipilih' : `:<br><b>${detailName}</b>`;
    const additionalResultInfo = detailName == '' ? 'yang dipilih' : `: <b>${detailName}</b>`;

    const confirmationText = `Untuk menghapus data <b>${name}</b> ${additionalConfirmInfo}? <br> Data yang dihapus tidak dapat <b>dipulihkan</b> kembali`;

    const confirmResult = await showSwalConfirm(confirmationText, 'Ya, hapus data');

    if (!confirmResult.isConfirmed) return;

    showSwalLoading();

    await sleep(1000);

    try {
        await axios.delete(`${apiURL}/${id}/`);

        showSwalSuccess('Berhasil', `Data ${name} ${additionalResultInfo} berhasil <b>dihapus</b>`, 3000);

        return true;
    } catch (error) {
        console.log('Terjadi kesalahan : ', error);
        showSwalGenericError();
        return false;
    } finally {
        $('.modal').modal('hide');

        if (usingDT) {
            console.log(config?.usingDT)
            console.log('Reloading all datatables ...');
            reloadAllDataTables();
        }
    }
}

/* --------------------------
 * CSRF TOKENIZATION HELPERS
----------------------------- */
const getCSRFToken = () => getCookie('csrftoken') || document.querySelector('meta[name="csrf-token"]').content;

/**
 * Shortcut get CSRFToken from Cookie for API Response
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Mengecek apakah cookie memiliki nama yang sesuai
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Shortcut getHeaders for API Response (not used)
 */
const getHeaders = (type) => {
    return { "X-CSRFToken": getCSRFToken(), 'Content-Type': type ?? 'application/json' }
}

/**
 * Check status response.
 */
const checkStatus = (status, startNum) => String(status).startsWith(startNum);

/* --------------------------
 * GLOBAL PLUGIN SETTER
----------------------------- */
// ******** AXIOS ********
axios.defaults.headers.common['X-CSRFToken'] = getCSRFToken();
axios.defaults.headers.post['Content-Type'] = 'application/json';

const { createPinia, defineStore } = Pinia;
const pinia = createPinia();
pinia.use(resetStore)