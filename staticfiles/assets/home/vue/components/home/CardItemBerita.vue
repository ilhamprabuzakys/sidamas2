<template>
    <article>
        <a :href="url" ref="articleLink">
            <div class="card">
                <div class="card-image">
                    <img class="thumb" :src="imageurl" alt="Article Image" @error="handleImageError" ref="articleImage" />
                </div>
                <div class="card-body">
                    <h5 class="card-title" ref="articleTitle">{{ title }}</h5>
                    <p class="card-author" ref="articleAuthor">{{ author }}</p>
                    <p class="card-text" ref="articleText" >{{ excerpt }}</p>
                    <div class="list-kategori" ref="articleListKategori">
                        <a :href="tag.link" v-for="(tag, index) in tags" :key="index" class="kategori text-decoration-none me-1" :ref="'articleKategori' + index">#{{ tag.title }}</a>
                    </div>
                </div>
            </div>
        </a>
    </article>
</template>
<script>
export default {
    name: 'Card Item Berita',
    props: ["url", "imageurl", "title", "author", "excerpt", "tags"],
    methods: {
        handleImageError(event) {
            event.target.src = "static/assets/images/404-image-1.png";
        },
    },
};
</script>