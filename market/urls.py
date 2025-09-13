from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'market'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('buy/', views.buy_list, name='buy_list'),
     path('buy1/', views.buy1, name='buy1'),
    path('sell/', views.sell_bike, name='sell_bike'),
    path('contact/', views.contact_us, name='contact'),
    path('pay/', views.pay, name='pay'),
    path('booking-confirmation/<int:pk>/', views.booking_confirmation, name='booking_confirmation'),
    # auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='market:index'), name='logout'),
]
