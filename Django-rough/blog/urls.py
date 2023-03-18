from django.urls import path
from .views import HomePageView,PostDetailView,NewPostView,UpdatePostView,DeletePostView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post/new/',NewPostView.as_view(), name="create-post"),
    path('post/<int:pk>/update/',UpdatePostView.as_view(),name="update-post"),
    path('post/<int:pk>/delete/',DeletePostView.as_view(),name="delete-post"),
]
