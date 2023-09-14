<script setup>
    defineEmits(['func'])
</script>
<template>
    <div class="filter__reset_btn"><button @click="$emit('func')"><slot/></button></div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.filter {
    &__container {
        padding: 20px;
    }
    &__reset_btn {
        width: 100%;
        button{
            width: 100%;
            font-family: $fontES;
            background-color: $colorBlue;
            border: 1px $colorGrey solid;
            font-size: 24px;
            padding: 10px 0px;
            color: $colorGrey;
            transition: all 300ms;
        }
        button:hover{
            cursor: pointer;
            width: 100%;
            font-family: $fontES;
            background-color: $colorGrey;
            font-size: 24px;
            padding: 10px 0px;
            color: #fff;
        }
    }
}
</style>
