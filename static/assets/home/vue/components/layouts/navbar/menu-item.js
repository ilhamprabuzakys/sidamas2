const NavbarMenuItem = {
    props: {
        href: {
            type: String,
            required: true,
        },
        blank: {
            default: false,
        }
    },
    template: `
        <li class="nav-item">
            <a :class="{'nav-link': true, 'active': isActive}" :href="href" :target="blank ? '_blank' : '_self'">
                <slot></slot>
            </a>
        </li>
    `,
     computed: {
        isActive() {
            return this.href === window.location.pathname;
        },
    },
};

export default NavbarMenuItem;