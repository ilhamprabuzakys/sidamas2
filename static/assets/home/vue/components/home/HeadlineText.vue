<template>
    <div>
        <h4><slot></slot></h4>
        <span ref=currentYear></span>
        <hr>
    </div>
</template>
<script>
export default {
    name: 'Headline Text',
    data() {
        return {
            currentYear: new Date().getFullYear(),
        }
    },
    mounted() {
        this.$refs.currentYear.innerHTML = this.currentYear;
    },
    methods: {
        doSomething() {
            console.log('Invoked from parent component...');
        }
    }
};
</script>