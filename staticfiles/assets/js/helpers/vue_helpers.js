// Vue helpers
if (window.Vue) {
    const options = {
        moduleCache: {
            vue: Vue,
        },
        async getFile(url) {
            const res = await fetch(url);
            if (!res.ok)
                throw Object.assign(new Error(res.statusText + " " + url), {
                    res,
                });
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
        },
    };

    const { loadModule } = window["vue3-sfc-loader"];

    // base path
    const base_component_url = "/static/assets/dashboard/vue/";

    // loaders
    window.loadVueComponent = async (path) => {
        return loadModule(base_component_url + path, options);
    };

    function loadComponent(path) {
        return Vue.defineAsyncComponent(() =>
            loadModule(base_component_url + path, options)
        );
    }
}
