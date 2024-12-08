import requests
import subprocess
import os

def check_download_speed():
    url = "http://speed.hetzner.de/10MB.bin"  # URL de teste
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Levanta um erro se a resposta for um erro HTTP

        start_time = response.elapsed.total_seconds()
        total_size = int(response.headers.get('content-length', 0))
        download_speed = total_size / (1024 * 1024) / start_time  # MB/s
        
        print(f"Velocidade de download: {download_speed:.2f} MB/s")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao tentar baixar: {e}")

def change_steam_download_region(region):
    # Substitua o caminho abaixo pelo caminho correto do executável da Steam no seu sistema
    steam_path = r"C:\Program Files (x86)\Steam\steam.exe"
    
    if not os.path.exists(steam_path):
        print("O caminho para o executável da Steam não foi encontrado.")
        return
    
    # Muda a região de download da Steam
    subprocess.run([steam_path, "-command", "set_download_region", region])

if __name__ == "__main__":
    check_download_speed()
    
    region = input("Digite a nova região de download (ex: Brasil, EUA): ")
    change_steam_download_region(region)
