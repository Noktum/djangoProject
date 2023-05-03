from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
from django.db.models import Q
from django.contrib.auth.models import User


class UserDetails(DetailView):
    template_name = 'users.html'
    model = User


class Registration(TemplateView):
    template_name = 'reg.html'


class Bloglist(ListView):
    model = Post
    paginate_by = 5
    template_name = 'home.html'


class Bloglist1(Bloglist):
    paginate_by = 10


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class SearchResultsView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        ).distinct()
        context['object_list'] = object_list
        context['query'] = query
        return context


class Category1(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Post.objects.filter(
            Q(category__name='Новости дна')).distinct()
        context['object_list'] = object_list
        context['query'] = 'Новости дна'
        return context


class Category2(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Post.objects.filter(
            Q(category__name='Новости России')).distinct()
        context['object_list'] = object_list
        context['query'] = 'Новости России'
        return context
