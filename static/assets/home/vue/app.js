// Home
import CardItemBerita from "./components/home/card-item-berita.js";

// Pilih Tipe Akun
import ButtonDirektorat from "./components/pilih-akun/button-direktorat.js";

// Media Sosial
// import SocialFeed from "./components/media-sosial/social-feed.js";

// Survei
import ButtonLanjutkan from "./components/survei/button-lanjutkan.js";
import Pertanyaan from "./components/survei/pertanyaan.js";
import PilihanJenisKelamin from "./components/survei/pilihan/pilihan-jenis-kelamin.js";
import PilihanRentangUsia from "./components/survei/pilihan/pilihan-rentang-usia.js";
import PilihanPendidikan from "./components/survei/pilihan/pilihan-pendidikan.js";
import PilihanSurvei from "./components/survei/pilihan/pilihan-survei.js";
import ButtonKeluar from "./components/survei/button-keluar.js";

// Beranda Kegiatan
import Chart from "./components/beranda-kegiatan/beranda-chart.js";

// Forms
import Input from "./components/forms/input-group.js";
import Form from "./components/forms/form.js";
import Button from "./components/forms/button.js";

// Layouts
import Footer from "./components/layouts/footer.js";
import Navbar from "./components/layouts/navbar.js";
import NavbarLogo from "./components/layouts/navbar/logo.js";
import NavbarMenu from "./components/layouts/navbar/menu.js";
import NavbarMenuItem from "./components/layouts/navbar/menu-item.js";
import NavbarDropdown from "./components/layouts/navbar/dropdown.js";
import NavbarDropdownItem from "./components/layouts/navbar/dropdown-item.js";
import NavbarDropdownDivider from "./components/layouts/navbar/dropdown-divider.js";

// Utility
import Modal from "./components/utility/modal/modal.js";
import ModalHeader from "./components/utility/modal/modal-header.js";
import ModalBody from "./components/utility/modal/modal-body.js";

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

const base_component_url = '/static/assets/home/vue/';

// To make it accessible outside this file.
window.loadVueComponent = async (path) => {
    return loadModule(base_component_url + path, options);
};

// A snippet to load the component (only from this file)
function load(path) {
    return Vue.defineAsyncComponent(() => loadModule(base_component_url + path, options));
}
// END Setup vue-sfc-loader

const components = {
    // Forms
    "v-input-group": Input,
    "v-button": Button,
    "v-form": Form,

    // Layouts
    "v-layouts.navbar": load('components/layouts/Navbar.vue'),
    "v-layouts.navbar.logo": NavbarLogo,
    "v-layouts.navbar.menu": NavbarMenu,
    "v-layouts.navbar.menu-item": NavbarMenuItem,
    "v-layouts.navbar.dropdown": NavbarDropdown,
    "v-layouts.navbar.dropdown-item": NavbarDropdownItem,
    "v-layouts.navbar.dropdown-divider": NavbarDropdownDivider,
    "v-layouts.footer": load('components/layouts/Footer.vue'),
    
    // Utility
    "v-utility.modal": Modal,
    "v-utility.modal-header": ModalHeader,
    "v-utility.modal-body": ModalBody,
    
    // Home
    "v-home.card-item-berita": load('components/home/CardItemBerita.vue'),
    
    // Pilih Tipe Akun
    "v-pilih-akun.button-direktorat": ButtonDirektorat,
    
    // Media Sosial
    "v-media-sosial": load('pages/MediaSosial.vue'),
    // "v-media-sosial.social-feed": SocialFeed,
    
    // Survei
    "v-survei": load('components/survei/Survei.vue'),
    "v-survei.button-lanjutkan": ButtonLanjutkan,
    "v-survei.pertanyaan": Pertanyaan,
    "v-survei.pilihan-jenis-kelamin": PilihanJenisKelamin,
    "v-survei.pilihan-rentang-usia": PilihanRentangUsia,
    "v-survei.pilihan-pendidikan": PilihanPendidikan,
    "v-survei.pilihan-survei": PilihanSurvei,
    "v-survei.button-keluar": ButtonKeluar,

    // Beranda Kegiatan
    "v-beranda-kegiatan.chart": Chart,

    // Auth
    "v-login": load('pages/Auth/Login.vue'),
    "v-pilih-direktorat": load('pages/Auth/PilihDirektorat.vue'),

};

const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    components: components,
});

const emitter = window.mitt();

app.config.globalProperties.emitter = emitter;

app.mount("#__VUE");

window.onload = () => {};
