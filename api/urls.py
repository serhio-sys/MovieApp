from django.urls import path, re_path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('comment/', CommentViewSet.as_view({'post': 'create'}), name='comment'),
    path('movie/<pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='movie_detail'),
    path('movie/', MovieViewSet.as_view({'get': 'list', 'post': 'filter'}), name='movie'),
    path('favorite-movie/',MovieViewSet.as_view({'post':'favorite_filter'}), name='favorite-movie'),
    path('to-favorite/<pk>/',add_to_favorite,name="favorite"),
    path('genre/', GenreView.as_view(), name='genre'),
    path('parse/', ParseMoviesView.as_view(), name='parse_movies'),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('jwt/user/', get_request_user_info, name="get_user_data"),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
