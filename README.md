
# API controle de gastos

O objetivo desta API é ajudar o usuário a controlar melhor suas finanças. Com ela, é possível adicionar transações e categorizá-las, permitindo assim um controle detalhado dos gastos em categorias como alimentação, roupas, entre outras.



## Autores

- [Samuel Fernando de Santana Nunes](https://www.github.com/SamuelFSNUnes)


## Descrição técnica detalhada da API

A API desenvolvida em Django Rest Framework é conectada a um banco de dados não relacional MongoDB. A estrutura segue o padrão MVT (Model-View-Template) do Django, complementado pelo padrão repository para gerenciar consultas ao banco de dados de forma organizada e reutilizável.

### Modelos de Dados
Os modelos de dados na API são representados por classes Django que mapeiam diretamente para coleções no MongoDB:

- **User:** Armazena informações de usuários, incluindo nome, email e senha.
- **Transaction:** Registra transações financeiras com detalhes como valor, data e categorização.
- **Category:** Define categorias para agrupar transações, como alimentação, transporte, entre outros.

### Estrutura da API
A API utiliza endpoints para definir operações CRUD (Create, Read, Update, Delete) para cada modelo. Cada endpoint é associado a uma view que implementa lógica de negócios específica e chama métodos do repository para interagir com o banco de dados.

### Camadas da Arquitetura
- **Endpoints:** Define URLs e métodos HTTP para cada recurso da API.
- **Views:** Implementa lógica de negócios e processamento de requisições HTTP.
- **Repository:** Encapsula operações de banco de dados para abstrair detalhes de implementação e promover reutilização de código.
- **Models:** Define a estrutura dos dados armazenados no MongoDB.
- **Serializer:** Inclui métodos para serialização e desserialização, para manter a integração do dados cadastrados.

### Tecnologias Utilizadas
- **Django Rest Framework:** Facilita a criação de APIs RESTful em Django com suporte a serialização, autenticação, e outras funcionalidades.
- **MongoDB:** Banco de dados NoSQL escolhido pela sua flexibilidade e escalabilidade, ideal para armazenar dados não estruturados como transações financeiras.
- **Python:** Linguagem de programação principal, proporcionando simplicidade e eficiência no desenvolvimento de APIs com Django.

## Requisitos

- **Python 3.x**
- **pip (Python package installer)**
- **MongoDB**
- **Virtualenv (opcional, mas recomendado)**

## Instalação

### Passo 1: Clonar repositório
https://github.com/SamuelFSNunes/TransactionApplication.git

cd caminho/para/o/projeto

Exemplo: C:\Users\User\Desktop\TransactionApplication

### Passo 2: Criar e Ativar um Ambiente Virtual
python -m venv venv

- **No Linux:** source venv/bin/activate 
- **No Windows:** venv\Scripts\activate

### Passo 3: Instalar as Dependências
pip install -r requirements.txt

### Passo 4: Instalar e configurar o MongoDB
[MongoDB Download](https://www.mongodb.com/try/download/community)
ou https://www.mongodb.com/try/download/community 

Ao abrir o launcher iniciar um conexão na uri mongodb://localhost:27017

### Passo 5: Iniciar a aplicação
python manage.py runserver

### Observações

Caso a conexão não seja bem sucedida com mongoDB, criar um database com o nome `mongodatabase` via launcher.

o arquivo `mongodatabase_categories_json` é um JSON com categorias padrões já criadas, caso tenha interesse pode cadastrar direto no banco de dados com a collection de nome `categories`
