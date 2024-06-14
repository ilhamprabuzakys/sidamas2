const sleep = async (duration) =>
    await new Promise((resolve) => setTimeout(resolve, duration));

/**
 * URL Params helper functions.
 */
function removeParams(name) {
    const params = new URLSearchParams(window.location.search);
    const baseURL = window.location.pathname;
    params.delete(name);
    const newUrl = baseURL + (params.toString() ? `?${params.toString()}` : "");
    window.history.pushState({ path: newUrl }, "", newUrl);
}

function getValueFromParams(type) {
    const params = new URLSearchParams(window.location.search);
    const value = params.get(type);
    if (value == "") removeParams(type);
    return value;
}

/**
 * Generic helper functions.
 */
const getRandomInt = (min, max) => {
    if (min && max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
        [min, max];
    } else {
        return Math.floor(Math.random() * min);
    }
};

const getRandomItem = (items) =>
    items[Math.floor(Math.random() * items.length)];

const calculatePercent = (value, total) => Math.round((value / total) * 100);

/**
 * Utility string manipulation helper functions.
 */

const capitalizeFirstChar = (str) =>
    `${str.charAt(0).toUpperCase()}${str.slice(1)}`;

const titleCase = (sentence) =>
    sentence.replace(/\b\w/g, (char) => char.toUpperCase());

const copyToClipboard = (content) => navigator.clipboard.writeText(content);

/**
 * BlockUI - Helper functions.
 */
function block(el) {
    el.block({
        // timeout: 1e3,
        message: `<div class="spinner-border text-success" role="status"></div>`,
        css: {
            backgroundColor: "transparent",
            border: "0",
        },
        overlayCSS: {
            backgroundColor: "#fff",
            opacity: 0.6,
        },
    });
}

const unblock = (el) => el.unblock();

const setIsLoading = (loading) =>
    loading ? block($("#__table")) : unblock($("#__table"));

/**
 * Browser built in API helper functions.
 */
const goBack = () => window.history.back();

const navigateToPage = (url) => (window.location.href = url);

const toggleFullscreen = () =>
    document.fullscreenElement
        ? document.exitFullscreen()
        : document.documentElement.requestFullscreen();

/**
 * Bootstrap built-in helper functions.
 */
const hideModal = () => $(".modal").modal("hide");
const hideAllModal = () => hideModal();

/**
 * Website Kawasan Rawan helper functions.
 */
function getStatusClass(data) {
    const statusMap = {
        BAHAYA: "danger",
        WASPADA: "warning",
        SIAGA: "primary",
        AMAN: "success",
    };

    data = data.toUpperCase();

    return statusMap[data] || "secondary";
}

/**
 * Share on social media.
 */
const url = window.location.href;

const shareOnFacebook = () =>
    window.open(
        `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(
            url
        )}`,
        "_blank"
    );
const shareOnTwitter = () =>
    window.open(
        `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}`,
        "_blank"
    );
const shareOnWhatsApp = () =>
    window.open(
        `https://api.whatsapp.com/send?text=${encodeURIComponent(url)}`,
        "_blank"
    );
const shareOnTikTok = () =>
    window.open(
        `https://www.tiktok.com/upload?reference=${encodeURIComponent(url)}`,
        "_blank"
    );
const shareOnInstagram = () =>
    window.open(
        `https://www.instagram.com/share?url=${encodeURIComponent(url)}`,
        "_blank"
    );
