<script setup>
import MovieItem from './MovieItem.vue';

const props = defineProps({
    data:{
        Type: Array
    }
});
</script>
<template>
    <div class="things__list">
        <MovieItem :item="item" v-for="item in data" />
    </div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.things {
    &__list{
        display: flex;
        flex-wrap: wrap;
        margin: 0 auto;
        min-height: calc(100vh - 155px);
    }
}

@media (max-width:1000px) {
    .things {
        &__list{
            width: 80%;
        }
    }
}
@media (max-width:900px) {
    .things {
        &__list{
            width: 90%;
        }
    }
}
@media (max-width:800px) {
    .things {
        &__list{
            width: 100%;
        }
    }
}
@media (max-width:768px) {
    .things {
        &__list{
            width: 50%;
        }
    }
}
@media (max-width:450px) {
    .things {
        &__list{
            width: 90%;
        }
    }
}
</style>
