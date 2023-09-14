<script setup>
import VHeader from '../components/htmlComponents/VHeader.vue';
import VFooter from '../components/htmlComponents/VFooter.vue';
import VMain from '../components/htmlComponents/VMain.vue';
import ResetButton from '../components/ResetButton.vue';
import SortButton from '../components/SortButton.vue';

import NoneImage from '../../public/bg.png'
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useStore } from 'vuex'
import { HTTP } from '../api'

const user = useStore().state.user
const store = useStore()
const router = useRouter()
const route = useRoute()
const movie = ref({})
const your_favorite = ref([])
const onLoading = ref(true)

onMounted( async () => {
    try{
        const response = await HTTP.get(`/movie/${route.params.id}/`)
        if (user.id != undefined){
            const response_user = await HTTP.get("/jwt/user/", {
                headers:{
                    Authorization: `Bearer ${user.token}`
                }
            })
            
            console.log(response_user.data.favorite)
            your_favorite.value = response_user.data.favorite
            console.log(your_favorite.value)
        }
        movie.value = response.data
        onLoading.value = false
    }
    catch (err){
        if (err.response.status == 401){
            store.dispatch('logout')
            router.push({path:"/login/"})
        }
        console.log(err)
    }
})

const addToFavorite = async () => {
    try{
        const response = await HTTP.post(`/to-favorite/${movie.value.id}/`,{},{
            headers:{
                Authorization: `Bearer ${user.token}`
            }
        })
        

        if (response.data[0] == false){
            your_favorite.value.push(movie.value.title)
        }
        else{
            your_favorite.value = your_favorite.value.filter(it => {
                return it != movie.value.title
            })
        }
    }
    catch(err){
        console.log(err)
    }
}

</script>
<template>
    <VHeader/>
    <VMain>
        <div v-if="!onLoading" class="detail-container">
            <h1>Movie: {{ movie.title }}</h1>
            <div class="detail__block">
                <div class="detail__image"><img v-if="movie.image" style="width: 100%;height: 100%;" :src="movie.image" /><img v-else style="width: 100%;height: 100%;" :src="NoneImage" /></div>
                <div class="detail__description-block">
                    <div>
                        <h3>Description</h3>
                        <div class="detail__description">{{ movie.description }}</div>
                    </div>                    
                    <div class="detail__raiting">
                        <h4>Raiting ({{ movie.raiting }})</h4>
                        <span v-for="item in 10" :key="item"><span v-if="item <= Math.round(movie.raiting)" style="color: gold; font-size: 24px;">★</span><span style="font-size: 24px;" v-else>☆</span></span>
                    </div>
                    <h4>Released (year): <h2>{{ movie.released }}</h2></h4>
                    <div class="detail__genres-block">
                        <h2>Genres</h2>
                        <ul class="detail__genres">
                            <li v-for="(genre, index) in movie.genres" :key="index" @click="() => {router.push({name:'Home',query:{searchGenres:[genre,]}})}" >{{ genre }}</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div v-if="user.name">
                <ResetButton @func="addToFavorite" style="margin-top: 1em;" v-if="!your_favorite.includes(movie.title)">Add to Favorite</ResetButton>
                <SortButton @func="addToFavorite" style="margin-top: 1em;" v-else>Remove from Favorite</SortButton>
            </div>
        </div>
    </VMain>
    <VFooter/>
</template>

<style scoped lang="scss">
@import "../scss/variables.scss";
*{
    font-family: $fontES;
}
.detail{
    &__image{
        width: 450px;
        height: 350px;
        overflow: hidden;
        object-fit: cover;
    }
    &__genres{
        width: 100px;
        list-style: none;
        li{
            cursor: pointer;
            text-transform: uppercase;
            transition: all ease 300ms;
        }
        li:hover{
            transform: scale(1.1,1.1);
            color: gray;
        }
    }
    &-container{
        background-color: rgba($color: #000000, $alpha: 0.6);
        padding: 80px 100px;
        h1{
            text-align: center;
        }
    }
    &__block{
        margin-top: 1em;
        display: flex;
    }
    &__description-block{
        h3{
            text-align: center;
        }
        margin-left: 2em;
        display: flex;
        flex-direction: column-reverse;
        justify-content: space-between;
    }
}


</style>