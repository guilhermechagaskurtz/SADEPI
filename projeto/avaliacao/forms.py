from django import forms
from django.db import models

from usuario.models import Usuario

from .models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    avaliador_responsavel = forms.ModelChoiceField(label='Selecione um professor como avaliador responsável *', queryset=Usuario.professores.all())
    avaliador_suplente = forms.ModelChoiceField(label='Selecione um professor como avaliador suplente', queryset=Usuario.professores.all(), required=False)

    
    class Meta:
        model = Avaliacao
        fields = ['submissao', 'avaliador_responsavel', 'avaliador_suplente', 'parecer_avaliador_responsavel', 'parecer_avaliador_suplente',
        'merito_projeto_relevancia_responsavel', 'merito_projeto_justificativa_responsavel', 'merito_projeto_metodologia_responsavel', 'merito_projeto_plano_atividades_responsavel','pc_artigos_qualis_a1_cinco_autores',
        'merito_projeto_relevancia_suplente', 'merito_projeto_justificativa_suplente', 'merito_projeto_metodologia_suplente', 'merito_projeto_plano_atividades_suplente',
        'pc_artigos_qualis_a1_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_a1_mais_cinco_autores_demais',
        'pc_artigos_qualis_a2_cinco_autores','pc_artigos_qualis_a2_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_a2_mais_cinco_autores_demais',
        'pc_artigos_qualis_b1_b2_cinco_autores','pc_artigos_qualis_b1_b2_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b1_b2_mais_cinco_autores_demais',
        'pc_artigos_qualis_b3_b4_cinco_autores','pc_artigos_qualis_b3_b4_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b3_b4_mais_cinco_autores_demais',
        'pc_artigos_qualis_b5_c_cinco_autores','pc_artigos_qualis_b5_c_mais_cinco_autores_primeiro_ultimo','pc_artigos_qualis_b5_c_mais_cinco_autores_demais',
        'pc_trabalhos_anais_eventos','pc_resumos_anais_eventos','pc_licenca_direito','pc_autoria_livros','pc_autoria_livros_capitulos',
        'pc_orientador_teses_doutorado','pc_orientador_mestrado','pc_orientador_iniciacao_cientifica','pc_orientador_trabalho_final_curso', 'total_producoes',
        'bolsista_media_notas']
            
    def clean_avaliador_suplente(self):
        avaliador_responsavel = self.cleaned_data.get('avaliador_responsavel')
        avaliador_suplente = self.cleaned_data.get('avaliador_suplente')
        submissao = self.cleaned_data.get('submissao')

        if avaliador_responsavel:
            if (avaliador_suplente == avaliador_responsavel):
                raise forms.ValidationError('Um professor não pode ser ao mesmo tempo avaliador responsável e avaliador suplente')

            if (avaliador_suplente == submissao.responsavel or avaliador_suplente in submissao.colaborador.all()):
                raise forms.ValidationError('Um professor não pode ser ao mesmo tempo avaliador e integrante de um projeto')

        return avaliador_suplente

    def clean_avaliador_responsavel(self):
        avaliador_responsavel = self.cleaned_data.get('avaliador_responsavel')        
        submissao = self.cleaned_data.get('submissao')
        
        if (avaliador_responsavel == submissao.responsavel or avaliador_responsavel in submissao.colaborador.all()):
            raise forms.ValidationError('Um professor não pode ser ao mesmo tempo avaliador e integrante de um projeto')

        return avaliador_responsavel
