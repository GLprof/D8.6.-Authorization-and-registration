from django.urls import path
from .views import PostList, PostDetail,Authen_up, create_post, post_edit, post_delete, article_create
from .views import article_edit, article_delete

urlpatterns = [path('post/', PostList.as_view()),
               path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
               path('post/creaposte/', create_post, name='create_news'),
               path('post/<int:pk>/edit/', post_edit, name='post_edit'),
               path('post/<int:pk>/delete', post_delete, name='post_delete'),
               path('article/create/', article_create, name='article_create'),
               path('article/<int:pk>/edit', article_edit, name='article_edit'),
               path('article/<int:pk>/delete', article_delete, name='article_delete'),
               path('authen/', Authen_up.as_view(), name='authen'),
               ]