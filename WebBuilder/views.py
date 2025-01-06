from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, UserLoginForm, UserProfileForm, PostForm
from .models import UserProfile, Post,FriendRequest
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_posts = Post.objects.filter(user=user)
    return render(request, 'user_profile.html', {
        'profile_user': user,
        'posts': user_posts,
    })

@login_required
def profile(request):
    user_posts = Post.objects.filter(user=request.user)
    return render(request, 'Profile.html', {'user': request.user, 'posts': user_posts})

@login_required
def profile_settings(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'ProfileSettings.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'CreatePost.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                first_name=form.cleaned_data.get('first_name'),
                middle_name=form.cleaned_data.get('middle_name'),
                last_name=form.cleaned_data.get('last_name')
            )
            login(request, user)
            return redirect('profile_settings')
    else:
        form = SignupForm()
    return render(request, 'Signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'Login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    posts = Post.objects.all().prefetch_related('heart_reactions')
    return render(request, 'home.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        return redirect('home')  # Only allow the owner to edit the post

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        post.delete()
    return redirect('home')

@login_required
def toggle_heart(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.heart_reactions.all():
        post.heart_reactions.remove(request.user)
    else:
        post.heart_reactions.add(request.user)
    return redirect('home')


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'Post.html', {'post': post})
