from .util import renomear_foto
from django.db import models
from rope.settings import AUTH_USER_MODEL

# Crie seus models aqui
class Materia(models.Model):

    """
        Esse model aqui tá estranho. Apesar de estar de acordo com o modelo, acho que seria o campo "id_usuario_responsavel" 
        o usuário que criou essa matéria. Temos que dar uma analisada.
    """

    nome = models.CharField(max_length=255)
    area_de_conhecimento = models.CharField(max_length=50)

    # Datas
    usuario_responsavel = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    # Relacionamentos
    usuarios = models.ManyToManyField(AUTH_USER_MODEL)

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"

    def __str__(self):
        return self.nome


class Publicacao(models.Model):
    # Checado
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(
        max_length=166, 
        default="""
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500sLorem Ipsum i
        """)
    conteudo = models.TextField() # Ajeitar o editor aqui
    tags = models.CharField(max_length=255)
    miniatura = models.ImageField(
        upload_to=renomear_foto, 
        default='miniaturas_publicacoes/default.jpg' #Tirar o default na versão de produção
    )
    avaliacao = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        max_length=5,
        default=0.0
    )

    #Chaves estrangeiras
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    materia = models.ForeignKey("Materia", on_delete=models.CASCADE)

    #Datas
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "publicacao"
        verbose_name_plural = "publicacoes"

    def __str__(self):
        return self.titulo


class PlanoDeEstudo(models.Model):

    # administrador = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    publicacoes = models.ManyToManyField('Publicacao')

    # Datas
    criado_em = models.DateTimeField(auto_now_add=True)

    #Relacionamentos
    administrador_principal = models.ForeignKey(
        to=AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='fk_administrador'
    )
    administradores = models.ManyToManyField(
        to=AUTH_USER_MODEL, 
        related_name='admistradores'
    )
    seguidores = models.ManyToManyField(
        to=AUTH_USER_MODEL, 
        related_name='seguidores'
    )

    class Meta:
        verbose_name = "plano_de_estudo"
        verbose_name_plural = "planos_de_estudo"

    def __str__(self):
        return self.titulo


class Chamado(models.Model):
    # Checado
    
    titulo = models.CharField(max_length=255)
    is_resolvido = models.BooleanField(default=False)
    mensagem = models.TextField(max_length=255)

    # Relacionamentos
    resolvido_por = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name="resolvido_por", 
        null=True,
        blank=True,
    )
    aberto_por = models.ForeignKey(
        to=AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="aberto_por"
    )

    # Datas
    respondido_em = models.DateTimeField(auto_now=True, auto_now_add=False)
    aberto_em = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "chamado"
        verbose_name_plural = "chamados"

    def __str__(self):
        return self.titulo


class Historico(models.Model):
    # Checado

    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    # Relacionamentos
    usuario = models.ForeignKey(
        to=AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="fk_usuario"
    )
    publicacao = models.ForeignKey(
        to="Publicacao", 
        on_delete=models.CASCADE, 
        related_name="fk_publicacao"
    )
    
    # Datas
    horario = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name ="historico"
        verbose_name_plural = "historicos"

    def __str__(self):
        return self.avaliacao


class Simulado(models.Model):
    is_cronometrado = models.BooleanField(default=False)
    tempo = models.IntegerField('minutos')

    class Meta:
        verbose_name = 'simulado'
        verbose_name_plural = 'simulados'


class Questao(models.Model):
    enunciado = models.TextField()
    resumo_do_enunciado = models.CharField(max_length=255)
    opcaoa = models.TextField()
    opcaob = models.TextField()
    opcaoc = models.TextField()
    opcaod = models.TextField()
    opcaoe = models.TextField()
    alternativa_correta = models.CharField(max_length=1)

    # Relacionamentos
    simulado = models.ManyToManyField("Simulado", related_name="fk_simulado")

    class Meta:
        verbose_name='questao'
        verbose_name_plural='questoes'

    def __str__(self):
        return self.resumo_do_enunciado