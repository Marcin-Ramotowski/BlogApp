from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.NewsList.as_view(), name='news_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.NewsLoginView.as_view(), name='login'),
    path('logout/', views.NewsLogoutView.as_view(), name='logout'),
    path('create/', views.NewsCreate.as_view(), name='news_create'),
    path('read/<int:pk>', views.NewsDetail.as_view(), name='news_detail'),
    path('update/<int:pk>', views.NewsUpdate.as_view(), name='news_update'),
    path('delete/<int:pk>', views.NewsDelete.as_view(), name='news_delete')
]
