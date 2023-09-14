<script setup>
import { useRouter } from 'vue-router';
import NoneImg from '../../public/bg.png'

const router = useRouter()

const props = defineProps({
    item:{
        Type: Object
    }
})

</script>
<template>
    <div @click="() => {router.push({name:'Detail',params:{id:item.id}})}" class="things__item">
        <div class="item__img">
            <img v-if="item.image" :src="item.image" alt="item_img" class="item__img_img">
            <img v-else :src="NoneImg" alt="item_img" class="item__img_img">
        </div>
        <div class="item__title">{{ item.title }}</div>
    </div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.things {
    &__item{
        max-width: calc(25% - 20px);
        padding: 20px 10px;
        padding-top: 0px;
        cursor: pointer;
    }
}
.item{
    &__img{
        width: 100%;
        height: 300px;
        margin-bottom: 10px;
        img{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }
    &__title{
        font-size: 20px;
        font-family: $fontR;
    }
}

@media (max-width:1200px) {
    .things__item{
        max-width: calc(33% - 20px);
    }
    .item{
    &__img{
        width: 100%;
        height: 300px;
        margin-bottom: 10px;
        img{
            width: 15em;
        }
    }
}
}

@media (max-width:1000px) {
    .things__item{
        max-width: calc(50% - 20px);
    }
    .item{
    &__img{
        width: 100%;
        
    }
}
}

@media (max-width:800px) {
    .things__item{
        max-width: calc(100% - 20px);
    }
    .item{
    &__img{
        width: 90%;
        height: 300px;
        margin-bottom: 10px;
        img{
            width: 15em;
        }
    }
}
}

@media (max-width:450px) {
    .things__item{
        max-width: calc(100% - 20px);
    }
    .item{
    &__img{
        width: 90%;
        height: 300px;
        margin-bottom: 10px;
        img{
            width: 12em;
        }
    }
}
}

</style>
