<template>
            <div class="form-check" style="display: flex; align-items: stretch;" :id="'pilihan-jenis-kelamin-' + gender">
                <input class="form-check-input" type="radio" :name="radioName" :id="'jenis_kelamin-' + gender" :value="gender" @change="handleRadioChange">
                <label class="form-check-label" style="margin-left: 5px;" :for="'jenis_kelamin-' + gender">
                <h5 class="card-title">{{ detailGender }}</h5>
                </label>
            </div>
</template>
<script>
export default {
    name: 'Pilihan Jenis Kelamin',
    props: {
        gender: {
            type: String,
            required: true,
            validator: (value) => ["L", "P"].includes(value),
        },
        buttonId: { type: String, required: true },
    },
    data() {
        return {
            radioName: "jenis_kelamin",
        }
    },
    methods: {
        handleRadioChange() {
            this.emitter.emit(`${this.buttonId}-gender-changed`, this.gender);
        },
    },
    computed: {
        detailGender() {
            const genderMap = {
                L: " Laki-laki",
                P: " Perempuan",
            };
            return genderMap[this.gender] || "";
        },
    },
}
</script>