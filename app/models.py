from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .manager import UsuarioManager


class Usuario(AbstractBaseUser):
    objects = UsuarioManager()

    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome