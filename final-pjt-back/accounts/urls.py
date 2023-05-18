from django.urls import path,include
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('user/', views.user),
    path('<int:userId>/get_name/', views.get_name)
]
