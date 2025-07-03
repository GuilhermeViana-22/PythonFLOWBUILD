# Instruções de Configuração - PythonFlowBuild

## 🔧 Problemas Corrigidos

### Problema Principal
O projeto estava configurado para usar MySQL mas com dependências incompatíveis, causando erros no `mysqlclient`.

### Soluções Implementadas

1. **Configuração do Banco de Dados**
   - Alterado de MySQL para SQLite no `settings.py`
   - SQLite é mais simples e não requer configuração externa
   - Configuração MySQL comentada para uso futuro

2. **Dependências**
   - Removido `mysql-connector-python` do `requirements.txt`
   - Mantidas apenas dependências necessárias para SQLite

3. **Migrações**
   - Criadas e aplicadas migrações para os modelos
   - Banco de dados SQLite configurado corretamente

## 🚀 Como Iniciar o Projeto

### 1. Ativar o Ambiente Virtual
```bash
cd /home/guilherme/Projetos/PythonFlowBuild
source venv/bin/activate
```

### 2. Instalar/Atualizar Dependências
```bash
pip install -r requirements.txt
```

### 3. Verificar Configuração
```bash
python3 manage.py check
```

### 4. Iniciar o Servidor
```bash
python3 manage.py runserver
```

### 5. Acessar o Projeto
Abra o navegador e acesse: `http://localhost:8000`

## 📁 Estrutura do Projeto

```
PythonFlowBuild/
├── mvp_project/          # Configurações principais
│   ├── settings.py       # Configurações do Django (agora com SQLite)
│   ├── urls.py          # URLs principais
│   └── wsgi.py          # WSGI configuration
├── accounts/            # App de contas/perfis
├── authentication/      # App de autenticação
├── welcome/            # App da página inicial
├── database/           # Conexão MySQL customizada (não utilizada)
├── templates/          # Templates HTML
├── db.sqlite3         # Banco de dados SQLite
└── requirements.txt   # Dependências do projeto
```

## 🎯 Funcionalidades Disponíveis

- ✅ **Página Welcome**: Interface moderna com Bootstrap
- ✅ **Sistema de Autenticação**: Login/Logout/Registro
- ✅ **API REST**: Endpoints com JWT
- ✅ **Templates Responsivos**: Design mobile-first
- ✅ **Banco de Dados**: SQLite configurado

## 🔄 Para Usar MySQL no Futuro

Se quiser usar MySQL posteriormente:

### 1. Instalar MySQL Server
```bash
sudo apt update
sudo apt install mysql-server mysql-client
```

### 2. Instalar Dependências Python
```bash
# Para mysqlclient (recomendado)
sudo apt install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient

# OU para mysql-connector-python (alternativa)
pip install mysql-connector-python
```

### 3. Configurar o Banco
```bash
sudo mysql_secure_installation
mysql -u root -p
```

```sql
CREATE DATABASE mvp_db;
CREATE USER 'mvp_user'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON mvp_db.* TO 'mvp_user'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Atualizar settings.py
Descomente a configuração MySQL e comente a SQLite:

```python
# Comente esta linha:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Descomente esta configuração:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mvp_db',
        'USER': 'mvp_user',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Executar Migrações
```bash
python3 manage.py migrate
```

## 🐛 Comandos Úteis para Debug

```bash
# Verificar configuração
python3 manage.py check

# Ver migrações pendentes
python3 manage.py showmigrations

# Acessar shell do Django
python3 manage.py shell

# Criar superusuário
python3 manage.py createsuperuser

# Coletar arquivos estáticos
python3 manage.py collectstatic
```

## 📝 Notas Importantes

1. **Use `python3`** ao invés de `python`
2. **Ative o ambiente virtual** antes de trabalhar
3. **SQLite é adequado para desenvolvimento** e testes
4. **MySQL é recomendado para produção** com múltiplos usuários
5. **A classe MySQLConnection** em `database/` não é utilizada pelo Django

## 🎉 Status Atual

✅ **Projeto funcionando corretamente!**
- Configuração verificada: OK
- Migrações aplicadas: OK
- Servidor Django: OK
- Dependências: OK

O projeto está pronto para uso e desenvolvimento! 