# Estado del build (badge) 

### (Se agrega por trabajo de implantación - automatización con Github actions) 

![Django Tests](https://github.com/Andrea-gonzalez-bit/ApiCandySoft/actions/workflows/django-tests.yml/badge.svg)

#### 📌Muestra el estado de tu workflow (django-tests.yml).

- Tiene tres estados posibles:

  - Verde → las pruebas pasaron.

  - Rojo → alguna prueba falló.

  - Amarillo → está en ejecución.


## API Candy Soft - Proyecto Modularizado (Trabajo de prueba)

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

# Configuración adicional de la base de datos
1. Dirígete a la carpeta del proyecto `apiCandySoft`.  
2. Ingresa al archivo `settings.py`. 
3. Ubica el siguiente bloque 

# Actualmente, el bloque de código luce así:
db_url = os.getenv("DATABASE_URL")

if db_url and "sslmode=disable" in db_url:
    DATABASES = {
        "default": dj_database_url.parse(
            db_url,
            conn_max_age=600,
            ssl_require=False
        )
    }
else:
    DATABASES = {
        "default": dj_database_url.parse(
            db_url,
            conn_max_age=600,
            ssl_require=True
        )
    }


# Debes de remplazar por este:
# El bloque de configuración actualizado quedaría de la siguiente forma:

DATABASES = {
    'default':{
        'ENGINE': os.getenv("DB_ENGINE"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'OPTIONS': {
          'charset' : 'utf8mb4',
        }
    }
}


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



# Automatización de pruebas con GitHub Actions (Trabajo implantación)

Este proyecto cuenta con un flujo de integración continua (CI) configurado con GitHub Actions.
Cada vez que haces un push o un pull request hacia la rama main, se ejecutan automáticamente las pruebas unitarias del proyecto.

**Nota importante**

Ya el código de .github/workflows/django-tests.yml esta actualizado según Despliegue en IaaS

---

## Ubicación del workflow

El flujo se encuentra en el archivo:

```bash

.github/workflows/django-tests.yml

```

---

## ¿Qué hace el workflow?

- Configura un entorno en Ubuntu.
- Levanta un servicio de PostgreSQL 14 (antes era MySQL 8.0, ya se actualizó).
- Instala Python 3.10.
- Instala las dependencias desde `requirements.txt`.
- Configura las variables de entorno de Django (simulando lo que está en el `.env`).
- Usa la variable `DATABASE_URL` para conectarse a la base de datos de pruebas en PostgreSQL.
- Ejecuta las migraciones con `python manage.py migrate`.
- Corre todas las pruebas unitarias con `python manage.py test`.

---

## Resultado

- Si las pruebas pasan ✅, GitHub marca el commit o PR como exitoso.

- Si alguna prueba falla ❌, el flujo se detiene y verás el error en la pestaña Actions de GitHub.

**Nota importante**

- En GitHub Actions, la base de datos se crea con migrate (sin usar el archivo db_candysoft.sql).

- En tu PC local, puedes usar db_candysoft.sql para cargar datos de ejemplo más rápido.

---

[Ver ejecuciones en GitHub Actions](https://github.com/Andrea-gonzalez-bit/ApiCandySoft/actions)

**Nota importante**

Ese enlace abre la pestaña **Actions** del repositorio, donde podrás ver:

- Ver todas las ejecuciones pasadas del flujo `django-tests.yml`.
- Revisar si un commit pasó o falló las pruebas.
- Consultar los logs detallados de cada paso del workflow.

---

# Despliegue en IaaS (Trabajo implantación)

API Rest desarrollada en **Django Rest Framework**, desplegada en **Render** y conectada a **Supabase (PostgreSQL)**.

---

## Deploy
- API principal: https://apicandysoft-kcow.onrender.com

---

## Tecnologías
- Django Rest Framework
- PostgreSQL (Supabase)
- Render (IaaS)

---

## Uso de la API
Ejemplo de endpoints disponibles:
- `GET /api/usuario/` → Lista de usuarios
- `POST /api/auth/` → Autenticación
- `GET /api/servicio/` → Lista de servicios

---

## Correr localmente

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

# 2. Crear archivo .env
# - Crealo dentro de la carpeta apiCandySoft, se debe llamar asi .env
# - Copia y pega el siguiente código

# No cambiar nada, ya que son los datos de la base de datos (Supebase)

SECRET_KEY=django-insecure-$=ae#$xpmjkw=7v&&0kv@$a)j+o9ti%u%z+tygd#3nzju=pajc
DEBUG=True

DATABASE_URL=postgresql://postgres.tshedqxfkkyhivglydzl:Gonzalez_pineda1032@aws-1-us-east-1.pooler.supabase.com:6543/postgres

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=candysoftpruebaapi@gmail.com
EMAIL_HOST_PASSWORD=ikyp huvb lnia zekw

IMGBB_API_KEY=fec1ba28d181c77a5801a0952fead016

# Abre la terminal (PowerShell) y ejecuta los siguientes comandos en este orden

# 3. Crear entorno virtual
python -m venv venv

# 4. Activar entorno virtual (en PowerShell)
.\venv\Scripts\activate

# 5. Ingresar a la carpeta principal donde está manage.py
cd apiCandySoft

# 6. Instalar dependencias 
pip install -r requirements.txt

# 7. Migrar base de datos con Django
python manage.py migrate

# ⚠️ Nota: El comando anterior aplicará migraciones en la base de datos definida en tu archivo `.env`.
# Si usas la misma `DATABASE_URL` de producción (Supabase), los cambios se reflejarán directamente en la base en la nube.
# Se recomienda tener una base de datos separada para desarrollo y pruebas.

# 8. Levantar el servidor
python manage.py runserver









