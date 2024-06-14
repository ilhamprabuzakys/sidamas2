async function hapusDataResponden(pk, tanggal_survei) {
    console.log(`Responden ID: ${pk}`);

    const apiUrl = `/survei/api/v1/data_responden_survei/${pk}/`;

    const confirmResult = await Swal.fire({
        title: 'Apakah anda yakin?',
        html: `Apakah anda yakin untuk <b>menghapus</b> data responden ID ke - <b>${pk}</b>` + ' ?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Ya, hapus data',
        cancelButtonText: 'Batalkan',
    });

    if (!confirmResult.isConfirmed) {
        return false;
    }

    Swal.fire({
        title: 'Tunggu sebentar',
        icon: 'info',
        html: `Sedang <b>menghapus</b> data responden ID ke <b>${pk}</b>`,
        showConfirmButton: true,
        didOpen: () => {
            Swal.showLoading();
        },
    });

    sleep(1000);

    try {
        const response = await api.delete(apiUrl, pk);

        console.log('Response setelah aksi DELETE data responden: ', response);

        if (response.status !== 204) {
            console.error('Terjadi Kesalahan : Response status is not 204');

            Swal.fire({
                title: "Terjadi Kesalahan",
                html: `Terjadi Kesalahan <b>tidak diketahui</b>, kontak developer untuk mengatasi masalah ini.`,
                icon: "error",
                confirmButtonText: "OK",
            });

            return false;
        }

        Swal.fire({
            title: 'Berhasil',
            icon: 'success',
            html: `Data responden ID ke <b>${pk}</b> berhasil di <b>hapus</b>`,
            showConfirmButton: true,
            timer: 2500,
        });

        $('.modal').modal('hide');
        table.ajax.reload();

    } catch (error) {
        console.error('Error msg: ', error);

        Swal.fire({
            title: "Terjadi Kesalahan",
            html: `Terjadi Kesalahan <b>tidak diketahui</b>, kontak developer untuk mengatasi masalah ini.`,
            icon: "error",
            confirmButtonText: "OK",
        });

    }
}