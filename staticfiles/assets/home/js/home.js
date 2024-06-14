$(document).ready(function () {
    const referensi = "?ref=https://sidamas.bnn.go.id";
    const proxyUrl = "https://web-production-f9b8b.up.railway.app/";
    const bnnUrl = "https://bnn.go.id/berita-satker/dayamas/";

    const getBerita = () => {
        axios
            .get(proxyUrl + bnnUrl)
            .then((response) => {
                try {
                    // Mengambil data HTML dari respons
                    const htmlContent = $(response.data);

                    // Memilih artikel dari HTML
                    const articles = htmlContent
                        .find(".posts-container article")
                        .slice(0, 4);

                    console.log(articles);

                    articles.each((index, article) => {
                        // Mengambil data dari setiap artikel
                        const title = $(article).find(".title a").text();
                        const imageUrl = $(article)
                            .find(".post-featured-img img")
                            .data("nectar-img-src");
                        const link = $(article).find(".title a").attr("href");
                        const date = formatDateBerita(
                            $(article).find(".grav-wrap .text span").text()
                        );
                        const excerpt = $(article).find(".excerpt").text();
                        const author =
                            $(article)
                                .find(".grav-wrap .text a")
                                .attr("rel", "author")
                                .text() + ` - ${date}`;

                        const tagsEl = $(article).find(
                            ".meta-category a.berita"
                        );

                        console.log(tagsEl);

                        const targetElementId =
                            "#daftar-berita #berita-bnn-pusat #berita-ke-" +
                            (index + 1) +
                            " article";

                        // Menetapkan data ke elemen target
                        const imageElement = $(targetElementId + " img.thumb");

                        // Event listener untuk menangani error pada gambar
                        imageElement.on("error", function() {
                            // Ganti dengan gambar default jika terjadi error
                            imageElement.attr("src", "static/assets/images/404-image-1.png");
                        });
                    
                        imageElement.attr("src", imageUrl);
                        
                        $(targetElementId + " a.article-link").attr(
                            "href",
                            link + referensi
                        ).attr("target", "_blank");
                        $(targetElementId + " h5.card-title").text(title);
                        $(targetElementId + " p.card-author").text(author);
                        $(targetElementId + " p.card-text").text(excerpt);
                    });
                } catch (error) {
                    console.error("Error: " + error.message);
                }
            })
            .catch((error) => {
                console.error("Error GET Request: " + error.message);
            });
    };

    const formatDateBerita = (dateText) => {
        // Pisahkan tanggal, bulan, dan tahun menggunakan spasi sebagai pemisah
        var dateParts = dateText.split(" ");

        // Ambil nilai tanggal
        var day = dateParts[0];

        // Ambil singkatan bulan
        var monthAbbreviation = dateParts[1];

        // Konversi singkatan bulan ke nama bulan lengkap
        var month;
        switch (monthAbbreviation) {
            case "Jan":
                month = "Januari";
                break;
            case "Feb":
                month = "Februari";
                break;
            case "Mar":
                month = "Maret";
                break;
            case "Apr":
                month = "April";
                break;
            case "May":
                month = "Mei";
                break;
            case "Jun":
                month = "Juni";
                break;
            case "Jul":
                month = "Juli";
                break;
            case "Aug":
                month = "Agustus";
                break;
            case "Ag":
                month = "Agustus";
                break;
            case "Sep":
                month = "September";
                break;
            case "Oct":
                month = "Oktober";
                break;
            case "Okt":
                month = "Oktober";
                break;
            case "Nov":
                month = "November";
                break;
            case "Dec":
                month = "Desember";
                break;
            case "Des":
                month = "Desember";
                break;
            default:
                break;
        }

        // Ambil nilai tahun
        var year = dateParts[2];

        // Gabungkan kembali dengan format yang diinginkan
        var formattedDate = day + " " + month + " " + year;

        return formattedDate;
    };
    
    getBerita();

});
