<h1>SINIDOT v2</h1>

El **SINIDOT**  (Sistema Nacional de Información sobre Donación y Trasplante) es
una aplicación web diseñada para la gestión de donación y trasplante de órganos
en Venezuela. Permite el registro inicial de datos, gestión de usuarios,
administración de donantes y solicitudes, así como la generación de reportes y
estadísticas.

* Entorno: Desarrollo

<h2>Requerimientos del Sistema Operativo</h2>

Asegúrate de tener instaladas las siguientes versiones:

```
Python >= 3.12
Django == 6.0.2
Node.js >= v20.20.0
npm >= 11.11.0
PostgreSQL >= 17
```

<h2>Configuración del entorno de desarrollo</h2>

Sigue estos pasos para ejecutar el proyecto en tu entorno de desarrollo local:

<h3>Configuración del backend (Django)</h3>

Se recomienda el uso de un entorno virtual de Python. A continuación se
describen los pasos para crearlo y activarlo:

1. Actualiza la lista de paquetes (en sistemas basados en Debian/Ubuntu):

    $ sudo apt update

2. Instala python3-venv:

    $ sudo apt install python3-venv

3. Crea el entorno virtual:

    $ python3 -m venv my_environment

4. Activa el entorno:

    source my_environment/bin/activate

5. Navega al directorio backend:

    $ cd backend

6. Instala las dependencias de Python:

    $ pip install -r requirements.txt

7. Crea tu archivo de configuración local:

    $ cp backend/settings.py_example backend/settings.py

8. Ejecuta las migraciones y crea la base de datos:

    $ python manage.py makemigrations users products

    $ python manage.py migrate

9. Crea un superusuario:

    $ python manage.py createsuperuser

10. Inicia el servidor de desarrollo:

    $ python manage.py runserver

<h4>Prueba el backend</h4>

Abre tu navegador y visita http://127.0.0.1:8000 verás la aplicación de Django
en funcionamiento.

<h4>Prueba la API de Django Ninja</h4>

La documentación interactiva de la API estará disponible en:

http://127.0.0.1:8000/api/docs


















<h3>Frontend Setup (Nuxt)</h3>

Open a new terminal and navigate to frontend directory

```
$ cd frontend
```

Install Node.js dependencies

```
$ npm install
```

Create your local settings file

```
$ cp .env_example .env
```

Start the Nuxt development server

```
$ npm run dev
```

The Nuxt application will be available at http://localhost:3000/

<h2>Access the Application</h2>

Once both servers are running:

Backend API: http://127.0.0.1:8000/api/person - Django Ninja person endpoint

Frontend: http://localhost:3000/ - View the initial project page
