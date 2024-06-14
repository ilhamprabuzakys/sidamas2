<template>
    <div :class="'card level-' + bobot" style="height: 100%;">
        <div class="card-body :" style="display: flex;flex-flow: column wrap;align-items: center;justify-content: space-between;">
            <h5 class="card-title text-center text-white" style="font-size: 100%;" :id="'option' + bobot">{{ getTitle }}</h5>
            <img :src="src" :alt="getTitle" style="" class="card-img-top img-fluid">
        </div>
    </div>
</template>
<script>
export default {
    name: 'Pilihan Survei',
    props: {
        bobot: {
            type: String,
            required: true,
            validator: (value) => ["1", "2", "3", "4"].includes(value)
        },
        src: {
            type: String,
            required: true
        }
    },
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
};
</script>