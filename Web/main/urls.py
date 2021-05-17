from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register, name='reg'),
    path('login/', views.login, name='login'),
    path('logout', views.logout,name='logout'),
    path('users/', views.UserView.as_view(), name='UserView'),
    path('room/', views.Createroom, name='CreateRoom'),
    path('room/<str:room>/', views.room, name='room'),   
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('suport/', views.suport, name='suport'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
