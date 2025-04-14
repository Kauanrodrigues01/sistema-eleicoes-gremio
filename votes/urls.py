from django.urls import path
from .views import home, get_team_data, success_page, get_teams_data, dashboard

app_name = 'votes'

urlpatterns = [
    path('', home, name='home'),
    path('api/teams/<int:team_id>/', get_team_data, name='get_team_data'),
    path('api/teams/', get_teams_data, name='get_teams_data'),
    path('success/page/', success_page, name='success_page'),

    path('dashboard/', dashboard, name='dashboard')
]
