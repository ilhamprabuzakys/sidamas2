/*== SETUP: VUE SFC LOADER ==*/
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

/** SET BASE COMPONENT URL **/
const base_component_url = '/static/assets/home/vue/';

// Assign to window to make it accessible from outside
window.loadVueComponent = async (path) => {
    return loadModule(base_component_url + path, options);
};

function importComponent(path) {
    return loadModule(base_component_url + path, options);
}

function loadComponent(path) {
    return Vue.defineAsyncComponent(() => loadModule(base_component_url + path, options));
}