# 📦 Blog Project com Django e Banco de Dados Oracle

Este projeto é um blog simples construído com Django, que permite a criação, edição e visualização de posts. A aplicação está configurada para utilizar um banco de dados Oracle como backend para persistência de dados.

## 🚀 Funcionalidades

- **Criação de Posts**: Permite que os usuários criem novos posts com título e conteúdo.
- **Edição de Posts**: Funcionalidade para editar posts existentes.
- **Visualização de Posts**: Exibe os detalhes de cada post.
- **Banco de Dados Oracle**: Integração com banco de dados Oracle para persistência de dados.
- **Sem Ambiente Virtual**: A aplicação foi configurada para rodar sem a necessidade de um ambiente virtual (venv).

## 🛠️ Tecnologias Utilizadas

- **Django**: Framework web utilizado para desenvolver a API.
- **Oracle Database**: Banco de dados utilizado para armazenar informações sobre os posts.
- **Python 3.x**: Linguagem de programação utilizada.
- **Pip**: Gerenciador de pacotes do Python para instalação das dependências.
  
## 📝 Como Executar

1. **Clone o Repositório**:

    ```bash
    git clone https://github.com/seuusuario/blog_project.git
    ```

2. **Navegue até o Diretório do Projeto**:

    ```bash
    cd blog_project
    ```

3. **Instale as Dependências**:

    Use o `pip` para instalar as dependências listadas no arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o Banco de Dados Oracle**:

    O projeto está configurado para utilizar um banco de dados Oracle. Altere as configurações do banco no arquivo `settings.py` para refletir suas credenciais Oracle:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'nome_do_banco',
            'USER': 'seu_usuario',
            'PASSWORD': 'sua_senha',
            'HOST': 'oracle.fiap.com.br',
            'PORT': '1521',
        }
    }
    ```

5. **Execute as Migrações**:

    Para criar as tabelas no banco de dados Oracle, execute o comando de migração:

    ```bash
    python manage.py migrate
    ```

6. **Execute o Servidor de Desenvolvimento**:

    Para rodar o servidor de desenvolvimento localmente, execute o comando abaixo:

    ```bash
    python manage.py runserver
    ```

    A API estará disponível em:

    ```http
    http://127.0.0.1:8000
    ```

## 🔍 Exemplo de Uso

Aqui estão alguns exemplos de como utilizar a API para interagir com o blog:

### Criar um Post

- **POST** `/posts/`  
  Corpo da requisição:
  ```json
  {
    "title": "Título do Post",
    "content": "Conteúdo do post."
  }
