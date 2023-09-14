<script setup>
    const props = defineProps(['value','placeholder','type','name'])
    defineEmits(['change'])
</script>
<template>
    <div class="filter__search_string">
        <input 
            :type="props.type"
            :placeholder="props.placeholder"
            :value="props.value"
            :name="props.name"
            @input="$emit('change', $event)"
        />
    </div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.filter{
    &__search_string {
        display: flex;
        align-items: center;
        background-color: $colorGrey;
        input{
            background-color: $colorGrey;
            font-family: $fontR;
            width: 100%;
            padding: 15px;
            padding-right: 0px;
            font-size: 18px;
        }
        input:focus{
            border: none;
            outline: none;
        }
        img{
            width: 60px;
            height: 60px;
        }
    }
}
</style>