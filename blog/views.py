
from django.views.generic import ListView, DetailView
#blog for creatingViews forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# individual blogs
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

#blog forms for creating Views
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

# blog form for updating views
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

# blog for deleting 
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    