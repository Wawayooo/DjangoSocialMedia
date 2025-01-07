from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings/', views.profile_settings, name='profile_settings'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('profile/settings/create_post/', views.create_post, name='create_post'),
    path('profile/settings/delete_profile/', views.delete_profile, name='delete_profile'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'), 
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('toggle_heart/<int:post_id>/', views.toggle_heart, name='toggle_heart'),
    path('my_post/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


