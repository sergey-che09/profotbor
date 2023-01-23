from django.contrib import admin
from django.urls import path
from candidates import views
# from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('', views.home, name="home"),
    #
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    #
    # path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    #
    # path('create-candidate/', views.createRoom, name="create-candidate"),
    # path('update-candidate/<str:pk>/', views.updateRoom, name="update-candidate"),
    # path('delete-candidate/<str:pk>/', views.deleteRoom, name="delete-candidate"),
    #
    #
    # path('update-user/', views.updateUser, name="update-user"),
    # path('activity/', views.activityPage, name="activity"),
]
