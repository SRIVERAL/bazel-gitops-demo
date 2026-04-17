# saludo/main.py
import requests

def decir_hola():
    print("¡Hola Ekumen! Conectando con el mundo exterior...")
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json()["ip"]
        print(f"Mi IP pública según el contenedor es: {ip}")
    except Exception as e:
        print(f"No pude conectar: {e}")

if __name__ == "__main__":
    decir_hola()