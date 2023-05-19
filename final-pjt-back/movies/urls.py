from django.urls import path
from . import views

urlpatterns = [
    path('<int:movieId>/get_movie/', views.get_movie),
    path('get_movies/', views.get_movies),
    path('get_review/', views.get_review),
    path('get_reviews/', views.get_reviews),
    path('<int:movieId>/review_create/', views.reviewcreate),
    path('<int:movieId>/review/', views.review),
    path('<int:movieId>/debate_create/', views.debatecreate),
    path('<int:movieId>/debate/', views.debate),
    path('movie/<int:movieId>/likes/', views.movielikes),

]
