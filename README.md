# CRUD-SQLite3
App de preguntas que implementa CRUD con SQLite3

## Base de datos
Estamos usando SQLite3 para almacenar los datos de las preguntas y respuestas.
Para crear una base de datos en SQLite3, se debe crear un archivo con extensión `.db` y luego se debe crear una tabla con la estructura de datos que se desea almacenar.
```
sqlite3 nombre_base_datos.db
```
Para crear una tabla, se debe usar la siguiente sintaxis:
```
CREATE TABLE nombre_tabla (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Question TEXT,
    Answer TEXT
);
```
Para consultar la base de datos, desde la ubicación del archivo `nombre_de_base_de_datos.db` se debe ejecutar el siguiente comando:
```
sqlite3 nombre_base_datos.db
```
- Ver tablas: `.tables`
- Ver estructura de una tabla: `.schema nombre_tabla`
- Ver información de tabla: `PRAGMA table_info(nombre_tabla);`
- Ver contenido de una tabla: `SELECT * FROM nombre_tabla;`
- Salir de la base de datos: `.exit` o `Ctrl + D`

## Para ejecutar la aplicación
- Activamos entorno virtual
    - El entorno debe tener `flask` instalado
```
python3 app.py
```
* Abre el puerto 5010. Se puede cambiar en `app.py`.