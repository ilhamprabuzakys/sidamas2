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
function load(path) {
    return Vue.defineAsyncComponent(() => loadModule(base_component_url + path, options));
}
// END Setup vue-sfc-loader

const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    components: {
        "v-greeting": load("components/test/Greeting.vue"),
    },
});

app.mount("#__VUE");
