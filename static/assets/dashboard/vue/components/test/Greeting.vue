<template>
    <div>
        <h1>Hello {{ message }}</h1>
    </div>
</template>
<script>
export default {
    data() {
        return {
            message: 'World!'
        };
    }
};
</script>
<style scoped>
h1 {
    color: red;
}
</style>