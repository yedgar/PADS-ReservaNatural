# PADS-ReservaNatural
Reserva Natural

Indicaciones:

1. Clonar el repositorio:
https://github.com/yedgar/PADS-ReservaNatural.git

2. En la ambiente virtual se deben tener instalados los paquetes:
   - Django
   - postgres
   - psycopg2
   
   ó instalarlos con el el comando pip
 
3. Crear la base de datos, se deberá correr al inicio el comando:
    
    python manage.py migrate
    
4. Una vez verificado que desde la base de datos se encuentran creadas las tablas, se corre el servidor.
 
5. Probar con http://localhost:8000/polls
 
 
 -----------------------------------------
 
 Hay dos carpetas
  ReservaNatural: es la principal donde se registran las urls que se vayan creando
  polls: es la aplicación, aca se encuentra todo, models, views, templates/polls/*.html, entre otros
  (images cuando creen usuarios)
  
  Tener en cuenta que la aplicacion se constryo con base al tutorial 5. Se utiliza ajax y rest.
