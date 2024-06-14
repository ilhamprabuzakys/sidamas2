<template>
    <button :type="type" class="btn btn-auth my-3 d-block w-100">
        <i v-if="icon" :class="icon + ' me-2'"></i>
        <slot></slot>
    </button>
</template>
<script>
export default {
    name: 'Button',
    props: {
        type: { type: String, default: 'button' },
        icon: { type: String, default: 'fa-solid fa-arrow-right-to-bracket' },
    },
};
</script>

