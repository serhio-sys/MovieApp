import axios from "axios";
import config from "./config";
import { computed, ref } from 'vue'

export const HTTP = axios.create({
    baseURL: config.MOCK,
});


export default{
    async getMovie(page){
        try{
            if(page === undefined){
                page = 1;
            }
            const response = await HTTP.get('/movie/',{
                params: {
                    page
                }
            });
            return response.data;
        }
        catch(e){
            console.log(e);
        }
    },
    async getMovieWithSearchStringAndGenres(page, searchString, genres){
        console.log(searchString)
        try{
            const response = await HTTP.post('/movie/',{page:page,string:searchString,genres:genres});
            return response.data;
        }
        catch(e){
            console.log(e);
        }
    },
    async getFavoriteMovieWithSearchStringAndGenres(page, searchString, genres, token){
        console.log(searchString)
        try{
            const response = await HTTP.post('/favorite-movie/',{page:page,string:searchString,genres:genres},{
                headers:{
                    Authorization: `Bearer ${token}`
                }
            });
            return response.data;
        }
        catch(e){
            console.log(e);
        }
    },
    async getGenre(){
        try{
            const response = await HTTP.get('/genre/');
            return response.data;
        }
        catch(e){
            console.log(e);
        }
    }

}