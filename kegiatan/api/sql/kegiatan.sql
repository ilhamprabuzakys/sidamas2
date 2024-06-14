-- ALL DATA
SELECT row_number() OVER () AS id, A.satker_id, B.nama_satker, COUNT(*) AS jumlah_kegiatan FROM kegiatan_dayatif_binaan_teknis A LEFT JOIN users_satker B ON A.satker_id = B.id GROUP BY B.nama_satker, A.satker_id LIMIT 50;

-- DETAIL DATA
SELECT row_number() OVER () AS id, A.id AS kegiatan_id, A.satker_id as satker_parent_id, B.nama_satker, A.tanggal_awal, A.tanggal_akhir, A.jumlah_hari_pelaksanaan, A.jumlah_peserta, A.tujuan, A.kendala, A.kesimpulan, A.tindak_lanjut, A.dokumentasi FROM kegiatan_dayatif_binaan_teknis A LEFT JOIN users_satker B ON A.satker_target_id = B.id WHERE A.satker_id = {satker_id} ORDER BY B.nama_satker ASC

SELECT
    users_satker.id,
    users_satker.nama_satker,
    kegiatan_dayatif_binaan_teknis.status,
    COUNT(kegiatan_dayatif_binaan_teknis.id) AS jumlah_kegiatan
FROM
    kegiatan_dayatif_binaan_teknis
    INNER JOIN users_satker ON kegiatan_dayatif_binaan_teknis.satker_id = users_satker.id
WHERE
    users_satker.provinsi_id = '32'
GROUP BY
    users_satker.id,
    users_satker.nama_satker,
    kegiatan_dayatif_binaan_teknis.status;