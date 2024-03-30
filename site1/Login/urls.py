from .views import IndexClass,LoginClass,ViewUser,RegisterClass
from django.urls import path

urlpatterns = [
    path('index/', IndexClass.as_view(), name="index"),
    path('login/',LoginClass.as_view(),name="login"),
    path('',RegisterClass.as_view(),name='register'),
    path('user-view/', ViewUser.as_view(), name='user_view')
]