import requests
import time

# URL do EPG
epg_url = "http://m3u4u.com/epg/p192y7m4g8fvq12gymeg"

# Função para baixar e salvar o EPG
def atualizar_epg(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        with open("epg.xml", "wb") as file:
            file.write(response.content)
        print("EPG atualizado com sucesso!")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao atualizar o EPG: {e}")

# Intervalo de atualização em segundos (2 horas)
intervalo_atualizacao = 1 * 60 * 60

# Loop infinito para atualizar o EPG periodicamente
while True:
    atualizar_epg(epg_url)
    time.sleep(intervalo_atualizacao)
    
