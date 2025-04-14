from django import forms

from votes.models import Vote


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['team', 'student_name', 'tier']
        labels = {
            'student_name': 'Nome Completo',
            'tier': 'Turma',
            'team': 'Chapa Desejada'
        }
        widgets = {
            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome'
            }),
            'tier': forms.Select(attrs={'class': 'form-select'}),
            'team': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_student_name(self):
        student_name = self.cleaned_data.get('student_name')
        if len(student_name) < 8:
            raise forms.ValidationError('O nome deve ter pelo menos 8 caracteres.')
        return student_name

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
