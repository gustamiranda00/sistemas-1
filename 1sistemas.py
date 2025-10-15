import requests

# Chave da API do OpenWeatherMap (substitua pela sua chave)
api_key = "SUA_CHAVE_AQUI"
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"

# Fazendo a requisição
response = requests.get(url)

# Verificando o status da resposta
if response.status_code == 200:
    data = response.json()
    
    # Pegando as informações principais
    nome_cidade = data['name']
    temperatura = data['main']['temp']
    descricao = data['weather'][0]['description']
    umidade = data['main']['humidity']
    
    # Exibindo as informações
    print(f"Previsão do tempo em {nome_cidade}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Condição: {descricao.capitalize()}")
    print(f"Umidade: {umidade}%")
else:
    print(f"Erro ao acessar a API. Status code: {response.status_code}")