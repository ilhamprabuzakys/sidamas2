<template>
    <footer id="footer" class="d-flex flex-wrap justify-content-between align-items-center py-3 mt-4 border-top">
        <div class="container text-center">
            <span class="text-footer">&copy; <span class="current-year">{{ currentYear }}</span> SIDAMAS | Deputi Bidang
                Pemberdayaan Masyarakat, BNN</span>
        </div>
    </footer>
</template>
<script>
export default {
    data() {
        return {
            currentYear: new Date().getFullYear()
        };
    }
};
</script>