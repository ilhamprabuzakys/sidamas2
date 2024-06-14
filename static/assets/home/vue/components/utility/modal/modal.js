const Modal = {
    props: {
        id: { required: true },
        size: { required: false, default: 'xl' },
        scrollable: { required: false, default: false },
    },
    data() {
        return {
            modalSize: 'modal-',
        }
    },
    template: `
        <div class="modal fade" tabindex="-1" :id="id">
            <div :class="getClasses()">
                <div class="modal-content">
                    <slot></slot>
                </div>
            </div>
        </div>
    `,
    methods: {
        getClasses() {
            return `modal-dialog ${this.modalSize} ${this.scrollable ? 'modal-dialog-scrollable' : ''}`
        }
    },
    mounted() {
        this.modalSize += this.size;
    }
};

export default Modal;
