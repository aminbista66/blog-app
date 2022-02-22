from asyncio.format_helpers import _format_callback
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import (SignupForm, BlogForm, CommentForm)
from django.urls import reverse_lazy, reverse
from .models import (BlogItem, Category, Comment)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from datetime import datetime, tzinfo
from django.db.models import Count
from .algos import bubble_sort_like, get_top_post
from django.contrib.auth import get_user_model

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('logout')
    form_class = SignupForm


class HomeView(generic.ListView):
    template_name = 'base/home.html'
    context_object_name = 'blogs_item'

    def get_queryset(self):
        qs = BlogItem.objects.all()
        admin = get_user_model().objects.get(username="admin")
        # qs = qs.annotate(nviews=Count('views')).order_by('-nviews', 'likes')
        # qs = qs.order_by('-views')
        # qs = qs.annotate(nlikes=Count('likes')).order_by('-nlikes')
        object_id = qs[0].pk
        # qs = qs.exclude(pk=object_id)
        qs_list = [x for x in qs]
        for i in qs_list:
            if i.likes.count == 0:
                i.likes.add(admin)
            if i.dislikes.count() == 0:
                i.dislikes.add(admin)
        r_qs = bubble_sort_like(qs_list)
        return r_qs

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        qs = BlogItem.objects.all()
        # qs = qs.annotate(nviews=Count('views')).order_by('-nviews', 'likes')
        # qs = qs.order_by('-views')
        # qs = qs.annotate(nlikes=Count('likes')).order_by('-nlikes')
        # r_qs = bubble_sort_like(qs)
        qs_list = [x for x in qs]
        r_qs = get_top_post(qs_list)
        context.update({
            "blog_of_the_day": r_qs
        })
        return context


class PostDetailView(generic.DetailView):
    template_name = 'base/blog_detail.html'
    context_object_name = 'blog'

    def get_queryset(self):
        qs = BlogItem.objects.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            Liked = False
            DisLiked = False
            Commented = False
            blog = self.get_object()
            user_id = self.request.user.id
            comments = Comment.objects.filter(post=blog)


            if blog.likes.filter(id=user_id).exists():
                Liked = True
                DisLiked = False
            if blog.dislikes.filter(id=user_id).exists():
                DisLiked = True
                Liked = False
            if comments.filter(user__id=user_id).exists():
                Commented = True
            if not blog.views.filter(id=user_id).exists():
                blog.views.add(self.request.user)


            context.update({
                "Liked": Liked,
                "DisLiked": DisLiked,
                'Commented': Commented,
                'comments': comments,
            })
        else:
            context.update({
                'comments':Comment.objects.filter(post=self.get_object())
            })
        return context


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'base/blog_create.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.author = self.request.user
        blog.save()
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'base/blog_update.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog:home')

    def get_queryset(self):
        user = self.request.user
        qs = BlogItem.objects.filter(author=user)
        return qs


@login_required
def PostDeleteView(request, pk):
    user = request.user
    qs = BlogItem.objects.filter(author=user)
    qs = qs.filter(id=pk)
    qs = qs.first()
    if qs.author == user:
        qs.delete()
    return HttpResponseRedirect(reverse('blog:home'))


class CategoryList(LoginRequiredMixin, generic.ListView):
    template_name = "base/category_list.html"
    context_object_name = 'categories'

    def get_queryset(self):
        qs = Category.objects.all()
        return qs


class CategoryDetail(LoginRequiredMixin, generic.DeleteView):
    template_name = 'base/category_detail.html'
    context_object_name = 'category'

    def get_queryset(self):
        qs = Category.objects.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        user = self.request.user
        category = self.get_object()
        qs = BlogItem.objects.all()
        qs = qs.filter(category=category)
        context.update({
            'blogs': qs
        })
        return context

@login_required
def LikeBlog(request, pk):
    blog = get_object_or_404(BlogItem, id=request.POST.get("blog_id"))
    blog.likes.add(request.user)
    if blog.dislikes.filter(id=request.user.id).exists():
        blog.dislikes.remove(request.user)
    return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'pk': pk}))

@login_required
def DisLikeBlog(request, pk):
    blog = get_object_or_404(BlogItem, id=request.POST.get("blog_id"))
    blog.dislikes.add(request.user)
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
    return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'pk': pk}))

@login_required
def AddComment(request, pk):
    post = BlogItem.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'pk':pk}))
    context = {
        'form': form
        }
    return render(request, 'base/comment_add.html', context)

class UpdateComment(LoginRequiredMixin, generic.UpdateView):
    template_name = 'base/comment_update.html'
    form_class = CommentForm
    
    def get_queryset(self):
        qs = Comment.objects.all()
        return qs

    def get_success_url(self):
        comment = self.get_object()
        return reverse('blog:blog-detail', kwargs={'pk':comment.post.id})

@login_required
def DeleteComment(request, pk):
    comment = Comment.objects.filter(user=request.user).filter(id=pk)
    post_id = comment.first().post.id
    comment.delete()
    return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'pk':post_id}))

@login_required
def RemoveLike(request, pk):
    blog = BlogItem.objects.filter(id=pk).first()
    blog.likes.remove(request.user)
    return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'pk': blog.id}))

@login_required
def RemoveDisLike(request, pk):
    blog = BlogItem.objects.filter(id=pk).first()
    blog.dislikes.remove(request.user)
    print(blog)
    return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'pk': blog.id}))