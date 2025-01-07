from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Post, Comment
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'middle_name', 'last_name', 'bio', 'profile_picture', 'cover_photo']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image']

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    middle_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']



