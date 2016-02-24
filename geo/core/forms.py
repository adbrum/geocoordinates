from django import forms


class CoordenadaForm(forms.Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    sobrenome = forms.CharField(label="Sobrenome", required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    endereco = forms.CharField(label="Endereço", widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    numero = forms.CharField(label="Número", widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    cidade = forms.CharField(label="Cidade", widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    estado = forms.CharField(label="Estado", widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    # latitude = forms.CharField(label="Latitude")
    # longitude = forms.CharField(label="Longitude")
