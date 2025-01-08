# 📦 Blog Project com Django e Banco de Dados Oracle

Este projeto é um blog simples construído com Django, que permite a criação, edição e visualização de posts. A aplicação está configurada para utilizar um banco de dados Oracle como backend para persistência de dados.

## 🚀 Funcionalidades

- **Criação de Posts**: Permite que os usuários criem novos posts com título e conteúdo.
- **Edição de Posts**: Funcionalidade para editar posts existentes.
- **Visualização de Posts**: Exibe os detalhes de cada post.
- **Banco de Dados Oracle**: Integração com banco de dados Oracle para persistência de dados.


## 🛠️ Tecnologias Utilizadas

- **Django**: utilizado para desenvolver o projeto.
- **Oracle Database**: Banco de dados utilizado para armazenar informações sobre os posts.
- **Python 3.12.1**: Linguagem de programação utilizada.
- **Pip**: Gerenciador de pacotes do Python para instalação das dependências.
  
## 📝 Como Executar

1. **Clone o Repositório**:

    ```bash
     https://github.com/silvio009/Desafio_tecnico.git
    ```

2. **Navegue até o Diretório do Projeto**:

    ```bash
    cd scicrop
    cd blog_project
    ```

3. **Configure o Banco de Dados Oracle**:

    O projeto está configurado para utilizar um banco de dados Oracle. Altere as configurações do banco no arquivo `settings.py` para refletir suas credenciais Oracle:

    ```python
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '----------:1521/ORCL',  
        'USER': '-----',
        'PASSWORD': '------',
    }
    }
    ```

4. **Execute as Migrações**:

    Para criar as tabelas no banco de dados Oracle, execute o comando de migração:

    ```bash
    python manage.py migrate
    ```

5. **Execute o Servidor de Desenvolvimento**:

    Para rodar o servidor de desenvolvimento localmente, execute o comando abaixo:

    ```bash
    python manage.py runserver
    ```

    A API estará disponível em:

    ```http
    http://127.0.0.1:8000
    ```

## 🔍 Exemplo de Uso

Aqui estão alguns exemplos de como utilizar o sistema para interagir com o blog:

### Criar um Post

Para criar um novo post no blog, siga as etapas abaixo:

1. **Acesse a página de criação de post**:  
   Navegue até a página de criação de post clicando no link "Criar Novo Post" na interface do blog.

2. **Preencha o formulário**:
   A página de criação de post exibirá um formulário com dois campos principais:
   - **Título do Post**: Um campo de texto onde você deve inserir o título do seu post.
   - **Conteúdo do Post**: Um campo de texto onde você deve inserir o conteúdo do seu post.

3. **Enviar o formulário**:  
   Após preencher o formulário, clique no botão de **"Criar Post"**. O post será salvo e exibido na página inicial do blog, com o título e conteúdo preenchidos.

#### Exemplo de Uso na Página:

- **Título do Post**: "Meu Primeiro Post"
- **Conteúdo do Post**: "Este é o conteúdo do meu primeiro post no blog."

Após enviar o formulário, você será redirecionado para a página principal do blog, onde o novo post será listado.



## 📚 Aprendizado

Este projeto foi uma excelente oportunidade para aprender Django, uma framework que eu nunca tinha usado antes. Para conseguir realizar a implementação, assisti aulas da Alura e vídeos no YouTube, que me ajudaram a entender os conceitos principais do Django, como a criação de views, formulários, e como utilizar o banco de dados. Este foi um ótimo passo para aprofundar meus conhecimentos e continuar evoluindo na área de desenvolvimento.


##  💻Utilização do Banco Oracle
![print](https://github.com/user-attachments/assets/7343aa60-1a42-43bd-a050-b9e75772f612)

