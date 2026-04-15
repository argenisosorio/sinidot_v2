<h1>SINIDOT v2</h1>

El SINIDOT (Sistema Nacional de Información sobre Donación y Trasplante) es una
aplicación web diseñada para la gestión de donación y trasplante de órganos en
Venezuela. Permite el registro inicial de datos, gestión de usuarios,
administración de donantes y solicitudes, así como la generación de reportes y
estadísticas.

* Entorno: Desarrollo

<h2>Requerimientos generales</h2>

Asegúrate de tener instaladas los siguientes paquetes y versiones:

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

Se recomienda el uso de un entorno virtual para aislar las dependencias del
proyecto. A continuación, se detallan los pasos para configurar el entorno
utilizando el módulo estándar venv de Python 3. No obstante, también se sugiere
el uso de pyenv como una alternativa robusta para la gestión de versiones y
entornos de Python.

1. Actualiza la lista de paquetes (en sistemas basados en Debian/Ubuntu):

    $ sudo apt update

2. Instala python3-venv:

    $ sudo apt install python3-venv

3. Crea el entorno virtual fuera del directorio del SINIDOT v2:

    $ python3 -m venv my_environment

4. Activa el entorno:

    source my_environment/bin/activate

5. Navega al directorio backend:

    $ cd backend

6. Instala las dependencias específicas de Python:

    $ pip install -r requirements.txt

7. Crea tu archivo de configuración local:

    $ cp config/settings.py_example config/settings.py

8. Ejecuta las migraciones y crea la base de datos:

    $ python manage.py makemigrations users donors applicants

    $ python manage.py migrate

9. Crea un superusuario:

    $ python manage.py createsuperuser

10. Inicia el servidor de desarrollo:

    $ python manage.py runserver

<h4>Prueba el backend</h4>

Abre tu navegador y visita http://127.0.0.1:8000 verás el mensaje
"Bienvenido al SINIDOT v2" lo que indica que Django está funcionando.

<h4>Prueba la API de Django Ninja</h4>

La documentación interactiva de la API estará disponible en:

http://127.0.0.1:8000/api/docs

Desde la interfaz puedes usar usar las funcionalidades CRUD sobre el modelo
Donor y Applicant.

* Documentación técnica del backend: docs/technical_documentation.txt
