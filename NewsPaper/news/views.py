from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


from .models import Post
from .filters import PostFilter
from .forms import PostForms

class PostList(ListView):
    model = Post
    ordering = 'post_title'
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    paginate_by = 2



    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, news=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'news'

    def get_context_data(self, news=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = None
        return context

def create_post(request):
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_type = 'NW'
            post.save()
            return HttpResponseRedirect('/post/')
    else:
        form = PostForms()
    return render(request, 'flatpages/post_create.html',
                  {'form': form}, )

def post_edit(request, pk):
    post_object = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForms(request.POST, instance=post_object)
        if form.is_valid():
            form.save()
            return redirect('/post/')
    form = PostForms
    return render(request, 'flatpages/post_edit.html', {'form': form})


def post_delete(request, pk):
    post_object = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post_object.delete()
        return redirect('/post/')
    return render(request, 'flatpages/post_delete.html', {'objekt': post_object})

def article_create(request):
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_type = 'AR'
            article.save()
            return HttpResponseRedirect('/post/')
    else:
        form = PostForms()
        return render(request, 'flatpages/article_create.html', {'form': form})

def article_edit(request, pk):
    article_object = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForms(request.POST, instance=article_object)
        if form.is_valid():
            form.save()
            return redirect('/post/')
    form = PostForms()
    return render(request, 'flatpages/article_edit.html', {'form': form})

def article_delete(request, pk):
    article_object = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        article_object.delete()
        return redirect('/post/')
    return render(request, 'flatpages/article_delete.html', {'object': article_object})



class Authen_up(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/authen.html'









