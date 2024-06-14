const InputGroup = {
    props: {
        label: { type: String, required: true },
        icon: { type: String, required: true },
        placeholder: { type: String },
        type: { type: String, required: true },
        id: { type: String },
        name: { type: String, required: true },
        modelValue: { type: String, default: "" },
        required: { required: false, default: false },
    },
    data() {
        return {
            showPassword: false,
            inputValue: this.modelValue,
        };
    },
    template: `
        <div class="mb-3">
            <label :for="id" class="form-label">{{ label }}</label>
            <div class="input-group">
                <span class="input-group-text"><i :class="icon"></i></span>
                <input
                    :required="required"
                    :type="getType()"
                    class="form-control"
                    :placeholder="placeholder || label"
                    :aria-label="id"
                    :aria-describedby="id"
                    :id="id || name"
                    :value="inputValue" 
                    @input="updateInputValue($event)" 
                    :name="name"
                    :ref="name"
                />
                <span v-if="isPasswordInput()" class="input-group-text password-toggle" @click="togglePasswordVisibility">
                    <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
                </span>
            </div>
        </div>
    `,
    methods: {
        togglePasswordVisibility() {
            this.showPassword = !this.showPassword;
        },
        isPasswordInput() {
            return this.type === "password";
        },
        getType() {
            if (this.isPasswordInput()) {
                return !this.showPassword ? "password" : "text";
            }
            return this.type;
        },
        updateInputValue(event) {
            this.inputValue = event.target.value;
            this.$emit('update:modelValue', this.inputValue);
        },
    },
};

// setup(props, context) {
//     const updateValue = (event) => {
//         context.emit('update:modelValue', event.target.value);
//     }

//     return { updateValue }
// },

export default InputGroup;
