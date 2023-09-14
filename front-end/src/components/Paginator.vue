<script setup>

    const props = defineProps(['movie'])
    defineEmits(['set_page'])
</script>
<template>
    <div class="things__pagination">
        <div @click="$emit('set_page',props.movie.page - 1)" class="pagination__arrow"><img src="../../public/arrow_left.png" alt="arrow"></div>
        <div class="pagination__btns">
            <div @click="$emit('set_page',1)" class="pagination__btn" v-if="props.movie.page != 1" ><button>1</button></div>
            <div @click="$emit('set_page',props.movie.page - 1)" class="pagination__btn active__btn" v-if="props.movie.page - 1 > 1"><button>{{ props.movie.page - 1 }}</button></div>
            <div class="pagination__btn"><button>{{ props.movie.page }}</button></div>
            <div @click="$emit('set_page',props.movie.page + 1)" class="pagination__btn active__btn" v-if="props.movie.page + 1 < props.movie.max_page"><button>{{ props.movie.page + 1 }}</button></div>
            <div @click="$emit('set_page',props.movie.max_page)" class="pagination__btn" v-if="props.movie.page != props.movie.max_page"><button>{{ props.movie.max_page }}</button></div>
        </div>
        <div @click="$emit('set_page',props.movie.page + 1)" class="pagination__arrow"><img src="../../public/arrow_right.png" alt="arrow"></div>
    </div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.pagination {
    &__arrow {
        width: 40px;
        height: 40px;
        background-color: $colorBlue;
        border-radius: 50%;
        display: flex;
        cursor: pointer;
        justify-content: center;
        align-items: center;
        img{
            width: 20px;
            height: 20px;
        }
    }
    &__btns {
        display: flex;
        align-items: center;
    }
    &__btn {
        cursor: pointer;
        margin: 0px 7.5px;
        width: 30px;
        height: 30px;
        button{
            cursor: pointer;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background-color: $colorBtns;
        }
    }
}
.active__btn{
    button{
        background-color: $colorGrey;
    }
}
</style>