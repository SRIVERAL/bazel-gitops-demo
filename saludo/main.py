import time
from prometheus_client import start_http_server, Counter

# Definimos la métrica: Un contador para los saludos
# El primer parámetro es el nombre de la métrica en Prometheus
SALUDOS_TOTAL = Counter('saludo_app_mensajes_total', 'Total de saludos emitidos por la app')

def main():
    # Iniciamos un servidor web en el puerto 8000 para exponer las métricas
    # Prometheus vendrá a este puerto a "leer" los datos
    start_http_server(8000)
    print("Servidor de métricas iniciado en el puerto 8000")

    while True:
        print("¡Hola Ekumen desde K8s con seguridad y métricas!")
        # Incrementamos el contador
        SALUDOS_TOTAL.inc()
        time.sleep(10)

if __name__ == "__main__":
    main()