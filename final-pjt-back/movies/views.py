from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, CommentSerializer,MovieListSerializer
from .models import Genre, Movie,Review, Comment, Keywords
from accounts.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import requests
import pandas as pd
# Create your views here.

def get_dbdata():
    api_key='5dcc6dd1aa73987866c715e255d2af47'

    # 장르정보 불러오기
    genre_url=f'https://api.themoviedb.org/3/genre/movie/list?language=ko&api_key={api_key}'
    res=requests.get(genre_url).json()['genres']
    for data in res:
        # if data['id']==10749:
        #     continue
        genre=GenreSerializer(data=data)
        if genre.is_valid():
            genre.save()
    
    # 영화정보 불러오기
    for page in range(1,101):
        movielist_url=f'https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page}&api_key={api_key}'
        res=requests.get(movielist_url).json()['results']
        for data in res:
            # if 10749 in data['genre_ids']:
            #     continue
            try:
                a={'id':data['id'],
                'title':data['title'],
                'overview':data['overview'],
                'popularity':data['popularity'],
                'release_date':data['release_date'],
                'vote_average':data['vote_average'],
                'poster_path':data['poster_path'],
                'genres':data['genre_ids'],}
                movie=MovieSerializer(data=a)
                if movie.is_valid():
                    movie.save()
            except:
                continue
# 리뷰 가져오기...
# def reviewpush():
#     df=pd.read_csv('C:/Users/SSAFY/Desktop/data/review.csv')
#     user=User.objects.get(username='defaultUser')
#     for movie_id, content in df.values.tolist():
#         try:
#             movie=Movie.objects.get(id=int(movie_id))
#         except:
#             continue
        
#         data={
#             'content':content
#         }
#         review=ReviewSerializer(data=data)
#         if review.is_valid():
#             review.save(user=user,movie=movie)


@api_view(['GET'])
def get_movie(request,movieId):
    movie=Movie.objects.get(id=movieId)
    if movie.like_users.filter(pk=request.user.pk).exists():
        likes=True
    else:
        likes=False
    serializer=MovieListSerializer(movie)
    
    return Response({'data':serializer.data,'likes':likes})

@api_view(['GET'])
def get_movies(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

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
    
    # 받아온 영화와 리뷰모델에 참조되어 있는 영화랑 동일한 것 뽑아오기 
    # 리뷰가 없는 초기화 상태에서 404에러 발생 -> 리뷰가 있으면 가져오고, 없으면 빈 결과 출력(오류 수정)
    try:
        reviews = get_list_or_404(Review,movie_id=movieId)
        # 데이터 전송
        serializer = ReviewSerializer(reviews,many=True)
        return Response(serializer.data)
    except:
        return Response({})


@api_view(['get'])
def get_reviews(request,movieId):
    movie=Movie.objects.get(id=movieId)
    try:
        reviews=Review.objects.filter(movie=movie)
        serializers=ReviewSerializer(reviews,many=True)
        return Response(serializers.data)
    except:
        return Response({})

@api_view(['GET'])
def get_review(request,reviewId):
    review=Review.objects.get(id=reviewId)
    if review.like_users.filter(pk=request.user.pk).exists():
        likes=True
    else:
        likes=False
    serializer=ReviewSerializer(review)
    return Response({'data':serializer.data,'likes':likes,'username':review.user.username})

# 리뷰 좋아요
@api_view(['GET'])
def reviewlikes(request, reviewId):
    review = Review.objects.get(id = reviewId)
    # 좋아요한 유저 중에 존재한다면
    if review.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 유저에서 제외
        review.like_users.remove(request.user)
        # 제외했으니까 false상태로 
        return Response(False)
    else:
        # 좋아요 유저에 추가
        review.like_users.add(request.user)
        return Response(True)

# 영화 좋아요
@api_view(['GET'])
def movielikes(request, movieId):
    # 해당 영화를 movie로 받아서
    movie = Movie.objects.get(id = movieId)
   
    # 좋아요한 유저 중에 존재한다면
    if movie.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 유저에서 제외
        movie.like_users.remove(request.user)
        # 제외했으니까 false상태로 
        return Response(False)
    else:
        # 좋아요 유저에 추가
        movie.like_users.add(request.user)
        return Response(True)

@api_view(['post'])
def gernemovies(request):
    genre_id=request.data['genre_id']
    sort_method=request.data['sort_method']
    if genre_id==9999:
        if sort_method:
            movies=Movie.objects.all().order_by('-popularity')
        else:
            movies=Movie.objects.all().order_by('-release_date')
    else:
        genre=Genre.objects.get(id=genre_id)
        if sort_method:
            movies=Movie.objects.filter(genres=genre).order_by('-popularity')
        else:
            movies=Movie.objects.filter(genres=genre).order_by('-release_date')
    serializers=MovieSerializer(movies, many=True)
    return Response(serializers.data)


# 리뷰댓글 작성하기
@api_view(['POST'])
def commentcreate(request, reviewId):
    review=get_object_or_404(Review, id=reviewId)
    serializer=CommentSerializer(data=request.data)
    if serializer.is_valid():
        # 참조키를 넣기 위해 (read_only_fields)로 참조키를 제외한 데이터만 입력받아도
        # 유효성 검사에 통과하도록 함
        # save시에 참조키를 대칭해서 넣어준 뒤 저장
        serializer.save(user=request.user, review=review)
        return Response(serializer.data)
    return Response({'error':'저장 실패'})

# 전역변수와 연결
@api_view(['GET'])
def comment(request, reviewId):
    # 해당 리뷰에 해당하는 댓글을 review로 받고
    
    # 받아온 리뷰와 댓글모델에 참조되어 있는 리뷰랑 동일한 것 뽑아오기 
    # 댓글이 없는 초기화 상태에서 404에러 발생 -> 댓글 있으면 가져오고, 없으면 빈 결과 출력(오류 수정)
    try:
        comments = get_list_or_404(Comment,review_id=reviewId)
        # 데이터 전송
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    except:
        return Response({})
    
@api_view(['GET'])
def get_comments(request, reviewId):
    try:
        review=Review.objects.get(id=reviewId)
        comments=Comment.objects.filter(review=review)
        serializers=CommentSerializer(comments,many=True)
        return Response(serializers.data)
    except:
        return Response({})
    
import re
import pandas as pd
# from pykospacing import Spacing
from konlpy.tag import Okt


from sklearn.feature_extraction.text import TfidfVectorizer

@api_view(['POST'])
def keyword(request,movieId):
    review=request.data['content']
    okt = Okt()    
    def preprocess(text):
        # 특수문자 제거
        text = re.sub('[^가-힣]', '', text)
        # 형태소 분석
        tokens = okt.nouns(text)
        # 불용어 제거
        stopwords = ['은', '는', '이', '가', '을', '를', '의', '에', '도', '와', '과', '으로', '로', '에서', '에게', '한', '하다','이고','영화','뭔가']
        tokens = [token for token in tokens if token not in stopwords and len(token)>1]
        return tokens

    word=preprocess(review)
    movie=Movie.objects.get(id=movieId)
    try:
        keywords=Keywords.objects.get(movie=movie)
        new=list(keywords.all_words.split(' '))+word
        keywords.all_words = ' '.join(new)
        keywords.save()
        return Response('추가완료')
    except:
        keywords=Keywords.objects.create(movie=movie,all_words=' '.join(word))
        keywords.save()
        return Response('완료')
    

@api_view(['get'])
def wordcloud(request,movieId):
    movie=Movie.objects.get(id=movieId)
    try:
        keywords=Keywords.objects.get(movie=movie)
        words=keywords.all_words
        from wordcloud import WordCloud
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('agg')
        # wordcloud 화하여 plt으로 그림 출력
        wc = WordCloud(width=1000, height=600, background_color="white", random_state=0, font_path=r'c:\Windows\Fonts\malgun.ttf')
        plt.imshow(wc.generate(words))
        plt.axis("off")
        # plt.show()
        plt.savefig(f'../final-pjt-front/src/assets/wordcloud.png',bbox_inches='tight')
        return Response(True)
    except:
        return Response(False)

    
