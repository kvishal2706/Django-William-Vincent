
*******         Articles Page             *********
add TIME_ZONE = 'America/New_York' # new in settings.py and register the app

create required models -->admin-->urls/views

*******         Authentications             *********

by default to add user in create view

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body') # new

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)


MIXINS
. To restrict view access to only logged in users, Django has a LoginRequired
mixin172 that we can use. It’s powerful and extremely concise

In the articles/views.py file, import LoginRequiredMixin at the top and then it add to our
ArticleCreateView. Make sure that the mixin is to the left of CreateView so it will be read first.
We want the CreateView to already know we intend to restrict access

**********************************************************************************************************************

from django.contrib.auth.mixins import LoginRequiredMixin # new

class ArticleDetailView(LoginRequiredMixin, ListView):  # new

**********************************************************************************************************************


We could add permissions logic to each view for this but a more elegant solution is to create a
dedicated mixin, a class with a particular feature that we want to reuse in our Django code. And
better yet, Django ships with a built-in mixin, UserPassesTestMixin173, just for this purpose!



