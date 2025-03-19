from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', account_views.login_view, name='login'),
    path('register/', account_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies, name='movies'),
    path('events/', views.events, name='events'),
    path('sports/', views.sports, name='sports'),
    path('mbooking/', views.movie_booking, name='mbooking'),
    path('ebooking/', views.event_booking, name='ebooking'),
    path('sbooking/', views.sports_booking, name='sbooking'),
    path('mpayments/', views.movie_payments, name='mpayments'),
    path('epayments/', views.event_payments, name='epayments'),
    path('spayments/', views.sports_payments, name='spayments'),
    path('sconf/', views.sports_confirmation, name='sconf'),
    path('test-sbooking/', views.test_sports_booking, name='test_sports_booking'),
]

