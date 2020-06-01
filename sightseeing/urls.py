from django.urls import path
from sightseeing.views import signup, location, index
from django.contrib.auth import views as auth_view


app_name = 'sightseeing'

urlpatterns = [
    path('signup/', signup.signup, name='signup'),
    path('index/', index.index, name='index'),
    path('locations/', location.LocationListView.as_view(), name='locations'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='sightseeing:login'), name='logout'),
]
