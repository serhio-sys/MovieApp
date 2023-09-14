from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.decorators import permission_classes, api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Q
from .services import get_filtered_paginated_response,get_based_paginated_response,parse_OTT_API,adding_to_favorite_logic

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_request_user_info(request):
    serializer = UserSerializer(request.user, many=False)
    return Response(serializer.data)

#A view for creating comments to some title. Access only to lged in users.
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Comment has been created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#A view for getting a list of all genres. Access only to anybody.
class GenreView(APIView):
    model_class = Genre
    serializer_class = GenreSerializer

    def get_queryset(self):
        return self.model_class.objects.filter(~Q(name="No genres"))
    

    def get(self, request, *args, **kwargs):
        results = self.serializer_class(self.get_queryset(), many=True).data
        return Response({'genres': results}, status=status.HTTP_202_ACCEPTED) 


#A view set for creating, deletation, editing, filtering, movie. Access depends on request.
class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    per_page = 20

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve" or self.action == "filter":
            permission_classes = [AllowAny, ]
        elif self.action == "favorite_filter":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser, ]

        return [permission() for permission in permission_classes]


    def get_queryset(self):
        search_str = self.request.GET.get('string', '')
        queryset = Movie.objects.filter(title__icontains = search_str)
        return queryset
    

    def list(self, request, *args, **kwargs):
        return get_based_paginated_response(
            queryset=self.get_queryset(),
            serializer_class=self.serializer_class,
            request=request,
            per_page=self.per_page
        )
    
    @action(methods=['POST'],detail=False)
    def favorite_filter(self, request, *args, **kwargs):
        string = request.data.get('string','')
        queryset = request.user.favorite.filter(title__icontains = string)
        return get_filtered_paginated_response(
            queryset=queryset,
            request=request,
            serializer_class=self.serializer_class,
            per_page=self.per_page
        )

    def filter(self, request, *args, **kwargs):
        string = request.data.get('string', '')
        queryset = Movie.objects.filter(title__icontains = string)  
        return get_filtered_paginated_response(
            queryset=queryset,
            request=request,
            serializer_class=self.serializer_class,
            per_page=self.per_page
        )
   
#A view for parse movie list api. Access only to admin.
class ParseMoviesView(APIView):
    permission_classes = [IsAdminUser,]
    model_class = Movie
    genre_class = Genre
    serializer_class = MovieSerializer
    genre_serializer_class = GenreSerializer


    def post(self, request, *args, **kwargs):
        self.model_class.objects.all().delete()
        self.genre_class.objects.all().delete()

        parse_OTT_API(model_class=self.model_class,genre_class=self.genre_class)
        
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([IsAuthenticated,])
def add_to_favorite(request,pk=None):
    if pk == None:
        return Response({"Not valid id of movie!"},status=status.HTTP_400_BAD_REQUEST)
    
    return adding_to_favorite_logic(
        request=request,
        pk=pk
    )
