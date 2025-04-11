from votes.models import Team


def get_graphic_team_metrics():
    teams = Team.objects.all()
    data = {team.name: team.selections.count() for team in teams}
    return data
