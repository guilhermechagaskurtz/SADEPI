from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from avaliacao.models import Avaliacao
from submissao.models import Submissao
from usuario.models import Usuario

class SubmissaoForm(forms.ModelForm):
    bolsista = forms.ModelChoiceField(label='Bolsista', queryset=Usuario.bolsistas.all(), required=False, help_text='Atenção: solicite que o seu bolsista faça o cadastro no SISGEP-SADEPI')
    responsavel = forms.ModelChoiceField(label='Responsável pelo projeto (orientador) *', queryset=Usuario.professores.all())
    colaborador = forms.ModelMultipleChoiceField(label='Colaboradores (co-orientadores)', queryset=Usuario.professores.all(),
                                         required=False, help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')


    class Meta:
        model = Submissao
        fields = ['edital', 'programa', 'responsavel', 'colaborador', 'nome_empresa' ,'contato_empresa', 'area', 'programa_extensao', 'titulo', 'palavras_chave','introducao', 'motivacao', 'objetivo', 'metodologia', 'plano','referencia', 'bolsista', 'nome_empresa', 'contato_empresa', 'nome_instituicao_beneficiada', 'contato_instituicao_beneficiada', 'cnpj_instituicao_beneficiada','arquivo_apendice1']

    def clean_bolsista(self):
        bolsista = self.cleaned_data.get('bolsista')
        edital = self.cleaned_data.get('edital')
        if edital.bolsista and not bolsista:
            raise forms.ValidationError('Este edital exige selecionar um bolsista!')
        return bolsista

    def clean_nome_empresa(self):
        nome_empresa = self.cleaned_data.get('nome_empresa')
        programa = self.cleaned_data.get('programa')
        if programa.tem_empresa_parceira and not nome_empresa:
            raise forms.ValidationError('Este edital exige informar o nome da empresa parceira!')
        return nome_empresa

    def clean_contato_empresa(self):
        contato_empresa = self.cleaned_data.get('contato_empresa')
        programa = self.cleaned_data.get('programa')
        if programa.tem_empresa_parceira and not contato_empresa:
            raise forms.ValidationError('Este edital exige informar o contato da empresa parceira!')
        return contato_empresa

    def clean_nome_instituicao_beneficiada(self):
        nome_instituicao_beneficiada = self.cleaned_data.get('nome_instituicao_beneficiada')
        programa = self.cleaned_data.get('programa')
        if programa.tem_instituicao_beneficiada and not nome_instituicao_beneficiada:
            raise forms.ValidationError('Este edital exige informar o nome da instituição beneficiada!')
        return nome_instituicao_beneficiada

    def clean_contato_instituicao_beneficiada(self):
        contato_instituicao_beneficiada = self.cleaned_data.get('contato_instituicao_beneficiada')
        programa = self.cleaned_data.get('programa')
        if programa.tem_instituicao_beneficiada and not contato_instituicao_beneficiada:
            raise forms.ValidationError('Este edital exige informar o contato da instituição beneficiada!')
        return contato_instituicao_beneficiada

    def clean_cnpj_instituicao_beneficiada(self):
        cnpj_instituicao_beneficiada = self.cleaned_data.get('cnpj_instituicao_beneficiada')
        programa = self.cleaned_data.get('programa')
        if programa.tem_instituicao_beneficiada and not cnpj_instituicao_beneficiada:
            raise forms.ValidationError('Este edital exige informar o CNPJ da instituição beneficiada!')
        return cnpj_instituicao_beneficiada

    def clean_colaborador(self):
        colaborador = self.cleaned_data.get('colaborador')
        responsavel = self.cleaned_data.get('responsavel')

        if(responsavel in colaborador.all()):
            raise forms.ValidationError('Um professor não pode ser ao mesmo tempo responsável e colaborador')
        return colaborador


class MinhaAvaliacaoResponsavelForm(forms.ModelForm):
    parecer_avaliador_responsavel = forms.CharField(label='Parecer do avaliador responsável (2000 caracteres)', max_length=2000, widget=forms.widgets.Textarea(), help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    merito_projeto_relevancia_responsavel = forms.DecimalField(label='O projeto apresentado tem caráter científico-investigativo, configurando um projeto de iniciação científica ou de inovação tecnológica, trazendo temas relevantes ou inovadores?', help_text='Máximo 1,0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    merito_projeto_justificativa_responsavel = forms.DecimalField(label='A justificativa é clara e tem relevância científica?', help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    merito_projeto_metodologia_responsavel = forms.DecimalField(label='Os aspectos metodológicos do projeto envolvem os objetivos propostos?', help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    merito_projeto_plano_atividades_responsavel = forms.DecimalField(label='O plano de atividades do bolsista contempla o projeto apresentado?', help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    class Meta:
        model = Avaliacao
        fields = ['parecer_avaliador_responsavel', 'merito_projeto_relevancia_responsavel', 
              'merito_projeto_justificativa_responsavel', 'merito_projeto_metodologia_responsavel',
              'merito_projeto_plano_atividades_responsavel']


class MinhaAvaliacaoSuplenteForm(forms.ModelForm):
    parecer_avaliador_suplente = forms.CharField(label='Parecer do avaliador responsável (2000 caracteres)', max_length=2000, widget=forms.widgets.Textarea(), help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    merito_projeto_relevancia_suplente = forms.DecimalField(label='O projeto apresentado tem caráter científico-investigativo, configurando um projeto de iniciação científica ou de inovação tecnológica, trazendo temas relevantes ou inovadores?', help_text='Máximo 1,0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    merito_projeto_justificativa_suplente = forms.DecimalField(label='A justificativa é clara e tem relevância científica?', help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    merito_projeto_metodologia_suplente = forms.DecimalField(label='Os aspectos metodológicos do projeto envolvem os objetivos propostos?', help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    merito_projeto_plano_atividades_suplente = forms.DecimalField(label='O plano de atividades do bolsista contempla o projeto apresentado?', help_text='Máximo 1.0 ponto', max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    
    
    class Meta:
        model = Avaliacao
        fields = ['parecer_avaliador_suplente', 'merito_projeto_relevancia_suplente', 
              'merito_projeto_justificativa_suplente', 'merito_projeto_metodologia_suplente',
              'merito_projeto_plano_atividades_suplente']


class SubmissaoBolsistaForm(forms.ModelForm):
    bolsista = forms.ModelChoiceField(label='Bolsista para o projeto', help_text='Você está aqui porque o edital exige bolsista', queryset=Usuario.bolsistas.all())

    class Meta:
        model = Submissao
        fields = ['bolsista']
        