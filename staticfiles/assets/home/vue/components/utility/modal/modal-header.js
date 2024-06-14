const ModalHeader = {
    props: {
        size: { required: false, default: 'h2' },
    },
    template: `
        <div class="modal-header">
            <component class="modal-title" :is="getElementBySize()">
                <slot></slot>
            </component>
            
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
    `,
    methods: {
        getElementBySize() {
            return this.size || "h2";
        }
    },
};

export default ModalHeader;
