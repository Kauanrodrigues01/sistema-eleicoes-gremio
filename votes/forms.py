from django import forms

from votes.models import Vote


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['team', 'matriculation_number', 'tier']
        labels = {
            'matriculation_number': 'Número da Matrícula',
            'tier': 'Turma',
            'team': 'Chapa Desejada'
        }
        widgets = {
            'matriculation_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o número da matrícula'
            }),
            'tier': forms.Select(attrs={'class': 'form-select'}),
            'team': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_matriculation_number(self):
        matriculation_number = self.cleaned_data.get('matriculation_number').strip()
        return matriculation_number

    def clean_tier(self):
        tier = self.cleaned_data.get('tier')
        if tier not in dict(Vote.TIER_CHOICES):
            raise forms.ValidationError('Turma inválida.')
        return tier

    def clean_team(self):
        team = self.cleaned_data.get('team')
        if not team:
            raise forms.ValidationError('Selecione uma chapa.')
        return team
