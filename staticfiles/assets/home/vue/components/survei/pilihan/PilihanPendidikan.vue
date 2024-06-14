<template>
    <div class="form-check">
        <input class="form-check-input" type="radio" :name="radioName" :id="getID()" :value="value" @change="handleRadioChange">
        <label class="form-check-label" :for="getID()">
        <h4 class="card-title"><slot></slot></h4>
        </label>
    </div>
</template>
<script>
export default {
    name: 'Pilihan Pendidikan',
    props: {
        value: { type: String, required: true },
        buttonId: { type: String, required: true },
    },
    data() {
        return {
            radioName: "pendidikan_terakhir",
        };
    },
    methods: {
        getID() {
            let modifiedValue = this.value.replace(/\s/g, "").toLowerCase();
            return "pendidikan_terakhir-" + modifiedValue;
        },
        handleRadioChange() {
            this.emitter.emit(`${this.buttonId}-pendidikan-changed`, this.value);
        },
    },
};
</script>