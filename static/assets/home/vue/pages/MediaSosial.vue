<template>
    <section id="media-sosial" class="px-2">
        <SocialFeed :name="'instagram'" :embedid="'217357'"></SocialFeed>
        <SocialFeed :name="'twitter'" :embedid="'217363'"></SocialFeed>
        <SocialFeed :name="'tiktok'" :embedid="'217445'"></SocialFeed>
        <SocialFeed :name="'youtube'" :embedid="'217443'"></SocialFeed>
    </section>
</template>
<script setup>
import SocialFeed from '../components/media-sosial/SocialFeed.vue';
</script>
