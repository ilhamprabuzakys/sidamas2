const PilihanJenisKelamin = {
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
    template: `
        <div class="row" :id="'pilihan-jenis-kelamin-' + gender">
            <div class="col-5 d-flex justify-content-center">
                <input class="form-check-input" type="radio" :name="radioName" :id="'jenis_kelamin-' + gender" :value="gender" @change="handleRadioChange">
            </div>
            <div class="col-5 d-flex justify-content-start">
                <label class="form-check-label" :for="'jenis_kelamin-' + gender">
                    <h4 class="card-title">{{ detailGender }}</h4>
                </label>
            </div>
        </div>
    `,
    methods: {
        handleRadioChange() {
            console.log('changed jenis kelamin ...');
            this.emitter.emit(`${this.buttonId}-gender-changed`, this.gender);
        },
    },
    computed: {
        detailGender() {
            const genderMap = {
                L: "Laki Laki",
                P: "Perempuan",
            };
            return genderMap[this.gender] || "";
        },
    },
};

export default PilihanJenisKelamin;
