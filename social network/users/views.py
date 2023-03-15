from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import AbstrapUserCreationForm, AbstrapAuthenticationForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.models import AbstrapUser


def signup(request):
    if request.method == 'POST':
        form = AbstrapUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            photo = form.cleaned_data.get('photo')
            if photo:
                user.photo = photo
                user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('network:home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = AbstrapUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def loginn(request):
    if request.method == 'POST':
        form = AbstrapAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('network:home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = AbstrapAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('network:home')


@login_required
def user_listt(request):
    query = request.GET.get('q')
    users = AbstrapUser.objects.all()

    if query:
        users = users.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    context = {
        'users': users,
        'query': query,
    }

    return render(request, 'users/user_list.html', context)


@login_required
def profile(request, username):
    user = AbstrapUser.objects.get(username=username)
    return render(request, 'users/profile.html', {'user': user})


def user_detail(request, pk):
    user = get_object_or_404(AbstrapUser, pk=pk)
    context = {'user': user}
    return render(request, 'users/user_detail.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile user.id')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
