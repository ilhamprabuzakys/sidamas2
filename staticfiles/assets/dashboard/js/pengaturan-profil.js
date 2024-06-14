window.addEventListener("load", () => {
    let e = document.getElementById("uploadedAvatar");
    const defaultUserImage = e.src;
    const l = document.querySelector(".account-file-input"),
        c = document.querySelector(".account-image-reset");
    if (e) {
        const r = e.src;
        l.onchange = () => {
            if (l.files[0]) {
                const allowedExtensions = ["png", "jpg", "jpeg", "webp"];
                const fileExtension = l.files[0].name
                    .split(".")
                    .pop()
                    .toLowerCase();

                if (l.files[0].size > 1 * 1024 * 1024) {
                    // alert("Ukuran file terlalu besar. Maksimal hanya 1 MB.");
                    console.error('File size too large');
                    l.value = "";
                    Swal.fire({
                        title: "Terjadi kesalahan",
                        html: `File yang anda upload <strong>terlalu besar</strong>, maksimal hanya <strong>1MB</strong>.`,
                        icon: "error",
                        confirmButtonText: "OK",
                    });
                    return;
                }

                if (!allowedExtensions.includes(fileExtension)) {
                    console.error('Insecure file type');
                    l.value = "";
                    Swal.fire({
                        title: "Terjadi kesalahan",
                        html: `File gagal diupload, hanya ekstensi <strong>PNG, JPG, JPEG</strong>, dan <strong>Webp</strong> yang diizinkan.`,
                        icon: "error",
                        confirmButtonText: "OK",
                    });
                    return;
                }

                console.log(l.files[0]);
                e.src = window.URL.createObjectURL(l.files[0]);
                document
                    .querySelector("#saveButton")
                    .classList.remove("d-none");
            }
        };

        c.onclick = () => {
            l.value = "";
            e.src = r;
        };
    }

    document
        .querySelector('#saveButton button[type="reset"]')
        .addEventListener("click", () => {
            document.querySelector("#saveButton").classList.add("d-none");

            let e = document.getElementById("uploadedAvatar");
            const l = document.querySelector(".account-file-input");

            // e.src = window.location.origin + '/static/assets/images/avatar.png';
            e.src = defaultUserImage;
            l.value = "";
        });
        
});
