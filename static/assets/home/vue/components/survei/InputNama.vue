<template>
    <div id="nama-daftar-pilihan" class="mt-5 fade-in-out">
        <div class="row justify-content-center">
            <input type="text" class="form-control" id="nama_id" @change="handleInput"
                placeholder="Isikan nama lengkap anda">
        </div>
    </div>
</template>
<script>
export default {
    name: 'Inputan Nama',
    methods: {
        handleInput() {
            this.emitter.emit(`nama-changed`, this.value);
        }
    }
};
</script>
<style lang="">
    
</style>