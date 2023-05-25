from django.urls import path
from . import views

urlpatterns = [
    # 영화 한개 데이터 가져오기
    path('<int:movieId>/get_movie/', views.get_movie),

    # 랜덤영화 10개 가져오기
    path('random/',views.random),

    # 사용자가 좋아요한 영화의 유사 영화 추천
    path('recommendmovies/',views.recommendmovies),

    # 한개의 영화 모든 리뷰 가져오기
    path('<int:movieId>/get_reviews/', views.get_reviews),

    # 한개의 영화 모든 리뷰 가져오기
    path('<int:reviewId>/get_review/', views.get_review),

    # 사용자가 좋아하는 영화 체크
    path('<int:reviewId>/likes/', views.reviewlikes),

    # 한개의 영화의 리뷰 생성
    path('<int:movieId>/review_create/', views.reviewcreate),

    path('<int:reviewId>/review_update/', views.reviewupdate),

    path('<int:movieId>/keyword/', views.keyword),

    path('<int:movieId>/wordcloud/', views.wordcloud),

    # 한개의 리뷰 모든 댓글 가져오기
    path('<int:reviewId>/get_comments/', views.get_comments),
    # 키워드 기반 추천 리스트업
    path('<int:movieId>/recommend/', views.recommend),
    # 영화 리뷰추가시 추천리스트 갱신
    path('<int:movieId>/recommend_update/', views.recommend_update),
    # 리뷰의 댓글 생성
    path('<int:reviewId>/comment_create/', views.commentcreate),

    path('<int:commentId>/comment_update/', views.commentupdate),

    # 사용자가 좋아하는 영화 체크
    path('movie/<int:movieId>/likes/', views.movielikes),

    # 장르별 영화데이터 가져가기
    path('gernemovies/', views.gernemovies),

    path('moviesearch/', views.moviesearch),
]
