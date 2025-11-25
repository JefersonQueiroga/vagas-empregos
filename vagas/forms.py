from django import forms
from .models import Funcao, Empresa, Vaga


class FuncaoForm(forms.ModelForm):
    class Meta:
        model = Funcao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da função'
            })
        }
        labels = {
            'nome': 'Nome'
        }


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da empresa'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            })
        }
        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'telefone': 'Telefone'
        }


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['descricao_vaga', 'funcao', 'empresa', 'salario', 'qtd_vagas']
        widgets = {
            'descricao_vaga': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição detalhada da vaga...'
            }),
            'funcao': forms.Select(attrs={
                'class': 'form-control'
            }),
            'empresa': forms.Select(attrs={
                'class': 'form-control'
            }),
            'salario': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'qtd_vagas': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': '1'
            })
        }
        labels = {
            'descricao_vaga': 'Descrição da Vaga',
            'funcao': 'Função',
            'empresa': 'Empresa',
            'salario': 'Salário',
            'qtd_vagas': 'Quantidade de Vagas'
        }


class VagaFiltroForm(forms.Form):
    descricao = forms.CharField(
        required=False,
        label='Descrição',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por descrição...'
        })
    )

    funcao = forms.ModelChoiceField(
        queryset=Funcao.objects.all(),
        required=False,
        label='Função',
        empty_label='Todas as funções',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        required=False,
        label='Empresa',
        empty_label='Todas as empresas',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
