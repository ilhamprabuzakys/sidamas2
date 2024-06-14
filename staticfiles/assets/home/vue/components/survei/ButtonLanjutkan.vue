<template>
    <button class="btn btn-mulai w-100">
    <!-- <button class="btn btn-mulai w-100" :class="{ 'disabled': !isActive }"> -->
        <i :class="icon + ' me-3'"></i>
        <slot></slot>
    </button>
</template>
<script>
export default {
    name: 'Button Lanjutkan',
    props: { id: { type: String, required: true } },
    data() {
        return {
            icon: "fas fa-arrow-right",
            isActive: false,
        };
    },
    mounted() {
        this.emitter.on(`nama-changed`, this.handleRadioChanged);
        this.emitter.on(`${this.id}-gender-changed`, this.handleRadioChanged);
        this.emitter.on(`${this.id}-usia-changed`, this.handleRadioChanged);
        this.emitter.on(`${this.id}-pendidikan-changed`, this.handleRadioChanged);
        this.emitter.on(`survey-ended`, this.handleSurveyEnded);
    },
    destroyed() {
        // Tidak berpengaruh karena bukan web SPA
        // this.emitter.off(`${this.id}-gender-changed`, this.handleRadioChanged);
        // this.emitter.off(`${this.id}-usia-changed`, this.handleRadioChanged);
        // this.emitter.off(`${this.id}-pendidikan-changed`, this.handleRadioChanged);
    },
    methods: {
        handleSurveyEnded() {
            this.isActive = false;
            // console.log('survei telah berakhir, state button direset ke semula ...');
        },
        handleRadioChanged() {
            // console.log('menghandle radio changed ...');
            // console.log('isActive:', this.isActive);
            this.isActive = true;
            // console.log('setelah perubahan isActive:', this.isActive);
        },
    },
};
</script>