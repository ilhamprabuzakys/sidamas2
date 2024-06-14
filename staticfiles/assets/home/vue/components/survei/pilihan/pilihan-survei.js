const PilihanSurvei = {
    props: {
        bobot: {
            type: String,
            required: true,
            validator: (value) => ["1","2","3","4"].includes(value)
        },
        src: {
            type: String,
            required: true
        }
    },
    template: `
        <div :class="'card level-' + bobot" @click="jawabSurvei">
            <div class="card-body">
                <h4 class="card-title" :id="'option' + bobot">{{ getTitle }}</h4>
                <img :src="src" class="img-fluid" style="max-width: 50%; width: 50px; height: auto;" :alt="getTitle">
            </div>
        </div>
    `,
    methods: {
        jawabSurvei() {
            jawab(this.bobot);
        },
    },
    computed: {
        getTitle() {
            const mapTitle = {
                "1": "Sangat Tidak Setuju",
                "2": "Tidak Setuju",
                "3": "Setuju",
                "4": "Sangat Setuju"
            };
            return mapTitle[this.bobot] || "0";
        }
    }
}

export default PilihanSurvei;