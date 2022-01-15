from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    STUDENT = 's'
    EMPLOYER = 'e'
    CHOICES = [
        (STUDENT, 'student'),
        (EMPLOYER, 'employer')
    ]
    first_name = models.CharField(verbose_name="Имя", max_length=20)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    email = models.EmailField(verbose_name="Электронная почта", max_length=100, unique=True)
    profile_pic = models.ImageField(verbose_name="Фотография", upload_to="users_photo", null=True, blank=True,
                                    default="/media/default_user_photo.jpg")
    description = models.CharField(max_length=256, null=True, blank=True, verbose_name='Описание профиля')
    city = models.CharField(max_length=16, verbose_name='Город проживания')
    phone_number = models.CharField(max_length=16, verbose_name='Номер телефона')
    role = models.CharField(max_length=1, choices=CHOICES, default=STUDENT)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)


