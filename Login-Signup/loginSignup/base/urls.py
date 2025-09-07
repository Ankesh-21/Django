from django.urls import path,include
from django.contrib.auth import urls
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.Home,name='home'),
    path('signup/',views.authView,name = 'signup'),
    # path('accounts/logout/',LogoutView.as_view(),name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
]