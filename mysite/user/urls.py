from django.urls import path

from . import views
def test():
    print('test')
urlpatterns = [
    path('',views.index,name='index'),
    path('test',views.test,name='test'),
    path('login',views.login,name='login'),
    path('getProfile', views.getProfileData, name='getProfile'),
    path('profile',views.updateProfile,name='profile'),
]