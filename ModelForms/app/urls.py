
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.home, name='Home'),
   path('signup/',views.signup , name='Signup'),
   path('signin/',views.signin,name='Signin'),
   path('blogs/',views.blogPage,name='Blog'),
   path('logout/',views.logout,name='Logout'),
   path('details/',views.details,name="Details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)