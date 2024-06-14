/* EVENT LISTENER */
document.addEventListener('DOMContentLoaded', function () {
    const currentURL = window.location.href;

    document.querySelector('.bagikan-facebook').addEventListener('click', function () {
        shareOnFacebook(currentURL);
    });

    document.querySelector('.bagikan-twitter').addEventListener('click', function () {
        shareOnTwitter(currentURL);
    });

    document.querySelector('.bagikan-whatsapp').addEventListener('click', function () {
        shareOnWhatsApp(currentURL);
    });

    document.querySelector('.bagikan-tiktok').addEventListener('click', function () {
        shareOnTikTok(currentURL);
    });

    document.querySelector('.bagikan-instagram').addEventListener('click', function () {
        shareOnInstagram(currentURL);
    });
});

/**
    LIST OF FUNCTION
*/
function shareOnFacebook(url) {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank');
}

function shareOnTwitter(url) {
    window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}`, '_blank');
}

function shareOnWhatsApp(url) {
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(url)}`, '_blank');
}

function shareOnTikTok(url) {
    window.open(`https://www.tiktok.com/upload?reference=${encodeURIComponent(url)}`, '_blank');
}

function shareOnInstagram(url) {
    window.open(`https://www.instagram.com/share?url=${encodeURIComponent(url)}`, '_blank');
}