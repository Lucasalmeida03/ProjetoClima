import requests

# Chamada da Key
API_Key = "b936e473931f2a95a0ea07d7a70c955d"

# Cidade desejada
cidade = input("Insira uma cidade: ")

# chamada da API e tradução da para português
base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=' + \
    API_Key+'&q='+cidade+"&lang=pt_br"

# extrações dos dados
informações_dic = requests.get(base_url).json()

# filtragem de informações climáticas
descrição = informações_dic["weather"][0]["description"]
temperatura = informações_dic["main"]["temp"] - 273.15
sensação_termica = informações_dic["main"]["feels_like"] - 273.15

# exibição
print(descrição)
print(f"{temperatura}°C")
print(f"{sensação_termica}°C")
