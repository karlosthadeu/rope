from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import re
    
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, data_de_nascimento, password):
        user = self.model(nome=nome, email=email, data_de_nascimento=data_de_nascimento, password=password)
        user.set_password(password)
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, data_de_nascimento, password):
        user=self.create_user(nome=nome, email=email, data_de_nascimento=data_de_nascimento, password=password)
        user.is_active = True
        user.is_superuser = True
        user.permissao = 1
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class Usuario(AbstractBaseUser, PermissionsMixin):

    nome = models.CharField(_('nome'), max_length=255)
    email = models.EmailField(_('email'), max_length=255, primary_key=True)
    data_de_nascimento = models.DateField(_('data_de_nascimento'))
    atualizado_por_ultimo_em = models.DateField(_('atualizado_por_ultimo'), auto_now_add=True)
    permissao = models.IntegerField(_('permissao'), default=0)
    is_professor = models.BooleanField('is_professor', default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_de_nascimento']
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
        
    def __str__(self):
        return '%s - %s' % (self.nome, self.email)

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome
        
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    # def get(self, **extra_fields):
    #     return self.objects.get(**extra_fields)

    @property
    def is_staff(self):
        return self.nivelDeSeguranca == 2 if False else True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True