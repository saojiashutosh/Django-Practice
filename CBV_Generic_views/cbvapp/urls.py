from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('firstpage/',views.FirstpageView.as_view(), name="FirstPage")
]
