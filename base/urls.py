from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('liked_rooms/', views.likedRooms, name="liked-rooms"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('like-post/<str:pk>', views.likeRoom, name = 'room-like'),
    path('report-room/<str:pk>', views.reportRoom, name = 'report-room'),
    
    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    path('report-management/', views.reportManagementPage, name="report-management"),
    path('censor-reported-room/<str:pk>/', views.censorReportedRoom, name="censor-reported-room"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
