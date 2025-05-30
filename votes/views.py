import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Count, Case, When, Value, BooleanField
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from app.metrics import get_graphic_team_metrics, get_votes_metrics
from votes.forms import VoteForm
from .models import Team


@login_required
def home(request):
    """Exibe a página inicial com o formulário"""
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Voto registrado com sucesso!')
            form = VoteForm()
        else:
            messages.error(request, 'Preencha corretamente os dados.')
    else:
        form = VoteForm()

    return render(request, 'votes/pages/home.html', {'form': form})


@login_required
def success_page(request):
    return render(request, 'votes/pages/success_page.html')


@login_required
def get_team_data(request, team_id):
    """Retorna os dados da chapa para popular a imagem via AJAX."""
    try:
        teacher = Team.objects.get(id=team_id)
        photo_url = teacher.photo.url if teacher.photo else None  # Adicionada verificação para evitar erro se a foto não existir
        return JsonResponse({
            'name': teacher.name,
            'photo_url': photo_url
        })
    except Team.DoesNotExist:
        return JsonResponse({'error': 'Professor não encontrado'}, status=404)


@login_required
def get_teams_data(request):
    teams = Team.objects.annotate(
        num_selections=Count('selections'),
        is_available=Case(
            When(num_selections__gte=9, then=Value(False)),  # Indisponível se tiver 9 ou mais seleções
            default=Value(True),
            output_field=BooleanField()
        )
    ).values("id", "name", "is_available")  # Pegando apenas os campos necessários

    return JsonResponse(list(teams), safe=False)  # Convertendo a QuerySet em uma lista para serialização


@login_required
def dashboard(request):
    if not request.user.is_superuser:
        print('caiu aqui')
        messages.error(request, 'Acesso negado: você precisa ser um administrador para acessar esta página.')
        return redirect('core:login')

    # Obtém as métricas
    team_metrics = get_graphic_team_metrics()
    votes_metrics = get_votes_metrics()

    # Prepara o contexto
    context = {
        # Métricas de equipe (já serializadas para JSON)
        'team_metrics': json.dumps(team_metrics),

        # Métricas de votos (dados brutos para uso no template)
        'total_votes': votes_metrics['total_votes'],
        'votes_by_tier': votes_metrics['votes_by_tier'],
        'votes_by_tier_and_team': votes_metrics['votes_by_tier_and_team'],
        'team_ranking': votes_metrics['team_ranking'],
    }

    # Adiciona participação por turma se existir (métrica condicional)
    if 'participation_by_tier' in votes_metrics:
        context.update({
            'participation_by_tier': votes_metrics['participation_by_tier'],
        })

    return render(request, 'votes/pages/dashboard.html', context)
