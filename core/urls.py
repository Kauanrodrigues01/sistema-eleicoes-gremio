from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('login/', views.login_get_view, name='login'),
    path('login/complete/', views.login_post_view, name='login_complete'),
    path('logout/', views.logout_view, name='logout')
]
