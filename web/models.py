from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.ImageField('profile_pic')
    description = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=16)
    chats = models.ManyToManyField('Chat', related_name='chats')


class Student(User):
    school = models.CharField(max_length=64)
    projects = models.ManyToManyField('Project', related_name='students')
    git_profile = models.CharField(max_length=256)
    skills = models.ManyToManyField('Skills')
    favourite_vacancies = models.ManyToManyField('Vacancy', related_name='favourite_vacancies')


class Employer(User):
    pass


class Resume(models.Model):
    name = models.CharField("name", max_length=32)
    description = models.CharField("description", max_length=512)
    skills = models.ManyToManyField('Skills', related_name='skills')
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    name = models.CharField("name", max_length=64)
    description = models.CharField("description", max_length=512)
    git_url = models.CharField("git_url", max_length=64)
    video_url = models.TextField("video_url")
    realisation_time = models.DateField("realisation_time")

    def __str__(self):
        return str(self.name)


class Skills(models.Model):
    SOFT = 's'
    HARD = 'h'
    CHOICES = [
        (SOFT, 'soft'),
        (HARD, 'hard')
    ]
    type = models.CharField(max_length=1, choices=CHOICES, default=HARD)    # это я тут хуйню написал
    name = models.CharField("name", max_length=16)

    def __str__(self):
        return str(self.name)


class ProjectImage(models.Model):
    image = models.ImageField("image")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Vacancy(models.Model):
    name = models.CharField("name", max_length=64)
    description = models.CharField("description", max_length=512)
    place = models.CharField("place", max_length=128)
    wage = models.FloatField('wage')
    skills = models.ManyToManyField(Skills)
    owner = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Chat(models.Model):
    pass


class Message(models.Model):
    text = models.TextField('text')
    img = models.ImageField('img')
    from_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='to_user')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)


class Notification(models.Model):
    FEEDBACK = 'f'
    MESSAGE = 'm'
    COMMENT = 'c'
    CHOICES = [
        (FEEDBACK, 'feedback'),
        (MESSAGE, 'message'),
        (COMMENT, 'comment')]
    text = models.TextField('text')
    type = models.CharField(max_length=1, choices=CHOICES, default=MESSAGE)  # и тут тоже
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type)
