# testSimetrik
> ```
> ** Python Version:** 3.8.2
> ** Django Version:** 3.0.8
>
> ```
## Descripción
> Este es un proyecto que se realiza como prueba tecnica para desarrollador Backend en python | Django

## Puesta en Marcha
> Para poner en marcha el proyecto es necesario clonar el repositrio en una directorio del local.
> ```
> git clone https://github.com/dcorquir/testSimetrik.git
> ```
>
> Luego es necesario crear un entorno virtual (debe estar con la version de python >= 3.5)
> ```
> Windows:
> python -m venv myvenv
>
> Linux:
> python3 -m venv myven
> ```
> Luego se debe activar el entorno virtual
> ```
> Windows:
> myvenv\Scripts\activate
>
> Linux:
> source myvenv/bin/activate
> ```
> Luego es necesario instalar los requirements, para ello se ejecuta el siguiente comando:
> ```
> pip install -r requirements.txt
> ```
>
> Luego es necesario ajustar el archivo settings.py, ya que se sube al repositorio con -dist en su nombre. Para ello es necesario editar el nombre de este archivo, y dejarlo como setting.py, solamente.
>
> Luego debemos abrir el archivo setting.py y ajustar la configuracion para la ruta de conexión de SqlAlchemy.
> Para eso, debemos modificar la constante: ** DATABASE_ENGINE **
> También en este archivo, debemos modificar la ruta de lectura, donde está expuesto el archivo .csv para lectura.
> Para eso, debemos modificar la constante: ** URL_FILE **
>
> Luego podemos poner en marcha el proyecto. Para eso en la consola se ejecuta el comando:
> ```
> python manage.py runserver
> ```

## EndPoints
> Dentro del proyecto tenemos 2 endpoints:
> ```
>
> api/transactions/ -- GET
>
> Este endpoint accedido por métod Http | GET, es el encargado de realizar la consulta de los datos cargados en la base de datos, para ello debe contener unos query params requeridos
>
> api/transactions/?transaction_id=0000&client_id=0000&transaction_date=2020-06-01&sort=-transaction_id&page=1&per_page=10
>
> ```
>
> ```
>
> api/transactions/ -- POST
>
> Este endpoint accedido por métod Http | POST, es el encargado de iniciar la tarea de lectura del archivo y carga de los datos en la base de datos.
>
> ```