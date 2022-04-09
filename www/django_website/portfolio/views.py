from django.shortcuts import render
from portfolio.models import Post, Job
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView


class HomePageView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_showcasing=True)
        context['jobs'] = Job.objects.all()
        return context


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-date_posted')
    template_name = 'portfolio/works.html'


class PostDetailView(DetailView):
    model = Post
