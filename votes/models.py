from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teams_photos/', null=True, blank=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    TIER_CHOICES = [
        # Desenvolvimento de Sistemas
        ('2DS', '2º Desenvolvimento de Sistemas'),
        ('3DS', '3º Desenvolvimento de Sistemas'),

        # Administração
        ('1A', '1º Administração'),
        ('2A', '2º Administração'),
        ('3A', '3º Administração'),

        # Enfermagem
        ('1E', '1º Enfermagem'),
        ('2E', '2º Enfermagem'),
        ('3E', '3º Enfermagem'),

        # Informática
        ('1I', '1º Informática'),
        ('3I', '3º Informática'),

        # Logística
        ('1L', '1º Logística'),
        ('2L', '2º Logística'),
    ]
    matriculation_number = models.CharField(max_length=255, unique=True, error_messages={'unique': 'Um voto com esta matrícula já foi registrado.'})
    tier = models.CharField(max_length=3, choices=TIER_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='selections')

    def __str__(self):
        return f"{self.matriculation_number} - {self.team.name} - {self.tier}"

    def save(self, **kwargs):
        self.matriculation_number = self.matriculation_number.strip()
        return super().save(**kwargs)
