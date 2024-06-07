from django import forms
from .models import Usuario
from instituicao.models import Instituicao

class UsuarioRegisterForm(forms.ModelForm):
    TIPOS_REGISTER = (
        ('PROFESSOR', 'Professor' ),
        ('BOLSISTA', 'Bolsista')
    )
   
    tipo = forms.ChoiceField(label='Tipo *',choices=TIPOS_REGISTER, help_text='Atenção professor, selecione seu tipo corretamente!!' )
    nome = forms.CharField(label='Nome completo', help_text='* Campos obrigatórios')
    email = forms.EmailField(label= 'Email *', max_length=100)
    lattes = forms.CharField(label='Lattes *', help_text="Acesse <a href='http://lattes.cnpq.br' target='_blank'>lattes </a> para descobrir", max_length=100)
    curso_graduacao_vinculado = forms.CharField(label='Curso de graduação vinculado *', help_text='Se houver mais de um, cadastre o mais antigo ou de maior relevância!!',max_length=50)
    instituicao = forms.ModelChoiceField(label='Instituição',queryset=Instituicao.objects.all())
    cpf = forms.CharField(label='CPF *' , max_length = 14 , help_text='ATENÇÃO: Somente os NÚMEROS', required = True)
    rg = forms.CharField(label='RG *' , max_length = 14 , help_text='ATENÇÃO: Somente os NÚMEROS', required = True)
    password = forms.CharField(label= "Senha *", widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['nome','tipo','email','curso_graduacao_vinculado','cpf','rg','password','lattes','instituicao']