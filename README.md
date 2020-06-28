# gestao-produtos
Primeiro projeto utilizando os frameworks Django e Bootstrap  
Developer: Victor Veiga  
Data: 28/06/2020  

![Imagem de home page](https://github.com/victorveiga/gestao-produtos/blob/master/statics/img/home.png)

# Primeiros passos...

1 - Criar uma virtualenv e ativá-la:  
  * python -m venv venv  
  * cd venv\Scripts\activate 
  
2 - Clonar o repositório e instalar as dependências:
  * git clone https://github.com/victorveiga/gestao-produtos.git
  * cd gestao-produtos
  * pip install -r requirements.txt
  
3 - Aplicar as migrations:
  * python manage.py migrate
  
4 - Criar um usuário administrador:
  * python manage.py createsuperuser
  * Informar um nome de usuário, email e senha
  
5 - Executar o serviço:
  * python manage.py runserver
  * acessar a homepage através do link: http://localhost:8000/
