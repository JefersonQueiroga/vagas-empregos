# Sistema de Gerenciamento de Vagas de Emprego

Sistema desenvolvido em Django para gerenciamento de vagas de emprego, empresas e funções, com sistema completo de autenticação de usuários.

## Características

- **Sistema de Autenticação** com cadastro e login de usuários
- **CRUD completo** para Função, Empresa e Vaga
- **Interface responsiva** com Bootstrap 5
- **Layout verde claro** personalizado
- **Menu lateral** para navegação fácil
- **Paginação** na listagem de Funções (10 itens por página)
- **Admin do Django** configurado para todas as entidades
- **Relacionamentos** entre entidades (Vaga → Função e Vaga → Empresa)

## Entidades

### Função
- Nome

### Empresa
- Nome
- Email
- Telefone

### Vaga
- Data de Cadastro (automática)
- Descrição da Vaga
- Função (relacionamento N:1)
- Empresa (relacionamento N:1)
- Salário
- Quantidade de Vagas

### Usuario
- User (Django User base - para autenticação)
- Email
- Endereço
- Telefone

## Como Executar

### 1. Criar e ativar o ambiente virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Instalar dependências

```bash
# Instalar todas as dependências do projeto
pip install -r requirements.txt
```

### 3. Executar as migrações do banco de dados

```bash
# Criar as tabelas no banco de dados
python manage.py migrate

# (Opcional) Criar um superusuário para acessar o admin
python manage.py createsuperuser
```

### 4. Executar o servidor

```bash
python manage.py runserver
```

### 5. Acessar o sistema

- **Tela de Login** (ponto de entrada): http://127.0.0.1:8000/usuario/login/
- **Tela de Cadastro**: http://127.0.0.1:8000/usuario/cadastro/
- **Sistema principal** (requer login): http://127.0.0.1:8000/
- **Admin do Django**: http://127.0.0.1:8000/admin/
  - Usuário: admin
  - Senha: admin (ou a senha configurada)

**IMPORTANTE**: O acesso ao sistema requer autenticação. Usuários não logados serão redirecionados para a tela de login.

## Estrutura do Projeto

```
vagas-empregos/
├── main/                   # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── vagas/                  # App de vagas, empresas e funções
│   ├── models.py          # Modelos (Funcao, Empresa, Vaga)
│   ├── views.py           # Views com CRUD
│   ├── urls.py            # Rotas
│   └── admin.py           # Configuração do admin
├── usuario/                # App de autenticação
│   ├── models.py          # Modelo Usuario
│   ├── views.py           # Views de login, cadastro, logout
│   ├── urls.py            # Rotas de autenticação
│   └── admin.py           # Configuração do admin
├── templates/              # Templates HTML
│   ├── base.html          # Template base com menu lateral
│   ├── index.html         # Página inicial
│   ├── funcao/            # Templates de Função
│   ├── empresa/           # Templates de Empresa
│   ├── vaga/              # Templates de Vaga
│   └── usuario/           # Templates de Login e Cadastro
├── manage.py
└── db.sqlite3             # Banco de dados SQLite
```

## Funcionalidades

### Sistema de Autenticação
- **Proteção de Rotas**: Todas as páginas do sistema requerem login
- **Redirecionamento Automático**: Usuários não autenticados são redirecionados para o login
- **Tela de Login** com validação de credenciais
- **Tela de Cadastro** de novos usuários com validações:
  - Confirmação de senha
  - Verificação de username único
  - Verificação de email único
- **Logout** com redirecionamento para login
- **Menu dinâmico** mostrando nome do usuário logado
- Informações adicionais: telefone e endereço

### Menu Lateral
- Navegação fácil entre as seções
- Ícones intuitivos
- Link para administração
- **Opções de Login/Cadastro** quando não autenticado
- **Botão de Logout** com nome do usuário quando autenticado

### CRUD Completo
Cada entidade (Função, Empresa, Vaga) possui:
- **Listagem** com todas as informações
- **Cadastro** de novos registros
- **Edição** de registros existentes
- **Exclusão** com confirmação

### Paginação
- Listagem de **Funções** com paginação (10 itens por página)

### Estilização
- **Bootstrap 5** para componentes responsivos
- **Font Awesome** para ícones
- **Tema verde claro** (#90EE90) personalizado
- Gradientes e efeitos de hover
- Telas de login e cadastro com design moderno e centralizado

## Tecnologias Utilizadas

- Python 3.x
- Django 5.2.8
- Bootstrap 5.3.0
- Font Awesome 6.4.0
- SQLite3

## Autor

Desenvolvido seguindo as especificações do projeto.
