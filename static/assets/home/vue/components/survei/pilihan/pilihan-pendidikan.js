const PilihanPendidikan = {
    props: {
        value: { type: String, required: true },
        buttonId: { type: String, required: true },
    },
    data() {
        return {
            radioName: "pendidikan_terakhir",
        };
    },
    template: `
        <div class="row">
            <div class="col d-flex justify-content-center">
                <input class="form-check-input" type="radio" :name="radioName"
                    :id="getID()" :value="value" @change="handleRadioChange">
            </div>
            <div class="col d-flex justify-content-start">
                <label class="form-check-label" :for="getID()">
                    <h4 class="card-title">
                        <slot></slot>
                    </h4>
                </label>
            </div>
        </div>
    `,
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

export default PilihanPendidikan;
