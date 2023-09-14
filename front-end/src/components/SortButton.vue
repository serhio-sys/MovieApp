<script setup>
    const props = defineProps(['style'])
    defineEmits(['func'])
</script>
<template>
    <div class="filter__sort_btn" :style="props.style" ><button @click="$emit('func')"><slot/></button></div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.filter {
    &__sort_btn {
        width: 100%;
        button{
            width: 100%;
            font-family: $fontES;
            background-color: $colorGrey;
            font-size: 24px;
            padding: 10px 0px;
            transition: all 300ms;
        }
        button:hover{
            cursor: pointer;
            width: 100%;
            font-family: $fontES;
            background-color: $colorBlue;
            border: 1px $colorGrey solid;
            font-size: 24px;
            padding: 10px 0px;
            color: $colorGrey;
        }
    }
}
</style>
