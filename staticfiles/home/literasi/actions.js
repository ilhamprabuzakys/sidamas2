async function handleDetail(id) {
    const modal = $('#detailModal');

    const response = await axios.get(`/dashboard/literasi/api/v1/${id}/`);
    const data = response.data;

    const dokumenExt = data.dokumen.split('.').pop();

    modal.find('#detail_judul').text(data.judul);
    modal.find('#detail_wadah').attr('src', data.dokumen);
    modal.find('#detail_dokumen').attr('href', data.dokumen).attr('download', `${data.judul}`);

    await axios.get(`/dashboard/literasi/api/v1/${id}/increment_unduhan/`);

    modal.modal('show');
}