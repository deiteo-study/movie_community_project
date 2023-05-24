from django.urls import path,include
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('alluser/', views.alluser),
    path('<int:userId>/get_name/', views.get_name),

    path('<str:username>/get_user/', views.get_user),

    path('check/',views.password_check),
    path('delete/',views.delete),

    path('<int:userId>/follow/',views.follow)
]
