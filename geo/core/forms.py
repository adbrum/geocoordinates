from django import forms


class CoordenadaForm(forms.Form):
    endereco = forms.CharField()
    numero = forms.CharField()
    cidade = forms.CharField()
    estado = forms.CharField()
    latitude = forms.CharField(label="Latitude")
    longitude = forms.CharField(label="Longitude")
