<script setup>

</script>
<template>
    <main class="main">
        <div class="main__containter">
            <slot></slot>
        </div>
    </main>
</template>
<style scoped lang="scss">
@import "../../scss/variables.scss";
.main {
    position: relative;
    z-index: 2;
    &__containter {
        min-height: calc(100vh - 66px);
        @extend %limiter;   
        display: flex;
    }

}


</style>
