# PADS-ReservaNatural
Reserva Natural

Indicaciones:

1. Clonar el repositorio:
https://github.com/yedgar/PADS-ReservaNatural.git

2. En la ambiente virtual se deben tener instalados los paquetes:
   - Django
   - postgres -> Instalar Postgres en el computador y asegurar que se encuentra en el Path para poder instalar los paquetes
   - psycopg2
   - Pillow para porder ver las imagenes si lo pide: pip install Pillow
   
   ó instalarlos con el el comando pip
 
3. Crear la base de datos, se deberá correr al inicio el comando:
    
    python manage.py migrate
    
4. Una vez verificado que desde la base de datos se encuentran creadas las tablas, se corre el servidor.
 
5. Probar con http://localhost:8000/polls

6. Crear el usuario super user para poder acceder a la funcionalidad de administrador: python manage.py createsuperuser

7. Ingresar a http://localhost:8000/admin con el usuario administrador e ingresar: Categorias y luego Especies para poder verlos en la pantalla Principal

 
 
 -----------------------------------------
 
 Hay dos carpetas
  ReservaNatural: es la principal donde se registran las urls que se vayan creando
  polls: es la aplicación, aca se encuentra todo, models, views, templates/polls/*.html, entre otros
  (images cuando creen usuarios)
  
  Tener en cuenta que la aplicacion se constryo con base al tutorial 5. Se utiliza ajax y rest.
