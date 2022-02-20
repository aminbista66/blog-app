from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserBioUpdateForm
from base.models import User, BlogItem
from .mixins import CustomLoginAndUserCheckMixin

class SelfProfileview(CustomLoginAndUserCheckMixin, generic.TemplateView):
    template_name = 'profileapp/self_home.html'

    def get_context_data(self, **kwargs):
        stats_qs = BlogItem.objects.filter(author=self.request.user)
        context =  super().get_context_data(**kwargs)
        like_count=0
        print(stats_qs)
        for i in range(stats_qs.count()):
            post_like = stats_qs[i].likes.count()
            like_count += post_like
        context.update({
            'total_post':stats_qs.count(),
            'total_likes': like_count
        })
        return context

class UpdateBio(CustomLoginAndUserCheckMixin, generic.UpdateView):
    form_class = UserBioUpdateForm
    template_name = 'profileapp/update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profileapp:profile-main')

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == request.user.id: 
            return super().dispatch(request, *args, **kwargs)
        return reverse_lazy('profileapp:profile-main')

    def get_queryset(self):
        qs = User.objects.all()
        return qs        