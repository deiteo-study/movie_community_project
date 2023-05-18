from django.urls import path
from . import views

urlpatterns = [
    path('get_genres/',views.get_genres),
    path('get_movies/', views.get_movies),
    path('save_movies/',views.savemovies),
    path('<int:movieId>/review_create/', views.reviewcreate),
    path('<int:movieId>/review/', views.review),
    path('<int:movieId>/debate_create/', views.debatecreate),

]
