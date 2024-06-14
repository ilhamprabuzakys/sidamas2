$(document).ready(function () {
    gantiContainerFluid();
});

const handleLogout = () => {
    // Trigger Bootstrap 5 Modal that has id named logoutModal
    $("#logoutModal").modal("show");
};

const handleLogoutConfirm = () => {
    // Trigger Bootstrap 5 Modal that has id named logoutModal
    $("#logoutModal").modal("hide");
};

const gantiContainerFluid = () => {
    $("#layout-navbar")
        .addClass("container-fluid")
        .removeClass("container-xxl");
    $("#main-content").addClass("container-fluid").removeClass("container-xxl");
};

/* $(document).ready(function () {
    document.querySelectorAll(".layout-menu-toggle").forEach((e) => {
        e.addEventListener("click", (e) => {
            console.log("mau ngehide sidebar");
            if (
                (e.preventDefault(),
                window.Helpers.toggleCollapsed(),
                config.enableMenuLocalStorage &&
                    !window.Helpers.isSmallScreen())
            )
                try {
                    localStorage.setItem(
                        "templateCustomizer-" +
                            templateName +
                            "--LayoutCollapsed",
                        String(window.Helpers.isCollapsed())
                    );
                    var t,
                        a = document.querySelector(
                            ".template-customizer-layouts-options"
                        );
                    a &&
                        ((t = window.Helpers.isCollapsed()
                            ? "collapsed"
                            : "expanded"),
                        a.querySelector(`input[value="${t}"]`).click());
                } catch (e) {}
        });
    });
}); */
