from django.urls import path, include
from sightseeing.views import signup, location, index, review
from django.contrib.auth import views as auth_view


app_name = 'sightseeing'

reviews_patterns = [
    path('', review.list, name='list'),
    path('<int:review_id>/', review.detail, name='detail'),
    path('new/', review.add_review, name='add')
]

urlpatterns = [
    path('signup/', signup.signup, name='signup'),
    path('index/', index.index, name='index'),
    path('locations/', location.LocationListView.as_view(), name='locations'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='sightseeing:login'), name='logout'),
    path('review/', include((reviews_patterns, 'review')))
]
