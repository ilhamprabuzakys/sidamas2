const NavbarDropdown = {
    props: {
        icon: { type: String, required: true },
        text: { type: String, required: true },
    },
    template: `
        <li class="nav-item dropdown-center">
            <a
                class="nav-link dropdown-toggle"
                href="javascript:;"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
            >
                <img
                    :src="icon"
                    alt=""
                    class="avatar rounded-circle mx-2"
                    style="width: 30px; height: 30px"
                />
                {{ text }}
            </a>
            <ul
                class="dropdown-menu dropdown-menu-start"
                aria-labelledby="navbarDropdown"
            >
                <slot></slot>
            </ul>
        </li>
    `,
};

export default NavbarDropdown;