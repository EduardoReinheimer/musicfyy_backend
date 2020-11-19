# Musicfyy

Uma API programada em Python com o uso do Django Rest Framework para a consulta e carregamento de músicas, front-end do musicfyy foi escrito em Vue.JS e se encontra [nesse link](https://github.com/EduardoReinheimer/musicfyy_frontend.git "Front-end repo")

# Para rodar localmente:

## 1 - Instale os pacotes e bibliotecas necessárias utilizando pip
```
pip -r requirements.txt
```
## Ou se você estiver usando pipenv
```
pipenv install
```
## 2 - Para a criação do banco de dados
```
python manage.py migrate
```
## 3 - Para carregar backup e não precisar criar conta e nem upar músicas manualmente
```
python manage.py loaddata backup.json
```
Assim que rodar esse comando, você pode se logar com as credenciais usu@aria.com/usuaria123

## 4 - Para iniciar o servidor
```
python manage.py runserver
``` 

Et voilá
