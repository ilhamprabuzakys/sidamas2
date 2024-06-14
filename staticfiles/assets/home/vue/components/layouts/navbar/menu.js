const NavbarMenu = {
    template: `
        <div class="collapse navbar-collapse" id="navbarMenu">
            <ul class="navbar-nav ms-auto mt-2 mt-lg-0">
                <slot></slot>
            </ul>
        </div>
    `,
};

export default NavbarMenu;