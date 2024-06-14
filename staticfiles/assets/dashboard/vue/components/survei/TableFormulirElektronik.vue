<template>
      <DataTable :columns="columns" :data="formData" />
    <!-- <table class="table table-bordered" id="__table">
        <thead class="bg-soft-green">
            <tr>
                <th>No.</th>
                <th>Nama Formulir</th>
                <th>Jumlah Responden</th>
                <th>Berlaku Sampai</th>
                <th>
                    AKSI<i class="fas fa-edit ms-2"></i>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr class="">
                <td scope="row">1</td>
                <td>Formulir Life Skill Warga Setempat Bandung Oktober 2023</td>
                <td>33</td>
                <td>31 Desember 2023</td>
                <td class="__action_button">
                    <div class="list-button gx-3 text-uppercase">
                        <div>
                            <a href="javascript:;" class="badge bg-primary text-white text-decoration-none mb-1"><i
                                    class="fas fa-print me-2"></i>Buat link</a>
                        </div>
                        <div>
                            <a href="javascript:;" class="badge bg-success text-white text-decoration-none mb-1"><i
                                    class="fas fa-pen-to-square me-2"></i>Edit</a>
                        </div>
                        <div>
                            <a href="javascript:;" class="badge bg-danger text-white text-decoration-none mb-1"><i
                                    class="fas fa-trash-alt me-2"></i>Hapus</a>
                        </div>
                    </div>
                </td>
            </tr>
            <tr class="">
                <td scope="row">2</td>
                <td>Formulir Life Skill Warga Setempat Kalimanatan Mei 2023</td>
                <td>21</td>
                <td>13 Agustus 2023</td>
                <td class="__action_button">
                    <div class="list-button gx-3 text-uppercase">
                        <div>
                            <a href="javascript:;" class="badge bg-primary text-white text-decoration-none mb-1"><i
                                    class="fas fa-print me-2"></i>Buat link</a>
                        </div>
                        <div>
                            <a href="javascript:;" class="badge bg-success text-white text-decoration-none mb-1"><i
                                    class="fas fa-pen-to-square me-2"></i>Edit</a>
                        </div>
                        <div>
                            <a href="javascript:;" class="badge bg-danger text-white text-decoration-none mb-1"><i
                                    class="fas fa-trash-alt me-2"></i>Hapus</a>
                        </div>
                    </div>
                </td>
            </tr>
            <tr class="">
                <td scope="row">3</td>
                <td>Formulir Life Skill Warga Setempat Jakarta Februari 2023</td>
                <td>83</td>
                <td>20 April 2023</td>
                <td class="__action_button">
                    <div class="list-button gx-3 text-uppercase">
                        <div>
                            <a href="javascript:;" class="badge bg-primary text-white text-decoration-none mb-1"><i
                                    class="fas fa-print me-2"></i>Buat link</a>
                        </div>
                        <div>
                            <a href="javascript:;" class="badge bg-success text-white text-decoration-none mb-1"><i
                                    class="fas fa-pen-to-square me-2"></i>Edit</a>
                        </div>
                        <div>
                            <a href="javascript:;" class="badge bg-danger text-white text-decoration-none mb-1"><i
                                    class="fas fa-trash-alt me-2"></i>Hapus</a>
                        </div>
                    </div>
                </td>
            </tr>
        </tbody>
    </table> -->
</template>
<script setup>
import DataTable from './datatables.js';

</script>
<script>
export default {
    components: {
        DataTable,
    },
    data() {
        return {
            columns: [
                { label: 'No.', key: 'id' },
                { label: 'Nama Formulir', key: 'namaFormulir' },
                { label: 'Jumlah Responden', key: 'jumlahResponden' },
                { label: 'Berlaku Sampai', key: 'berlakuSampai' },
                { label: 'Aksi', key: 'aksi' },
            ],
            formData: [
                {
                    id: 1,
                    namaFormulir: 'Formulir Life Skill Warga Setempat Bandung Oktober 2023',
                    jumlahResponden: 33,
                    berlakuSampai: '31 Desember 2023',
                    aksi: '<div class="list-button gx-3 text-uppercase"><div><a href="javascript:;" class="badge bg-primary text-white text-decoration-none mb-1"><i class="fas fa-print me-2"></i>Buat link</a></div><div><a href="javascript:;" class="badge bg-success text-white text-decoration-none mb-1"><i class="fas fa-pen-to-square me-2"></i>Edit</a></div><div><a href="javascript:;" class="badge bg-danger text-white text-decoration-none mb-1"><i class="fas fa-trash-alt me-2"></i>Hapus</a></div></div>',
                },
                {
                    id: 2,
                    namaFormulir: 'Formulir Life Skill Warga Setempat Kalimanatan Mei 2023',
                    jumlahResponden: 21,
                    berlakuSampai: '13 Agustus 2023',
                    aksi: '<div class="list-button gx-3 text-uppercase"><div><a href="javascript:;" class="badge bg-primary text-white text-decoration-none mb-1"><i class="fas fa-print me-2"></i>Buat link</a></div><div><a href="javascript:;" class="badge bg-success text-white text-decoration-none mb-1"><i class="fas fa-pen-to-square me-2"></i>Edit</a></div><div><a href="javascript:;" class="badge bg-danger text-white text-decoration-none mb-1"><i class="fas fa-trash-alt me-2"></i>Hapus</a></div></div>',
                },
                {
                    id: 3,
                    namaFormulir: 'Formulir Life Skill Warga Setempat Jakarta Februari 2023',
                    jumlahResponden: 83,
                    berlakuSampai: '20 April 2023',
                    aksi: '<div class="list-button gx-3 text-uppercase"><div><a href="javascript:;" class="badge bg-primary text-white text-decoration-none mb-1"><i class="fas fa-print me-2"></i>Buat link</a></div><div><a href="javascript:;" class="badge bg-success text-white text-decoration-none mb-1"><i class="fas fa-pen-to-square me-2"></i>Edit</a></div><div><a href="javascript:;" class="badge bg-danger text-white text-decoration-none mb-1"><i class="fas fa-trash-alt me-2"></i>Hapus</a></div></div>',
                },
            ],
        };
    },
};
</script>
<style lang="">
    
</style>