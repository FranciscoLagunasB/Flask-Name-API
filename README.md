# Creación de API en Flask

Para este ejercicio, se espera que desarrolles un microservicio en Flask que permita buscar el nombre completo de una persona física en una 
tabla específica de una base de datos. El microservicio deberá recibir los siguientes parámetros de entrada en formato JSON:
 nombre: El nombre completo de la persona (nombre y apellidos).
• El microservicio deberá buscar en la base de datos si los parámetros enviados coinciden con alguna entrada en la tabla de personas. La búsqueda 
debe ser insensible a mayúsculas y minúsculas.
• El microservicio deberá devolver como respuesta un JSON que indique si la búsqueda fue exitosa o no. Por ejemplo:
 {
 "encontrado": true
 }
 o
 {
 "encontrado": false
 }
Además, se requiere mantener una bitácora de cada consulta que incluya la fecha en que se realizó la consulta, los parámetros enviados y la respuesta obtenida. Esta 
información se almacenará en una tabla de registro.

---

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Configuración del Entorno](#configuración-del-entorno)
3. [Ejecución](#ejecución)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Contribución](#contribución)
6. [Licencia](#licencia)

---

## Requisitos

- Python 3.x
- PostgreSQL (o cualquier otra base de datos compatible)

---

## Configuración del Entorno

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_proyecto.git
   cd tu_proyecto
   ```

2. **Instalar Dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la Base de Datos:**

   - Asegúrate de tener PostgreSQL instalado y configurado.
   - Modifica el archivo `config.py` con los datos de conexión correctos para tu base de datos.

4. **Variables de Entorno:**

   - Define las variables de entorno necesarias, como `FLASK_APP` y `FLASK_ENV`.
   
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```

5. **Inicializar la Base de Datos:**

   ```bash
   flask db upgrade
   ```

---

## Ejecución

1. **Ejecutar la Aplicación:**

   ```bash
   flask run
   ```

2. **Acceder a la Aplicación:**

   Abre un navegador web y visita `http://localhost:5000`.

---

## Estructura del Proyecto

- **`app/`**: Directorio que contiene la lógica de la aplicación.
  - **`db.py`**: Configuración de la base de datos.
  - **`models.py`**: Definición de los modelos de la base de datos.
  - **`routes.py`**: Definición de las rutas y controladores.
  - **`utils.py`**: Funciones de utilidad.
  - **`tests/`**: Directorio para las pruebas unitarias.

- **`venv/`**: Entorno virtual de Python.

- **`config.py`**: Archivo de configuración para la aplicación.

- **`requirements.txt`**: Lista de dependencias de Python.

- **`run.py`**: Punto de entrada principal de la aplicación.

- **`README.md`**: Documentación del proyecto.

---

## Contribución

- Para contribuir, sigue estos pasos:
  1. Haz un fork del repositorio.
  2. Crea una nueva rama (`git checkout -b feature/feature_name`).
  3. Realiza tus cambios y haz commit (`git commit -am 'Add some feature'`).
  4. Push a la rama (`git push origin feature/feature_name`).
  5. Crea un nuevo Pull Request.

---
