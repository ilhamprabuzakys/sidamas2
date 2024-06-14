const RentangUsia = {
    props: { 
        value: { type: String, required: true },
        buttonId: { type: String, required: true },
    },
    data() {
        return {
            radioName: "rentang_usia",
        }
    },
    template: `
        <div class="row">
            <div class="col-3 d-flex">
                <input class="form-check-input" type="radio" :name="radioName" :id="'rentang_usia-' + value"
                    :value="value" @change="handleRadioChange">
            </div>
            <div class="col-9 d-flex">
                <label class="form-check-label" :for="'rentang_usia-' + value">
                    <h4 class="card-title">{{ value + " tahun"}}</h4>
                </label>
            </div>
        </div>
    `,
    methods: {
        handleRadioChange() {
            this.emitter.emit(`${this.buttonId}-usia-changed`, this.value);
        },
    },
};

export default RentangUsia;