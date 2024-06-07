from django import forms


from avaliacao.models import Avaliacao

class ComissaoForm(forms.ModelForm):
    TIPOS_STATUS = (
        ('APROVADO', 'Aprovado'),
        ('EM ANÁLISE', 'Em análise'),
        ('REPROVADO', 'Reprovado' ),
        ('TRANCADO', 'Trancado'),
    )
    
    status = forms.ChoiceField(label='Status final do projeto', max_length=25, choices=TIPOS_STATUS)
    
    class Meta:
        model = Avaliacao
        fields = ['status']