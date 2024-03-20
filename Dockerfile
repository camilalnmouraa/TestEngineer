# Use a imagem Python 3.8 como base
FROM python:3.8

# Copie os arquivos do projeto para o diretório de trabalho
COPY . /app

# Defina o diretório de trabalho como /app
WORKDIR /app

# Instale as dependências do projeto
RUN pip install --upgrade pip && \
    apt-get update && apt-get install -y libgl1-mesa-glx && \
    pip install -r requirements.txt

# Exponha a porta 3000 (se necessário)
EXPOSE 3000

# Comando para executar os testes ou iniciar sua aplicação
CMD [ "pytest" ]

