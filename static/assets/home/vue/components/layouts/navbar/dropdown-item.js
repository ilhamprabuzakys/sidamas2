const NavbarDropdownItem = {
    props: {
        href: { type: String, required: false, default: 'javascript:;' },
        icon: { type: String, required: false },
        logout: { type: String, required: false },
    },
    template: `
        <li>
            <a class="dropdown-item" :href="href" @click="handleClick">
                <i v-if="icon" :class="icon + ' align-center'" style="color: #289da5"></i>
                <slot></slot>
            </a>
        </li>
    `,
    methods: {
        checkLogout() {
            return this.logout === 'yes';
        },

        handleLogoutConfirmation() {
            let urlLogout = "/accounts/logout";

            Swal.fire({
                title: "Apakah anda yakin?",
                text: "Kamu akan keluar dari aplikasi?",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3f858a",
                //cancelButtonColor: '#d33',
                cancelButtonText: "Batalkan",
                confirmButtonText: "Ya, saya mau keluar!",
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = urlLogout;
                }
            });
        },

        handleClick() {
            if (this.checkLogout()) {
                this.handleLogoutConfirmation();
            }
        },
    },
};

export default NavbarDropdownItem;