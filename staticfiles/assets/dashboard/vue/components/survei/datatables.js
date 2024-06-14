(function (e, l) {
    typeof exports == "object" && typeof module < "u"
        ? (module.exports = l(require("vue")))
        : typeof define == "function" && define.amd
        ? define(["vue"], l)
        : ((e = typeof globalThis < "u" ? globalThis : e || self),
          (e.datatables = e.datatables || {}),
          (e.datatables["net-vue3"] = l(e.Vue)));
})(this, function (e) {
    "use strict";
    const l = [
        "childRow",
        "column-sizing",
        "column-visibility",
        "destroy",
        "draw",
        "error",
        "init",
        "length",
        "order",
        "page",
        "preDraw",
        "preInit",
        "preXhr",
        "processing",
        "requestChild",
        "search",
        "stateLoadParams",
        "stateLoaded",
        "stateSaveParams",
        "xhr",
        "autoFill",
        "preAutoFill",
        "buttons-action",
        "buttons-processing",
        "column-reorder",
        "key",
        "key-blur",
        "key-focus",
        "key-refocus",
        "key-return-submit",
        "responsive-display",
        "responsive-resize",
        "rowgroup-datasrc",
        "pre-row-reorder",
        "row-reorder",
        "row-reordered",
        "dtsb-inserted",
        "deselect",
        "select",
        "select-blur",
        "selectItems",
        "selectStyle",
        "user-select",
        "stateRestore-change",
    ];
    let f;
    const y = {
            name: "Datatables.netVue",
            inheritAttrs: !1,
            use(n) {
                f = n;
            },
        },
        h = e.defineComponent({
            ...y,
            props: { ajax: null, columns: null, data: null, options: null },
            emits: l,
            setup(n, { expose: c }) {
                const s = n,
                    p = e.ref(null),
                    r = e.ref(),
                    w = e.ref([]);
                e.watch(
                    () => s.data,
                    (t) => {
                        var i, o, u, b;
                        let a =
                            (i = r.value) == null ? void 0 : i.data().toArray();
                        for (let d of t)
                            (a != null && a.includes(d)) ||
                                (o = r.value) == null ||
                                o.row.add(d);
                        if (typeof a < "u")
                            for (let d of a)
                                t.includes(d) ||
                                    (u = r.value) == null ||
                                    u.row((k, v) => v === d).remove();
                        (b = r.value) == null || b.rows().invalidate().draw(!1),
                            m(t);
                    },
                    { deep: !0 }
                ),
                    e.onMounted(() => {
                        const t = e.getCurrentInstance();
                        let a = s.options || {};
                        if (
                            (s.data && ((a.data = s.data), m(a.data)),
                            s.columns && (a.columns = s.columns),
                            s.ajax && (a.ajax = s.ajax),
                            !f)
                        )
                            throw new Error(
                                "DataTables library not set. See https://datatables.net/tn/19 for details."
                            );
                        r.value = new f(e.unref(p), a);
                        for (let i of l)
                            r.value &&
                                t &&
                                r.value.on(i, function () {
                                    var o = Array.from(arguments),
                                        u = o.shift();
                                    o.unshift({ event: u, dt: r }),
                                        o.unshift(i),
                                        t.emit.apply(t, o);
                                });
                    }),
                    e.onBeforeUnmount(() => {
                        var t;
                        (t = r.value) == null || t.destroy(!0);
                    });
                function m(t) {
                    w.value = t.value ? t.value.slice() : t.slice();
                }
                return (
                    c({ dt: r }),
                    (t, a) =>
                        a[0] ||
                        (e.setBlockTracking(-1),
                        (a[0] = e.createElementVNode(
                            "div",
                            { class: "datatable" },
                            [
                                e.createElementVNode(
                                    "table",
                                    e.mergeProps(
                                        { ref_key: "table", ref: p },
                                        t.$attrs,
                                        { style: { width: "100%" } }
                                    ),
                                    [e.renderSlot(t.$slots, "default")],
                                    16
                                ),
                            ]
                        )),
                        e.setBlockTracking(1),
                        a[0])
                );
            },
        });
    return (() => {
        const n = h;
        return (
            (n.install = (c) => {
                c.component("Datatables.netVue", n);
            }),
            n
        );
    })();
});
