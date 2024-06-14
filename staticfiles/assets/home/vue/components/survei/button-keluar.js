const ButtonKeluar = {
    props: {
        icon: { type: String, default: 'fa-solid fa-arrow-right-from-bracket' },
    },
    template: `
        <button type="button" id="button-keluar" class="btn btn-orange" @click="handleKeluarSurvey">
            <i :class="icon + ' me-2'"></i>
                <slot></slot>
        </button>
    `,
    methods: {
        handleKeluarSurvey() {
            this.emitter.emit(`survey-ended`);
        },
    }
};

export default ButtonKeluar;