# Investments API Coderockr 🖤

<img src="imagem.png" alt="Exemplo imagem">

> Linha adicional de texto informativo sobre o que o projeto faz. Sua introdução deve ter cerca de 2 ou 3 linhas. Não exagere, as pessoas não vão ler.


## 💻 Pré-requisitos

Para executar o projeto em sua maquina é importantate ter instalado em sua maquina:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🚀 Instalando

Para instalar a aplicação, siga estas etapas:

Depois de ter clonado o repositório execute o comando para entrar na pasta do projeto:

```
 cd api-coderockr
```

Crie o arquivo que irá conter as variáveis de ambiente da aplicação:
```
 cp .env_example .env
```
Caso o comando anterior não funcione em seu sistema operacional, crie um ".env" com o conteúdo o conteúdo do ".env_example".


Em seguida utilize o comando para gerar o build de nossos containers

```
 docker-compose build
```

Por fim, rode o comando para subir nossa aplicação:
```
 docker-compose up
```

## ☕ Usando a aplicação

Acesse a documentação da API em [localhost:8000/api#](http://localhost:8000/api#/)


