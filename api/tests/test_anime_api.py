from django.urls import reverse, resolve
from django.test import SimpleTestCase
from api.views import *
from api.models import *
from rest_framework.test import APITestCase


class MovieistAPIViewTests(APITestCase):
    movie_list_url = reverse('movie')
    model_class = Movie
    model_genre_class = Genre


    def setUp(self):
        self.model_genre_class.objects.create(name='genre1')
        self.model_genre_class.objects.create(name='genre2')
        self.model_genre_class.objects.create(name='genre3')

        movie1 = self.model_class.objects.create(title='title1', image='image1.jpg', description='description1')
        movie1.genres.set(({'genre1', 'genre2'}))
        movie1.save()

        movie2 = self.model_class.objects.create(title='title2', image='image2.jpg', description='description1')
        movie2.genres.set(({'genre2', 'genre1'}))
        movie2.save()

        movie3 = self.model_class.objects.create(title='title3', image='image3.jpg', description='description1')
        movie3.genres.set(({'genre3', 'genre1'}))
        movie3.save()


    def test_get_movie_list(self):
        response = self.client.get(self.movie_list_url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


class MovieDetailAPIViewTests(APITestCase):
    movie_detail_url = reverse('movie_detail', kwargs={"pk": "1"})
    model_class = Movie
    model_genre_class = Genre


    def setUp(self):
        self.model_genre_class.objects.create(name='genre1')
        self.model_genre_class.objects.create(name='genre2')

        movie1 = self.model_class.objects.create(title='title1', image='image1.jpg', description='description1')
        movie1.genres.set(({'genre1', 'genre2'}))
        movie1.save()


    def test_get_movie_detail(self):
        response = self.client.get(self.movie_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GenreListViewTests(APITestCase):
    genre_list_url = reverse('genre')
    model_class = Genre


    def setUp(self):
        self.model_class.objects.create(name="genre1")
        self.model_class.objects.create(name="genre2")
        self.model_class.objects.create(name="genre3")


    def test_get_movie_detail(self):
        response = self.client.get(self.genre_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)