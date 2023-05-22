from django.urls import path
from . import views

urlpatterns = [
    # 영화 한개 데이터 가져오기
    path('<int:movieId>/get_movie/', views.get_movie),

    # 모든 영화 데이터 가져오기
    path('get_movies/', views.get_movies),

    # 한개의 영화 모든 리뷰 가져오기
    path('get_review/', views.get_review),

    # 전체영화 모든 리뷰 가져오기
    path('get_reviews/', views.get_reviews),

    # 한개의 영화의 리뷰 생성
    path('<int:movieId>/review_create/', views.reviewcreate),

    # 한개의 영화 모든 리뷰 요청
    path('<int:movieId>/review/', views.review),

    # 한개의 리뷰 모든 댓글 가져오기
    path('<int:reviewId>/get_comment/', views.get_comment),

    # 전체리뷰 모든 댓글 가져오기
    path('<int:reviewId>/get_comments/', views.get_comments),
    
    # 사용자가 좋아하는 영화 체크
    path('movie/<int:movieId>/likes/', views.movielikes),

    # 장르별 영화데이터 가져가기
    path('gernemovies/', views.gernemovies),
]
