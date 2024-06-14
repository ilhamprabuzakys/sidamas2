function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Mengecek apakah cookie memiliki nama yang sesuai
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function getCSRFToken() {
    return getCookie('csrftoken');
}

function getHeaders() {
    return {
        "X-CSRFToken": getCSRFToken(),
        'Content-Type': 'application/json',
    };
}

// Vue
// Setup vue-sfc-loader
const options = {
    moduleCache: {
        vue: Vue,
    },
    async getFile(url) {
        const res = await fetch(url);
        if (!res.ok)
            throw Object.assign(new Error(res.statusText + " " + url), { res });
        return {
            getContentData: (asBinary) =>
                asBinary ? res.arrayBuffer() : res.text(),
        };
    },
    addStyle(textContent) {
        const style = Object.assign(document.createElement("style"), {
            textContent,
        });
        const ref = document.head.getElementsByTagName("style")[0] || null;
        document.head.insertBefore(style, ref);
    },
    log(type, ...args) {
        console.log(type, ...args);
    }
};

const { loadModule } = window["vue3-sfc-loader"];

const base_component_url = "/static/assets/dashboard/vue/";

// To make it accessible outside this file.
window.loadVueComponent = async (path) => {
    return loadModule(base_component_url + path, options);
};

// A snippet to load the component (only from this file)
function loadComponent(path) {
    return Vue.defineAsyncComponent(() => loadModule(base_component_url + path, options));
}
// END Setup vue-sfc-loader