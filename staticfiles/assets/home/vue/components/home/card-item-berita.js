const CardItemBerita = {
    props: ["url", "imageurl", "title", "author", "excerpt"],
    template: `
            <article>
                <a :href="url">
                <div class="card">
                    <div class="card-image">
                        <img class="thumb" :src="imageurl" alt="Article Image" />
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">{{ title }}</h5>
                        <p class="card-author">{{ author }}</p>
                        <p class="card-text">{{ excerpt }}</p>
                        <div class="list-kategori">
                            <a href="javascript:;" class="kategori text-decoration-none">#Berita Satker</a>
                            <a href="javascript:;" class="kategori text-decoration-none">#Bidang Pemberdayaan Masyarakat</a>
                            <a href="javascript:;" class="kategori text-decoration-none">#Foto</a>
                        </div>
                    </div>
                </div>
                </a>
            </article>
    `,
};


export default CardItemBerita;