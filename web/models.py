from django.db import models
from users.models import CustomUser


class Resume(models.Model):
    name = models.CharField("name", max_length=32)
    description = models.CharField("description", max_length=512)
    skills = models.ManyToManyField('Skill', related_name='skills')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='Ссылка на профиль')

    def __str__(self):
        return str(self.name)


class Vacancy(models.Model):
    name = models.CharField("name", max_length=64)
    description = models.CharField("description", max_length=512)
    place = models.CharField("place", max_length=128)
    wage = models.FloatField('wage')
    skills = models.ManyToManyField('Skill')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Skill(models.Model):
    SOFT = 's'
    HARD = 'h'
    CHOICES = [
        (SOFT, 'soft'),
        (HARD, 'hard')
    ]
    type = models.CharField(max_length=1, choices=CHOICES, default=HARD)
    name = models.CharField("name", max_length=16)

    def __str__(self):
        return str(self.name)



