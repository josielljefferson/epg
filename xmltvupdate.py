import requests
import time

# URL do EPG
epg_url = "http://m3u4u.com/epg/p192y7m4g8fvq12gymeg"

# Função para baixar e salvar o EPG
def atualizar_epg(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        with open("epg.xml", "wb") as file:
            file.write(response.content)
        print("EPG atualizado com sucesso!")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao atualizar o EPG: {e}")

# Intervalo de atualização em segundos (2 horas)
intervalo_atualizacao = 2 * 60 * 60

# Loop infinito para atualizar o EPG periodicamente
while True:
    atualizar_epg(epg_url)
    time.sleep(intervalo_atualizacao)
