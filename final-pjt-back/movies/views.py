from django.shortcuts import render
from .serializers import GenreSerializer, MovieSerializer
from .models import Genre, Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
# Create your views here.

# 장르 정보 불러와서 저장하는 코드
@api_view(['GET'])
def get_genres(request):
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko&api_key=5dcc6dd1aa73987866c715e255d2af47"
    res=requests.get(url).json()['genres']
    for data in res:
        genre=GenreSerializer(data=data)
        if genre.is_valid():
            genre.save()
    
    genres=Genre.objects.all()
    serializer=GenreSerializer(genres, many=True)
    return Response(serializer.data)


# 영화 정보 불러와서 db에 저장하는 코드
@api_view(['GET'])
def get_movies(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def savemovies(request):
    res=request.data['results']
    for data in res:
        a={'id':data['id'],
           'title':data['title'],
           'overview':data['overview'],
           'release_date':data['release_date'],
           'vote_average':data['vote_average'],
           'poster_path':data['poster_path'],
           'genres':data['genre_ids']}
        movie=MovieSerializer(data=a)
        if movie.is_valid():
            movie.save()
    return Response({'save':'저장완료'})
