from django.urls import path, include
from django.contrib.auth import views as auth_view
from sightseeing.views import signup, location, index, review, profile


app_name = 'sightseeing'

profile_patters = [
    path('<int:profile_id>/', profile.detail, name='detail'),
    path('<int:profile_id>/update/', profile.update_info, name='update')
]

locations_patterns = [
    path('', location.list, name='list'),
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
    path('review/', include((reviews_patterns, 'review'))),
    path('profile/', include((profile_patters, 'profile')))
]
