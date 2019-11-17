from nucleo.util import renomear_foto
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import re

"""
    Níveis de permissão
        0 - usuário comum
        1 - professor
        2 - admnistrador
        3 - super usuário
"""
   
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, data_de_nascimento, senha):
        user = self.model(nome=nome, email=email, data_de_nascimento=data_de_nascimento, password=senha)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, data_de_nascimento, senha):
        user=self.create_user(nome=nome, email=email, data_de_nascimento=data_de_nascimento, password=senha)
        user.is_active = True
        user.nivel_de_seguranca = 3
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class Usuario(AbstractBaseUser, PermissionsMixin):

    avatar = models.ImageField(
        'avatar', 
        upload_to=renomear_foto, 
        default='avatares_usuarios/default.jpg'
    )
    nome = models.CharField(
        'nome', 
        max_length=255
    )
    email = models.EmailField(
        'email', 
        max_length=255
    )
    data_de_nascimento = models.DateField(
        'data_de_nascimento'
    )
    atualizado_por_ultimo_em = models.DateField(
        'atualizado_por_ultimo', 
        auto_now_add=True
    )
    entrou_em = models.DateField(
        'atualizado_por_ultimo', 
        auto_now_add=True
    )
    nivel_de_seguranca = models.IntegerField(
        'nivel_de_seguranca', default=0)
    is_professor = models.BooleanField(
        'is_professor', 
        default=False
    )
    is_active = models.BooleanField(
        'is_active', 
        default=True
    )
    biografia = models.TextField(
        "biografia"
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_de_nascimento']
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
        
    def __str__(self):
        return f"{self.nome} - {self.emal}"

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome
        
    @property
    def is_staff(self):
        return self.nivel_de_seguranca == 3 or self.nivel_de_seguranca == 2

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
