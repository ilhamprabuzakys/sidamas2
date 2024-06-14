/**==========================
**** MAIN - DASHBOARD ****
=========================***/

$(() => {
    moment.locale("id");

    new PureCounter({ selector: ".purecounter" });

    expandBodyLength();

    // FIX SELECT 2 ON MODAL
    $(".modal").on("shown.bs.modal", function () {
        if (
            $(this)
                .find(".modal-dialog-scrollable .modal-body")
                .find("select.select2").length > 0
        ) {
            $(this)
                .find(".modal-dialog-scrollable .modal-body")
                .css("overflow-x", "hidden");
        }
    });

    // FIX OVERFLOW-X AXIS INSIDE SCROLLABLE DIALOG MODAL
    $(".modal").on("hidden.bs.modal", function () {
        $(this)
            .find(".modal-dialog-scrollable .modal-body")
            .css("overflow-x", "");
    });

    // FIX DATE RANGEPICKER CLOSE PARENT
    $("div.daterangepicker").click((e) => e.stopPropagation());

    document.querySelectorAll(".list-button button").forEach((button) => {
        button.addEventListener("click", function () {
            const trElement = this.closest("tr");
            trElement.classList.remove("bg-soft-light");
            trElement.classList.add("bg-soft-gray");
        });
    });

    document.addEventListener("click", function (event) {
        const trElements = document.querySelectorAll("tr.bg-soft-gray");
        trElements.forEach((trElement) => {
            if (!trElement.contains(event.target)) {
                trElement.classList.remove("bg-soft-gray");
                trElement.classList.add("bg-soft-light");
            }
        });
    });
});

function fetchSearchResults() {
    //console.log('Searching a page with query :', this.searchInput);

    const role = document
        .getElementById("global_search_input")
        .getAttribute("data-role");
    const direktorat = document
        .getElementById("global_search_input")
        .getAttribute("data-direktorat");

    let url = "";

    if (role != "superadmin") {
        url = `/static/data/pages/${role}/${direktorat}/${role}_${direktorat}.json`;
    } else {
        url = `/static/data/pages/${role}_pages.json`;
    }

    if (!this.searchInput.length > 0) {
        this.searchResults = [];
        return;
    }

    //console.log({ role, direktorat })
    axios
        .get(url)
        .then((response) => {
            this.searchResults = response.data.pages.filter((page) =>
                page.name.toLowerCase().includes(this.searchInput.toLowerCase())
            );
        })
        .catch((error) => {
            console.error("Error fetching data:", error);
        });
}

function expandBodyLength() {
    $("#layout-navbar")
        .addClass("container-fluid")
        .removeClass("container-xxl");
    $("#main-content").addClass("container-fluid").removeClass("container-xxl");
}

// ******** HANDLE FILTER ********
$("#resetFilter, #applyFilter").on("click", function () {
    $(this)
        .closest(".dropdown-menu")
        .prev(".dropdown-toggle")
        .dropdown("toggle");
});

$(function () {
    $(".list-dropdown-button button").click(function () {
        $(this)
            .closest(".dropdown-menu")
            .prev(".dropdown-toggle")
            .dropdown("toggle");
    });
});

const handleLogout = () => {
    $("#logoutModal").modal("show");
};

const handleLogoutConfirm = () => {
    $("#logoutModal").modal("hide");
};
