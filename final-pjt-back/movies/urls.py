from django.urls import path
from . import views

urlpatterns = [
    path('get_movies/', views.get_movies),
    path('get_reviews/', views.get_reviews),
    path('<int:movieId>/review_create/', views.reviewcreate),
    path('<int:movieId>/review/', views.review),
    path('<int:movieId>/debate_create/', views.debatecreate),
    path('<int:movieId>/debate/', views.debate),

]
