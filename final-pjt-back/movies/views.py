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
        genre=GenreSerializer(data=data)
        if genre.is_valid():
            genre.save()
    
    # 영화정보 불러오기
    for page in range(1,101):
        movielist_url=f'https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page}&api_key={api_key}'
        res=requests.get(movielist_url).json()['results']
        okt = Okt()
        def preprocess(text):
            text = re.sub('[^가-힣a-zA-Z0-9]', '', text)
            tokens = okt.morphs(text)
            return ' '.join(tokens)
        for data in res:
            try:
                a={'id':data['id'],
                'title':data['title'],
                'overview':data['overview'],
                'popularity':data['popularity'],
                'release_date':data['release_date'],
                'vote_average':data['vote_average'],
                'poster_path':data['poster_path'],
                'genres':data['genre_ids'],
                'movie_key':preprocess(data['title'])}
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
    serializer=MovieSerializer(movie)
    return Response({'data':serializer.data,'likes':likes})

@api_view(['GET'])
def random(request):
    import random
    movies=Movie.objects.all()
    lst=[movies[i] for i in random.sample(range(0,len(movies)-1),10)]
    serializers=MovieSerializer(lst,many=True)
    genres=[12,14,16,18,27,28,35,36,37,53,80,99,878,9648,10402,10751,10752,10770]
    random_genre=[]
    for genre in random.sample(genres,2):
        movies=Movie.objects.filter(genres=genre).order_by('-popularity')
        if len(movies)>=10:
            s=MovieSerializer(movies[0:10],many=True).data
        else:
            s=MovieSerializer(movies,many=True).data
        g=Genre.objects.get(id=genre)
        random_genre.append([g.name, s])
        
    return Response({'random':serializers.data,'genre_random1':random_genre[0],'genre_random2':random_genre[1]})

@api_view(['GET'])
def recommendmovies(request):
    user=request.user
    all=set()
    for movie in user.like_movies.all():
        if type(movie.recommend)==str and movie.recommend!='':
            all.update(movie.recommend.split(' '))

    for movie in user.like_movies.all():
        if str(movie.id) in all:
            all.remove(str(movie.id))
    
    import random
    if len(all)>10:
        all=random.sample(all,10)
    else:
        all=list(all)
    
    movies=[Movie.objects.get(id=int(i)) for i in all]
    serializers=MovieSerializer(movies,many=True)
    return Response(serializers.data)

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


# from sklearn.feature_extraction.text import TfidfVectorizer

@api_view(['POST','PUT'])
def keyword(request,movieId):
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
    if request.method=='POST':
        review=request.data['content']

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
    else:
        if request.data['new_content']==False:
            review=request.data['content']
            word=preprocess(review)
            movie=Movie.objects.get(id=movieId)
            keywords=Keywords.objects.get(movie=movie)
            cc=keywords.all_words.split(' ')
            for i in word:
                cc.remove(i)
            keywords.all_words=' '.join(cc)

            keywords.save()
            return Response('키워드 삭제완료')
        else:
            review=request.data['content']
            new_review=request.data['new_content']
            word=preprocess(review)
            new_word=preprocess(new_review)
            movie=Movie.objects.get(id=movieId)
            keywords=Keywords.objects.get(movie=movie)
            cc=keywords.all_words.split(' ')
            for i in word:
                cc.remove(i)
            cc += new_word
            keywords.all_words=' '.join(cc)
            keywords.save()
            return Response('키워드 수정완료')

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

@api_view(['post','delete'])
def reviewupdate(request,reviewId):
    review=Review.objects.get(id=reviewId)
    if request.method=='POST':
        review.content=request.data['new_content']
        review.save()
        return Response('수정완료')
    else:
        review.delete()
        return Response('삭제완료')
    
@api_view(['post','delete'])
def commentupdate(request,commentId):
    comment=Comment.objects.get(id=commentId)
    if request.method=='POST':
        comment.content=request.data['content']
        comment.save()
        return Response('수정완료')
    else:
        comment.delete()
        return Response('삭제완료')


@api_view(['POST'])
def moviesearch(request):
    okt=Okt()
    import math
    # search=okt.nouns(request.data['search_title'])
    search= list(request.data['search_title'])
    movies=Movie.objects.all()
    # 코사인 유사도 계산
    def cosine_similarity(v1, v2):
        dot_product = sum([a*b for a,b in zip(v1,v2)])
        magnitude = math.sqrt(sum([a**2 for a in v1])) * math.sqrt(sum([b**2 for b in v2]))
        if magnitude == 0:
            return 0
        else:
            return dot_product / magnitude
    lst=[]
    for movie in movies:
        # mv=okt.nouns(movie.title)
        mv=list(movie.title)
        keywords = set(search+mv)
        vectorA=[1 if keyword in search else 0 for keyword in keywords]
        vectorB=[1 if keyword in mv else 0 for keyword in keywords]
        # 코사인 유사도 출력
        if cosine_similarity(vectorA, vectorB)>0.3:
            lst.append([movie, cosine_similarity(vectorA, vectorB)])
    lst.sort(key=lambda x:-x[1])
    movies=[l[0] for l in lst]
    seri=MovieSerializer(movies,many=True)
    return Response(seri.data)

@api_view(['GET'])
def recommend(request,movieId):
    movie=Movie.objects.get(id=movieId)
    if type(movie.recommend)==str and movie.recommend!='':
        movies=[Movie.objects.get(id=int(i)) for i in movie.recommend.split(' ')]
        serializers=MovieSerializer(movies,many=True)
        return Response(serializers.data)
    else:
        return Response(False)

@api_view(['GET'])
def recommend_update(request,movieId):
    mv=Movie.objects.get(id=movieId)
    po=Keywords.objects.get(movie=mv)
    search=po.all_words.split(' ')
    all_key=Keywords.objects.all()

    import math
    # 코사인 유사도 계산
    def cosine_similarity(v1, v2):
        dot_product = sum([a*b for a,b in zip(v1,v2)])
        magnitude = math.sqrt(sum([a**2 for a in v1])) * math.sqrt(sum([b**2 for b in v2]))
        if magnitude == 0:
            return 0
        else:
            return dot_product / magnitude
    lst=[]
    for key in all_key:
        if key==po:
            continue
        kw=key.all_words.split(' ')

        keywords = set(search+kw)
        vectorA=[1 if keyword in search else 0 for keyword in keywords]
        vectorB=[1 if keyword in kw else 0 for keyword in keywords]
        # 코사인 유사도 출력
        if cosine_similarity(vectorA, vectorB)>0.3:
            lst.append([key.movie, cosine_similarity(vectorA, vectorB)])
    lst.sort(key=lambda x:-x[1])
    movies=[l[0].id for l in lst]
    mv.recommend=' '.join(map(str,movies))
    mv.save()
    return Response('추천 리스트 갱신')


# def mv_recommend():
#     import math
#     # 코사인 유사도 계산
#     def cosine_similarity(v1, v2):
#         dot_product = sum([a*b for a,b in zip(v1,v2)])
#         magnitude = math.sqrt(sum([a**2 for a in v1])) * math.sqrt(sum([b**2 for b in v2]))
#         if magnitude == 0:
#             return 0
#         else:
#             return dot_product / magnitude
        
#     movies=Movie.objects.all()
#     all_key=Keywords.objects.all()
#     for movie in movies:
#         if movie.id < 985939:
#             continue
#         print('1')
#         try:
#             key=Keywords.objects.get(movie=movie)
#         except:
#             continue
#         print('2')
#         search=key.all_words.split(' ')
#         lst=[]
#         for k in all_key:
#             if k!=key:
#                 kw=k.all_words.split(' ')

#                 keywords = set(search+kw)
#                 vectorA=[1 if keyword in search else 0 for keyword in keywords]
#                 vectorB=[1 if keyword in kw else 0 for keyword in keywords]
#                 # 코사인 유사도 출력
#                 if cosine_similarity(vectorA, vectorB)>0.3:
#                     lst.append([k.movie, cosine_similarity(vectorA, vectorB)])
#                     print('3')
                
#         lst.sort(key=lambda x:-x[1])
#         if len(lst)==0:
#             continue
#         elif len(lst)>10:
#             ids=[l[0].id for l in lst[0:10]]
#         else:
#             ids=[l[0].id for l in lst]
#         print(ids)
#         movie.recommend=' '.join(map(str,ids))
#         movie.save()
#         print('clear')

