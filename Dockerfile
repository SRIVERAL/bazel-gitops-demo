# Usamos una imagen base de Ubuntu 22.04 que es estándar en robótica
FROM ubuntu:22.04

# Evitar prompts interactivos durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias básicas
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    python3 \
    python3-pip \
    g++ \
    unzip \
    zip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar Bazelisk (el wrapper oficial para manejar versiones de Bazel)
RUN curl -L https://github.com/bazelbuild/bazelisk/releases/download/v1.19.0/bazelisk-linux-amd64 -o /usr/local/bin/bazel && \
    chmod +x /usr/local/bin/bazel

# Crear directorio de trabajo
WORKDIR /app

# Comando por defecto
CMD ["/bin/bash"]