from django.contrib import admin
from django.urls import path, include
from WebBuilder.views import *
from django.conf import settings
from django.conf.urls.static import static
from WebBuilder.views import deletestud, updatestud

urlpatterns = [
    #path('', loginpage, name=''),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),  # Changed path from '' to 'signup/'
    path('login/', loginpage, name='login'),  # Changed path from '' to 'login/'
    path('home/', home, name='home'),
    path('logout/', logoutpage, name='logout'),
    path('addstud/', addstud, name='addstud'),
    path('viewstud/', viewstud, name='viewstud'),
    path('deletestud/<int:studentid>/', deletestud, name='deletestud'),
    path('editstud/<int:studentid>/', editstud, name='editstud'),
    path('updatestud/<int:studentid>/', updatestud, name='updatestud'),
    path('records/', stud_records, name='stud_records'),
    path('S_Up/', signup_page, name='signup_page'),
    path('scroll/', scroll, name='scroll')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Corrected MEDIA_ROOT
