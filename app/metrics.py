from votes.models import Team, Vote
from django.db.models import Count


def get_graphic_team_metrics():
    teams = Team.objects.all()
    data = {team.name: team.selections.count() for team in teams}
    return data


def get_votes_metrics():
    total_votes = Vote.objects.count()

    metrics = {
        'total_votes': total_votes,
        'votes_by_tier': Vote.objects.values('tier').annotate(total=Count('id')).order_by('tier'),
        'votes_by_tier_and_team': Vote.objects.values('tier', 'team__name').annotate(total=Count('id')).order_by('tier', '-total'),
        'team_ranking': Vote.objects.values('team__name').annotate(votes=Count('id')).order_by('-votes'),
    }

    if total_votes > 0:
        metrics['participation_by_tier'] = (
            Vote.objects.values('tier')
            .annotate(count=Count('id'))
            .annotate(percentage=100.0 * Count('id') / total_votes)
            .order_by('-percentage')
        )

    return metrics
