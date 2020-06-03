from django.urls import path, include
from django.contrib.auth import views as auth_view
from sightseeing.views import signup, location, index, review


app_name = 'sightseeing'


locations_patterns = [
    path('', location.LocationListView.as_view(), name='list'),
    path('<int:location_id>/', location.detail, name='detail')
]


reviews_patterns = [
    path('', review.list, name='list'),
    path('<int:review_id>/', review.detail, name='detail'),
    path('new/', review.add_review, name='add')
]


urlpatterns = [
    path('signup/', signup.signup, name='signup'),
    path('index/', index.index, name='index'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='sightseeing:login'), name='logout'),
    path('locations/', include((locations_patterns, 'locations'))),
    path('review/', include((reviews_patterns, 'review')))
]
