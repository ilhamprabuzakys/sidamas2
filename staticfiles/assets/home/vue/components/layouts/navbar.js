const Navbar = {
    template: `
        <nav class="navbar navbar-expand-sm navbar-dark no-highlight">
            <div class="container">
                <slot></slot>    
            </div>
        </nav>
    `,
};

export default Navbar;