from django.shortcuts import render
import requests
from geo.core.forms import CoordenadaForm


def geoCoordenada(request):
    if request.method == 'POST':
        form = CoordenadaForm(request.POST)
        print('XXXXX: ', request.POST)

        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        numero = request.POST['numero']
        estado = request.POST['estado']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']

        address = numero +' '+ endereco +', '+ cidade +', '+ estado

        # address = "1600 Amphitheatre Parkway, Mountain View, CA"
        api_key = "AIzaSyBWKWlI1WE9nvuld9AVcpTZQItHLTUmWxo"
        api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()

        if api_response_dict['status'] == 'OK':
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            print('Latitude:', latitude)
            print('Longitude:', longitude)

        return render(request, 'index.html',
                      {'form': CoordenadaForm()})
    else:
        return render(request, 'index.html',
                      {'form': form()})