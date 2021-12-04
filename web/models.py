from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils.text import slugify
from django.shortcuts import reverse
from googletrans import Translator


class User(AbstractUser):
    STUDENT = 's'
    EMPLOYER = 'e'
    CHOICES = [
        (STUDENT, 'student'),
        (EMPLOYER, 'employer')
    ]
    username = models.CharField(verbose_name="Никнейм", max_length=24, unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=20)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    email = models.EmailField(verbose_name="Электронная почта", max_length=100, unique=True)
    profile_pic = models.ImageField(verbose_name="Фотография", upload_to="users_photo", null=True, blank=True,
                                    default="/media/default_user_photo.jpg")
    description = models.CharField(max_length=256, null=True, blank=True, verbose_name='Описание профиля')
    city = models.CharField(max_length=16, verbose_name='Город проживания')
    phone_number = models.CharField(max_length=16, verbose_name='Номер телефона')
    chats = models.ManyToManyField('Chat', blank=True, null=True, related_name='chats', verbose_name='Чат')
    role = models.CharField(max_length=1, choices=CHOICES, default=STUDENT)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Student(models.Model):
    school = models.CharField(max_length=64)
    projects = models.ManyToManyField('Project', blank=True, null=True, related_name='students')
    git_profile = models.CharField(max_length=256)
    skills = models.ManyToManyField('Skill', blank=True, null=True)
    favourite_vacancies = models.ManyToManyField('Vacancy', blank=True, null=True, related_name='favourite_vacancies')
    student_slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='Ссылка на профиль')
    student_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_user')

    #def save(self, *args, **kwargs):
    #    if not self.id:
    #        self.slug = slugify(
    #            f"students/{self.username}")
    #        print(self.slug)

    class Meta:
        verbose_name = 'Программист'
        verbose_name_plural = 'Программисты'

    def get_absolute_url(self):
        return reverse('iteens:profile_view', kwargs={'slug': self.slug})


class Employer(models.Model):
    employer_slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='Ссылка на профиль')
    employer_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_user')

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'

    #def save(self, *args, **kwargs):
    #    if not self.id:
    #        self.slug = slugify(
    #            f"students/{self.username}")
    #        print(self.slug)


class Resume(models.Model):
    name = models.CharField("name", max_length=32)
    description = models.CharField("description", max_length=512)
    skills = models.ManyToManyField('Skill', related_name='skills')
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='Ссылка на профиль')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Project(models.Model):
    name = models.CharField("name", max_length=64)
    description = models.CharField("description", max_length=512)
    git_url = models.CharField("git_url", max_length=64)
    video_url = models.TextField("video_url")
    realisation_time = models.DateField("realisation_time")
    skills = models.ManyToManyField('Skill', blank=True, null=True)

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


class ProjectImage(models.Model):
    image = models.ImageField("image")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Vacancy(models.Model):
    name = models.CharField("name", max_length=64)
    description = models.CharField("description", max_length=512)
    place = models.CharField("place", max_length=128)
    wage = models.FloatField('wage')
    skills = models.ManyToManyField(Skill)
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
    type = models.CharField(max_length=1, choices=CHOICES, default=MESSAGE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type)
