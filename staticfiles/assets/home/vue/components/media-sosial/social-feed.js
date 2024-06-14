const SocialFeed = {
    props: {
        name: {
            type: String,
            required: true,
            validator: (value) => ["instagram", "twitter", "tiktok", "youtube"].includes(value)
        },
        embedid: {
            type: String,
            required: true
        }
    },
    template: `
        <section :id="name" class="px-2">
            <h4 class="headline">{{ capitalizeFirstLetter(name) }}</h4>
            <hr>
            <div class="sosial-container">
                <div :class="embedClass" :data-embed-id="embedid" ref="socialContainer"></div>
            </div>
        </section>
    `,
    computed: {
        embedClass() {
            return this.getPrefixScript() + this.name + this.getSuffixScript();
        }
    },
    methods: {
        capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
        },
        getScriptUrl() {
            return `https://widgets.sociablekit.com/${this.name}${this.getSuffixScript()}/widget.js`;
        },
        getPrefixScript() {
            const prefixMap = {
                instagram: "sk-ww-",
                twitter: "sk-ww-",
                tiktok: "sk-",
                youtube: "sk-ww-"
            };
            return prefixMap[this.name] || "";
        },
        getSuffixScript() {
            const suffixMap = {
                instagram: "-reels",
                twitter: "-feed",
                tiktok: "-feed",
                youtube: "-channel-videos"
            };
            return suffixMap[this.name] || "";
        }
    },
    mounted() {
        const script = document.createElement('script');
        script.src = this.getScriptUrl();
        script.async = true;
        script.defer = true;

        this.$refs.socialContainer.appendChild(script);
    }
};

export default SocialFeed;
