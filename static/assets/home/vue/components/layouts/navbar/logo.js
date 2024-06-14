const NavbarLogo = {
    props: {
        src: {
            type: String,
            required: true
        }
    },
    template: `
        <a class="navbar-brand" href="javascript:;" @click="enterFullscreen()">
            <img
                :src="src"
                alt="Logo Website"
                style="width: 45px"
                class="me-2"
            />
            <slot></slot>
        </a>

        <button
            class="navbar-toggler d-lg-none"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapsibleNavId"
            aria-controls="collapsibleNavId"
            aria-expanded="false"
            aria-label="Toggle navigation"
        >
            <span class="navbar-toggler-icon"></span>
        </button>
    `,
    methods: {
        enterFullscreen() {
            if (document.fullscreenElement) {
                document.exitFullscreen();
            } else {
                document.documentElement.requestFullscreen();
            }
        }
    }
};

export default NavbarLogo;