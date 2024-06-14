<template>
    <!-- Blok Masukan Kode -->
    <section id="masukan-container" class="">
        <form onsubmit="bukaSurvei(event)" method="">
            <div class="row justify-content-center">
                <div class="col-lg-7 col-sm-12 d-flex justify-content-center align-items-center">
                    <div class="mb-3">
                        <div class="mb-5">
                            <h2 class="text-mulai text-center">
                                Masukan kode survei untuk <strong>Membuka</strong>
                                surveinya!
                            </h2>
                        </div>
                        <label for="" class="form-label">Kode Survei</label>
                        <input type="text" class="form-control" name="" id="input-code" aria-describedby="helpId"
                            placeholder="" />
                    </div>
                </div>
            </div>
            <div class="row mt-4">
                <div class="col-12 d-flex justify-content-center">
                    <button type="submit" id="button-masuk" class="btn btn-mulai"><i class="fas fa-lock-open me-3"></i>Buka
                        Survei</button>
                </div>
            </div>
        </form>
    </section>
    <!-- End of Blok Masukan Kode -->
</template>
<script>
export default {
    name: 'Masukan Kode',
};
</script>
<style>
#button-mulai {
    color: #fff;
}
</style>