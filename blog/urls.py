from django.urls import path
from .views import Bloglist, BlogDetailView, AboutPageView, SearchResultsView, Category1, Category2, Bloglist1, \
    Registration, UserDetails

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', Bloglist.as_view(), name='home'),
    path('show10/', Bloglist1.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('impo/', Category1.as_view(), name='category1'),
    path('Rus/', Category2.as_view(), name='category2'),
    path('reg/', Registration.as_view(), name='reg'),
    path('user/<str:pk>/', UserDetails.as_view(), name='user')
]
