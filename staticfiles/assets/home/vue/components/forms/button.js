const Button = {
    props: {
        type: { type: String, default: 'button' },
        icon: { type: String, default: 'fa-solid fa-arrow-right-to-bracket' },
    },
    template: `
        <button :type="type" class="btn btn-auth my-3 d-block w-100">
            <i v-if="icon" :class="icon +' me-2'"></i>
            <slot></slot>
        </button>
    `
};

export default Button;
