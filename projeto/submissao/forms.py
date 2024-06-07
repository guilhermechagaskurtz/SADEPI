from django import forms

from usuario.models import Usuario

from .models import Submissao

class SubmissaoForm(forms.ModelForm):

    bolsista = forms.ModelChoiceField(label='Bolsista', queryset=Usuario.bolsistas.all(), required=False)
    responsavel = forms.ModelChoiceField(label='Responsável pelo projeto (orientador) *', queryset=Usuario.professores.all())
    colaborador = forms.ModelMultipleChoiceField(label='Colaboradores (co-orientadores)', queryset=Usuario.professores.all(),
                                         required=False, help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    
    
    class Meta:
        model = Submissao
        fields = ['edital', 'programa', 'responsavel', 'colaborador', 'nome_empresa' ,'contato_empresa', 'area', 'programa_extensao', 
                  'area_tecnologica', 'titulo', 'palavras_chave','introducao', 'motivacao', 'objetivo', 'metodologia', 'plano','referencia', 'bolsista', 'nome_empresa', 'contato_empresa', 'nome_instituicao_beneficiada', 'contato_instituicao_beneficiada', 'cnpj_instituicao_beneficiada','arquivo_apendice1']

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

    def clean_programa_extensao(self):
        programa_extensao = self.cleaned_data.get('programa_extensao')
        programa = self.cleaned_data.get('programa')
        if programa.tem_instituicao_beneficiada and not programa_extensao:
            raise forms.ValidationError('Este edital exige informar um programa de extensão institucional!')
        return programa_extensao
    
    def clean_area_tecnologica(self):
        area_tecnologica = self.cleaned_data.get('area_tecnologica')
        programa = self.cleaned_data.get('programa')
        if programa.tem_empresa_parceira and not area_tecnologica:
            raise forms.ValidationError('Este edital exige informar uma área de aderência tecnológica!')
        return area_tecnologica

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