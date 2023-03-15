from django.urls import path
from communities.views import create_community,all_communities,community_detail

app_name = 'communities'

urlpatterns = [
    path('create_community/', create_community, name='create_community'),
    path('communities/', all_communities, name='communities'),
    path('community/<int:pk>/', community_detail, name='community_detail'),
]
