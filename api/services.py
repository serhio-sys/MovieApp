from django.core.paginator import Paginator
from django.db.models import QuerySet,Model
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from .models import Movie
import requests

def get_based_paginated_response(queryset:QuerySet,serializer_class:ModelSerializer,request:Request,per_page:int):
    page = int(request.GET.get('page', 1))
    pagination = Paginator(object_list=queryset, per_page=per_page)
    results = serializer_class(pagination.page(page), many=True).data

    return Response(
        {
            'results': results,
            'page': page, 
            'max_page': pagination.num_pages
        }, 
        status=status.HTTP_202_ACCEPTED
    )  

def get_filtered_paginated_response(queryset:QuerySet,request:Request,serializer_class:ModelSerializer,per_page:int) -> Response:
    queryset = queryset
    genres_data = request.data.get('genres', [])
    if type(genres_data) == str:
        genres_data = [genres_data,]
    if len(genres_data) > 0:
        for genre in genres_data:
            queryset = queryset.filter(genres = genre)

    page = int(request.data.get('page', 1))
    pagination = Paginator(object_list=queryset, per_page=per_page)
    results = serializer_class(pagination.page(page), many=True).data

    return Response(
        {
            'results': results,
            'page': page, 
            'max_page': pagination.num_pages,
            'search_string': request.data.get('string', ''),
            'filter_data': {'genres': genres_data}
        }, 
        status=status.HTTP_202_ACCEPTED
    )
    

def adding_to_favorite_logic(request:Request,pk:int) -> Response:
    user = request.user
    movie = get_object_or_404(Movie,pk=pk)
    if user.favorite.filter(pk=pk).exists():
        user.favorite.remove(movie)
        user.save()
        return Response({True},status=status.HTTP_200_OK)
    else:
        user.favorite.add(movie)
        user.save()
        return Response({False},status=status.HTTP_200_OK)

def parse_OTT_API(model_class:Model,genre_class:Model):
    url = "https://ott-details.p.rapidapi.com/advancedsearch"

        
    headers = {
        "X-RapidAPI-Key": "27d633f222msh2903c78e8ce2968p14edc8jsn684b871ab638",
        "X-RapidAPI-Host": "ott-details.p.rapidapi.com"
    }

    for i in range(1,100):
        querystring = {"start_year":"1970","end_year":"2020","min_imdb":"4","max_imdb":"10","language":"english","type":"movie","sort":"latest","page":i}

        response = requests.get(url, headers=headers, params=querystring)

        for movie in response.json()['results']:
            film = model_class.objects.create()
            for genre in movie['genre']:
                print(genre)
                p, is_created = genre_class.objects.get_or_create(
                    name = genre
                )
                film.genres.add(p)
            
            try:    
                film.image = movie['imageurl'][0]
                res = requests.get(film.image,headers=headers)
                if res.status_code == 404:
                    film.delete()
                    continue
            except Exception:
                pass 

            film.raiting = movie['imdbrating']
            film.released = movie['released']
            film.title = movie['title']
            film.description = movie['synopsis']
            film.save()
        