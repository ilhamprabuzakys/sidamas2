// Loading helper
function modifyBodyClass() {
    document.body.classList.remove('pace-done');
    document.body.classList.add('pace-running');
}

function modifyPaceDiv() {
    var paceDiv = document.querySelector('div.pace');
    if (paceDiv) {
        paceDiv.classList.remove('pace-inactive');
        paceDiv.classList.add('pace-active');
        paceDiv.style.backgroundColor = 'rgba(255, 255, 255, 0.75)';
    }
}

function validateEl() {
    return targetElement.getAttribute('href') !== '#' && targetElement.getAttribute('href') !== 'javascript:;' && targetElement.getAttribute('href') !== 'javascript:void(0);' && targetElement.getAttribute('target') !== '_blank';
}

function modifyPageOnReload() {
    modifyBodyClass();
    modifyPaceDiv();
}

document.addEventListener('click', function (event) {
    var targetElement = event.target;

    if (targetElement.tagName === 'A' &&
        (targetElement.getAttribute('href') !== '#' && targetElement.getAttribute('href') !== 'javascript:;') && targetElement.getAttribute('href') !== 'javascript:void(0);' && targetElement.getAttribute('target') !== '_blank') {

        modifyBodyClass();
        modifyPaceDiv();
    }
});

document.addEventListener('keydown', function (event) {
    if ((event.key === 'Enter' || event.key === ' ') && document.activeElement.tagName === 'A' &&
        (document.activeElement.getAttribute('href') !== '#' && document.activeElement.getAttribute('href') !== 'javascript:;')) {

        modifyBodyClass();
        modifyPaceDiv();
    }
});

window.addEventListener('beforeunload', function () {
    modifyPageOnReload();
});

// Utility 
function handleLogoutConfirmation() {
    let urlLogout = "/accounts/logout";

    Swal.fire({
        title: "Apakah anda yakin?",
        text: "Kamu akan keluar dari aplikasi?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3f858a",
        //cancelButtonColor: '#d33',
        cancelButtonText: "Batalkan",
        confirmButtonText: "Ya, saya mau keluar!",
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = urlLogout;
        }
    });
}


function toggleFullscreen() {
    if (document.fullscreenElement) {
      document.exitFullscreen();
    } else {
      document.documentElement.requestFullscreen();
    }
}

// Append host name to static URL
window.addEventListener('load', function(e) {
    const updateStaticUrls = function (element, attribute) {
        const baseUrl = window.location.origin;
        const elements = document.querySelectorAll(element);
  
        elements.forEach(function (el) {
          const currentUrl = el.getAttribute(attribute);
  
          // Check if the URL starts with "/static/assets/"
          if (currentUrl && currentUrl.startsWith("/static/assets/")) {
            const updatedUrl = baseUrl + currentUrl;
            el.setAttribute(attribute, updatedUrl);
          }
        });
      };
      
      
      updateStaticUrls("meta", "content");
      updateStaticUrls("link[rel='stylesheet']", "href");
      updateStaticUrls("link[rel='icon']", "href");
      updateStaticUrls("img", "src");
      updateStaticUrls("script", "src");  
});

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