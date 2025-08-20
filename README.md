## API Candy Soft - Proyecto Modularizado  

API **Candy Soft** es un sistema modularizado diseñado para la gestión integral de un **spa de uñas**.  
Su objetivo principal es ofrecer una arquitectura **organizada, escalable y mantenible**, donde cada módulo represente una funcionalidad independiente del negocio.  

---

## Explicación de los módulos y clases con pruebas  

- **Módulo Usuario** → Administra los usuarios del sistema (administradores y recepcionistas).  
- **Módulo Manicurista** → Gestiona los datos de las especialistas encargadas de realizar los servicios.  
- **Módulo Cliente** → Administra la información de los clientes que solicitan los servicios.  

- **Módulo Calificación** → Registra las valoraciones de los servicios prestados.  
- **Módulo Servicio** → Administra la información de los servicios ofrecidos (ejemplo: acrílicas, esmaltado, diseños).  
- **Módulo Rol** → Define los permisos y roles del sistema (administrador, recepcionista, etc.).  

---

## Tecnologías utilizadas  

Antes de comenzar, debes de tener instaladas las siguientes herramientas:  

- **Python** (Versión 3.10 o superior)   
  [Descargar](https://www.python.org/downloads/)  

- **MySQL** (Gestión de base de datos)  
  [Descargar](https://dev.mysql.com/downloads/)  

- **Git** (para clonar el repositorio)  
  [Descargar](https://git-scm.com/downloads)  

- **Visual Studio Code** (editor recomendado para el desarrollo)  
  [Descargar](https://code.visualstudio.com/download)  

---

## Instalación y despliegue
```bash

# 1. Clonar el repositorio  

# Opción 1: Clonar desde GitHub  
1. Entra al repositorio en GitHub y da clic en el botón **Code**.  
2. Copia el enlace HTTPS que aparece.  
3. Abre **Visual Studio Code (VS Code)**.  
4. Dirígete a la barra lateral izquierda y selecciona el ícono de **Source Control**.  
5. Haz clic en **Clonar repositorio**.  
6. Pega el enlace que copiaste de GitHub.  
7. Selecciona la carpeta en tu equipo donde quieras guardar el proyecto.  
8. Una vez finalizada la clonación, **VS Code** abrirá automáticamente el proyecto.  

# Opción 2: Descargar en ZIP  
1. Entra al repositorio en GitHub y da clic en el botón **Code**.  
2. Selecciona la opción **Download ZIP**.  
   - Esto descargará el proyecto comprimido en tu computador.  
3. Una vez descargado, busca el archivo donde se haya descargado. 
4. Descomprime el archivo y ábrelo en **VS Code**. 

# Opción 3: Línea de comandos  
1. Abre una terminal:  
   - Puedes usar **CMD** o la terminal integrada en **VS Code**.  

2. Escribe el siguiente comando:  
git clone https://github.com/Andrea-gonzalez-bit/ApiCandySoft.git
cd ApiCandySoft


---

# 2. Crear archivo `.env`
1. Créalo dentro de la carpeta **apiCandySoft**.  
2. Copia y pega el siguiente código:  

# IMPORTANTE SOBRE LA CONTRASEÑA:
# Cambia "tu_contraseña" por la contraseña real de tu usuario MySQL.
# Si tu usuario NO tiene contraseña, deja este campo vacío (ejemplo: DB_PASSWORD=).

# IMPORTANTE SOBRE EL PUERTO:
# Este proyecto está configurado por defecto para usar el puerto 3308.
# Si en tu equipo MySQL corre en otro puerto (ejemplo: 3306 o 3307),
# cambia este valor para que coincida con tu configuración.

SECRET_KEY='django-insecure-$=ae#$xpmjkw=7v&&0kv@$a)j+o9ti%u%z+tygd#3nzju=pajc'
DEBUG=True

# Base de datos - solo cambia esto
DB_ENGINE=django.db.backends.mysql
DB_NAME='CandySoftApi2'
DB_USER='root'
DB_PASSWORD='tu-contraseña'
DB_HOST=127.0.0.1
DB_PORT=3308

# Tema de correo - esto dejarlo igual
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='candysoftpruebaapi@gmail.com'
EMAIL_HOST_PASSWORD='ikyp huvb lnia zekw'

IMGBB_API_KEY='fec1ab2811dc77a5801a0952fead16'

---

# 3. Crear entorno virtual
python -m venv venv


# 4. Activar entorno virtual en PowerShell 
.\venv\Scripts\activate


# 5. Instalar dependencias
pip install -r requirements.txt

# 6.Importar base de datos con el archivo SQL

# Primero debes crear la base de datos vacía en MySQL
CREATE DATABASE CandySoftApi2;

# Luego importa el archivo db_apicandydoft.sql en la base de datos:
# NOTA: en la parte -p --port=3308, el proyecto está configurado con 3007, si su MySQL corre 3307 o 3306, +6lo debes de cambiar
Get-Content db_apicandysoft.sql  | & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p --port=3308 CandySoftApi2 


# 7. Ingresar a la carpeta principal donde está manage.py
cd apiCandySoft


# 8. Migrar base de datos (opcional)
# Solo usa esta opción si no funciona la importación con el archivo SQL.
python manage.py migrate


# 9. Ejecutar pruebas unitarias
# Nota: después de ejecutar cada prueba es necesario revisar los resultados
# porque los datos quedan guardados en la base de datos y no se puede guardar el mismo dato dos veces.

# Módulo usuario (Carpeta usuario/tests/)
python manage.py test usuario.tests.test_usuario
python manage.py test usuario.tests.test_manicurista
python manage.py test usuario.tests.test_cliente

# Módulo rol (Carpeta rol/tests/)
python manage.py test rol.tests.test_rol

# Módulo servicio (Carpeta servicio/tests/)
python manage.py test servicio.tests.test_servicio

# Módulo calificación (Carpeta calificacion/tests/)
python manage.py test calificacion.tests.test_calificacion







