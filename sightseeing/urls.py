from django.urls import path, include
from sightseeing.views import signup, location, index
from django.contrib.auth import views as auth_view


app_name = 'sightseeing'

locations_patterns = [
    path('', location.LocationListView.as_view(), name='list'),
    path('<int:location_id>/', location.detail, name='detail')
]


urlpatterns = [
    path('signup/', signup.signup, name='signup'),
    path('index/', index.index, name='index'),
    path('locations/', include((locations_patterns, 'locations'))),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='sightseeing:login'), name='logout'),
]
