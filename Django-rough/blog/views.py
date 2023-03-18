from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class HomePageView(ListView):
    model=Post
    template_name="home.html"
    context_object_name="all_posts"

class PostDetailView(DetailView):
    model=Post
    template_name='blog_detail.html'
    context_object_name="posts"

class NewPostView(CreateView):
    model = Post
    template_name='create_post.html'
    fields = ['title','author','body']

class UpdatePostView(UpdateView):
    model= Post
    template_name='update_post.html'
    fields=['title','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    context_object_name="vishal"
    success_url= reverse_lazy('home')
    