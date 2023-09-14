<script setup>
import VHeader from '../components/htmlComponents/VHeader.vue';
import VFooter from '../components/htmlComponents/VFooter.vue';
import VMain from '../components/htmlComponents/VMain.vue';
import MovieList from '../components/MovieList.vue';
import ResetButton from '../components/ResetButton.vue';
import SortButton from '../components/SortButton.vue';
import Paginator from '../components/Paginator.vue';

import api from "../api"
import {onMounted, ref} from 'vue'
import { useRouter, useRoute } from 'vue-router'
import SearchString from '../components/searchstring.vue'

const route = useRoute();
const router = useRouter();

const genres = ref({})

const onLoad = ref(true)
const searchGenres = ref([])
const searchString = ref("");
const movie = ref({});

onMounted(async () =>{
    genres.value = await api.getGenre();
    if(route.query.searchString !== "" || route.query.searchGenres.length > 0){
        searchString.value = route.query.searchString;
        if (route.query.searchGenres != null){
            searchGenres.value = route.query.searchGenres;
        }
        movie.value = await api.getMovieWithSearchStringAndGenres(route.query.page, route.query.searchString, route.query.searchGenres);
    }
    else{
        movie.value = await api.getMovie(route.query.page);
    }
    onLoad.value = false
});

const setPage = async (page) => {
    if(page >= 1 && page <= movie.value.max_page){
        page_up();
        setDefaultImg();
        router.push({query: { page: page, searchString: searchString.value, searchGenres: searchGenres.value}});
        if(searchString.value !== ""){
            movie.value = await api.getMovieWithSearchStringAndGenres(page, searchString.value, searchGenres.value);
        }
        else{
            movie.value = await api.getMovie(page);
        }
    }
}

const addSearchGenre = (e) => {
    if (!e.target.checked){
        searchGenres.value = searchGenres.value.filter( genre => {
            return e.target.name != genre
        })
    }
    else{
        searchGenres.value.push(e.target.name)
    }
}

const setMovieWithGenreAndSearchString = async () => {
    movie.page = 1
    
    router.push({query: { page: movie.page, searchString: searchString.value, searchGenres: searchGenres.value }});
    
    const response = await api.getMovieWithSearchStringAndGenres(movie.page, searchString.value, searchGenres.value)
    movie.value = response

}

const page_up = () =>{
    window.scroll({
        top: 0,
        left: 0,
    })
}

const resetSearchSettings = async () => {
    searchString.value = ""
    searchGenres.value = []
    movie.page = 1
    router.push({query: { page: movie.page, searchGenres: searchGenres.value }});
    const response = await api.getMovieWithSearchStringAndGenres(movie.page, searchString.value, searchGenres.value)
    movie.value = response
}

const stringChanging = (e) => {
    searchString.value = e.target.value
}

const setDefaultImg = () =>{
    const allImg = document.querySelectorAll(".item__img_img")       
        for(let i = 0; i < allImg.length; i++){
            allImg[i].src = "../../public/bg.png";
        }
}
</script>
<template>
    <VHeader/>
    <VMain>
        <div v-if="!onLoad" class="things">
            <div class="things__filter">
                <SearchString
                    :value="searchString"
                    @changing="stringChanging"
                    @search="setMovieWithGenreAndSearchString"
                />
                <div class="filter__container">
                    <ResetButton @func="resetSearchSettings">Reset</ResetButton>
                    <div class="filter__genres">
                        <div class="genres__list">
                            <div class="genres__item" v-for="item in genres.genres"><span>{{ item.name }}</span><input v-if="searchGenres.includes(item.name)" checked  v-on:change="addSearchGenre" :name="item.name" type="checkbox"/><input v-else v-on:change="addSearchGenre" :name="item.name" type="checkbox"/></div>
                        </div>
                    </div>
                    <SortButton @func="setMovieWithGenreAndSearchString">Sort</SortButton>
                </div>
            </div>
            <div class="things__content">
                <MovieList :data="movie.results"/>
                <Paginator @set_page="setPage" :movie="movie" />
            </div>
        </div>
    </VMain>
    <VFooter/>
</template>

<style scoped lang="scss">
@import "../scss/variables.scss";
.things {
    width: 100%;
    position: relative;
    display: flex;
    z-index: 2;
    padding-top: 80px;
    &__filter {
        width: calc(30% - 2px);
        background-color: $colorBlue;
        border: 1px $colorBlue solid;
    }
    &__content {
        width: 100%;
        background-color: $colorBlackA;
        padding: 0px 10px;
        padding-top: 20px;
    }
    &__pagination {
        display: flex;
        justify-content: space-between;
        align-items: centers;
        margin: 10px 0px;
    }
}
.filter {
    &__container {
        padding: 20px;
    }
    &__genres {
        max-height: 500px;
        margin: 20px 0px;
        overflow-y: scroll;
        background-color: $colorGrey;
        padding: 20px;
    }
}
.genres {
    &__item {
        font-size: 20px;
        font-family: $fontR;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        border-bottom: 3px solid $colorGrey2;
        padding-bottom: 3px;
        input[type="checkbox"] {
            -webkit-appearance: none;
            appearance: none;
            margin: 0;
            width: 20px;
            height: 20px;
            background-color: $colorGrey2;
            display: grid;
            place-content: center;
            cursor: pointer;
            transition: 120ms transform ease-in-out;
        }
        input[type="checkbox"]:checked {
            background-color: $colorBlue;
        }
    }
    &__item:last-child{
        margin-bottom: 0px;
    }
}



</style>