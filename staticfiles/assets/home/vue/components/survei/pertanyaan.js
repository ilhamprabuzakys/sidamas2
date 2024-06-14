const Pertanyaan =  {
    template: `
        <div class="card">
            <div class="card-body">
            <component :is="getElementBySize()" id="questionText" class="card-text text-center">
                <slot></slot>
            </component>
            </div>
        </div>
    `,
    data() {
        return {
            size: "md"
        }
    },
    methods: {
        getElementBySize() {
            const sizeMap = {
                md: "h4",
                sm: "h5",
                xs: "h6",
            };
            return sizeMap[this.size] || "h4";
        }
    },
};

export default Pertanyaan;