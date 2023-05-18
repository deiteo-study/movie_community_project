from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, DebateSerializer
from .models import Genre, Movie,Review, Debate
from accounts.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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
    print(request.user)
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

# 리뷰작성하기
@api_view(['POST'])
def reviewcreate(request, movieId):
    user=get_object_or_404(User, username=request.user)
    movie=get_object_or_404(Movie, id=movieId)
    serializer=ReviewSerializer(data=request.data)
    if serializer.is_valid():
        # 참조키를 넣기 위해 (read_only_fields)로 참조키를 제외한 데이터만 입력받아도
        # 유효성 검사에 통과하도록 함
        # save시에 참조키를 대칭해서 넣어준 뒤 저장
        serializer.save(user=user, movie=movie)
        return Response(serializer.data)
    return Response({'error':'저장 실패'})

# 전역변수와 연결
@api_view(['GET'])
def review(request, movieId):
    # (디테일페이지의) 영화에 해당하는 영화를 movie로 받고
    movie=get_object_or_404(Movie,id=movieId)
    # 받아온 영화와 리뷰모델에 참조되어 있는 영화랑 동일하것 뽑아오기 
    reviews = get_list_or_404(Review,movie=movie)
    # 데이터 전송
    serializer = ReviewSerializer(reviews,many=True)
    return Response(serializer.data)


# 토론방에서 의견 등록하기
# DebateView의 axios와 연결
@api_view(['POST'])
def debatecreate(request, movieId):
    user=get_object_or_404(User, username=request.user)
    movie = get_object_or_404(Movie, id=movieId)
    serializer = DebateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user, movie=movie)
        return Response(serializer.data)
    return Response({'error':'저장 실패'})

