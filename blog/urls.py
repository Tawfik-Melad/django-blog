from django.urls import path
from .views import *
urlpatterns = [
    path('',PostListView.as_view(),name='blog_home'),
    path('about/',about_view,name='blog_about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),
    path('post-creat/',PostCreatView.as_view(),name='post_creat'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_confirm_delete'),
    path('new-post/',PostCreatView.as_view(),name='post-creat'),
    path('like-post/<int:pk>',Like_post,name='like-post'),
]
