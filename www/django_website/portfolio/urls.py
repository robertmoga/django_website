from django.urls import path
from portfolio.views import HomePageView, PostListView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='portfolio-home'),
    path('works/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail')
]