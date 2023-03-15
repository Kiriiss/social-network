from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from communities.forms import CommunityForm
from communities.models import Community

def community_detail(request, pk):
    community = get_object_or_404(Community, pk=pk)
    context = {'community': community}
    return render(request, 'communities/community_detail.html', context)

@login_required
def create_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            community = form.save(commit=False)
            community.creator = request.user
            community.save()
            return redirect('communities:community_detail', pk=community.pk)
    else:
        form = CommunityForm()
    return render(request, 'communities/create_community.html', {'form': form})



def all_communities(request):
    communities = Community.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        communities = communities.filter(name__icontains=search_query)
    context = {'communities': communities, 'search_query': search_query}
    return render(request, 'communities/communities.html', context)

