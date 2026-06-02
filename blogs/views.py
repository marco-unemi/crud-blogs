from django.urls import reverse_lazy
from django.views import generic

from .models import BlogPost


class PostListView(generic.ListView):
	model = BlogPost
	template_name = 'blogs/post_list.html'
	context_object_name = 'posts'


class PostDetailView(generic.DetailView):
	model = BlogPost
	template_name = 'blogs/post_detail.html'
	context_object_name = 'post'


class PostCreateView(generic.CreateView):
	model = BlogPost
	fields = ['title', 'content']
	template_name = 'blogs/post_form.html'


class PostUpdateView(generic.UpdateView):
	model = BlogPost
	fields = ['title', 'content']
	template_name = 'blogs/post_form.html'


class PostDeleteView(generic.DeleteView):
	model = BlogPost
	template_name = 'blogs/post_confirm_delete.html'
	success_url = reverse_lazy('blogs:post_list')
