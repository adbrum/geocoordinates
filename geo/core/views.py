import requests
from django.shortcuts import render
from geo.core.forms import CoordenadaForm
from geo.core.models import Pessoa, Coordenada


def geoCoordenada(request):
    if request.method == 'POST':
        form = CoordenadaForm(request.POST)

        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        numero = request.POST['numero']
        estado = request.POST['estado']
        # longitude = request.POST['longitude']
        # latitude = request.POST['latitude']

        address = numero + ' ' + endereco + ', ' + cidade + ', ' + estado

        # address = "1600 Amphitheatre Parkway, Mountain View, CA"
        api_key = "AIzaSyBWKWlI1WE9nvuld9AVcpTZQItHLTUmWxo"
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()

        if api_response_dict['status'] == 'OK':
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            print('Latitude:', latitude)
            print('Longitude:', longitude)

            # cria uma pessoa
            pessoa = Pessoa.objects.create(nome=nome,
                                           sobrenome=sobrenome)

            Coordenada.objects.create(possoa_id=pessoa.pk,  # insere o pk do pessoa.
                                      endereco=endereco,
                                      cidade=cidade,
                                      numero=numero,
                                      estado=estado,
                                      longitude=longitude,
                                      latitude=latitude
                                      )

            return render(request, 'index.html',
                          {
                              'latitude': latitude,
                              'longitude': longitude,
                              'form': CoordenadaForm(),
                          })
        else:
            return render(request, 'index.html',
                          {'form': form})
    else:
        return render(request, 'index.html',
                      {'form': CoordenadaForm()})
