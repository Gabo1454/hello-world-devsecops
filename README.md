# Hello World DevSecOps

Proyecto de ejemplo para practicar integración y despliegue continuo (CI/CD) utilizando Jenkins, GitHub, Maven, Docker y herramientas de seguridad para la gestión de dependencias.

El repositorio contiene dos proyectos de ejemplo desarrollados en actividades diferentes: una aplicación Spring Boot en Java y una aplicación Flask en Python.

## Descripción

El objetivo del repositorio es practicar la automatización del ciclo de desarrollo de software, incluyendo la compilación, las pruebas automatizadas, el análisis de dependencias, la documentación técnica y la construcción de imágenes Docker.

## Tecnologías utilizadas

### Proyecto Spring Boot

- **Java 21:** lenguaje y entorno de ejecución.
- **Spring Boot:** desarrollo de la aplicación web.
- **Maven Wrapper:** compilación y ejecución de pruebas.
- **Docker:** empaquetado de la aplicación.
- **Jenkins:** automatización del pipeline CI/CD.
- **Git y GitHub:** control de versiones.

### Proyecto Flask

- **Python:** lenguaje de programación.
- **Flask:** desarrollo de la aplicación web.
- **Pipenv:** administración de entornos virtuales y dependencias.
- **Pipfile y Pipfile.lock:** definición y bloqueo de dependencias.
- **pip-audit:** análisis de dependencias en busca de vulnerabilidades conocidas.
- **Doxygen:** generación automática de documentación técnica.
- **Jenkins:** automatización de las etapas del pipeline.
- **Docker:** construcción de la imagen de la aplicación.

## Actividades desarrolladas

### 1. Pipeline CI/CD con Spring Boot

Se implementó un pipeline básico en Jenkins para automatizar la compilación, las pruebas y la construcción y ejecución de la aplicación mediante Docker.

Las etapas principales son:

1. **Build:** compila el proyecto mediante Maven Wrapper y genera el archivo JAR.
2. **Test:** ejecuta las pruebas automatizadas.
3. **Deploy:** construye la imagen Docker y ejecuta un contenedor con la aplicación.

El proyecto utiliza el archivo `Jenkinsfile` para definir las etapas del pipeline.

La aplicación Spring Boot se ejecuta localmente en el puerto 8080. En la configuración original de Docker, se utiliza el puerto 8082 del equipo anfitrión para acceder al contenedor.

### 2. Actividad 3.3.2: Dependencias y actualizaciones seguras

En esta actividad se trabajó en la gestión de dependencias y las comprobaciones de seguridad de una aplicación Flask desarrollada en Python.

El proyecto se encuentra en la carpeta `flask-vulnerable/` y utiliza Pipenv para administrar las dependencias y mantener el archivo `Pipfile.lock`.

Se incorporaron las siguientes herramientas y configuraciones:

- **Pipenv:** administración de dependencias y entornos virtuales.
- **Pipfile.lock:** bloqueo de versiones para mantener instalaciones reproducibles.
- **pip-audit:** análisis de dependencias en busca de vulnerabilidades conocidas.
- **Pruebas unitarias:** comprobación del funcionamiento del endpoint `/hello`.
- **Doxygen:** generación de documentación técnica a partir del código fuente y sus comentarios.

#### Configuración del pipeline Jenkins

El pipeline se definió en `flask-vulnerable/Jenkinsfile` y contempla cinco etapas:

1. **Build:** prepara el entorno Python, instala Pipenv y verifica el archivo de bloqueo de dependencias.
2. **Dependency Management:** sincroniza las dependencias definidas en `Pipfile.lock`, incluyendo las dependencias de desarrollo, y verifica su consistencia.
3. **Test:** ejecuta las pruebas unitarias automatizadas mediante `unittest`.
4. **Analyze:** utiliza `pip-audit` para analizar las dependencias instaladas en el entorno de Pipenv.
5. **Deploy:** construye la imagen Docker de la aplicación Flask.

#### Documentación técnica con Doxygen

Se incorporó Doxygen para generar documentación técnica del proyecto.

Los principales archivos incorporados fueron:

- `Doxyfile`: archivo de configuración de Doxygen.
- `mainpage.dox`: contenido de la página principal de la documentación.
- `test_app.py`: incorpora comentarios estructurados para documentar el módulo, la clase y los métodos de prueba.
- `Jenkinsfile-docs.txt`: archivo adicional relacionado con la configuración de documentación.

La documentación generada se encuentra en:

- `docs/html/`: documentación navegable mediante un navegador web.
- `docs/latex/`: documentación en formato LaTeX.

#### Resultados obtenidos

Las comprobaciones realizadas localmente finalizaron correctamente:

- Las pruebas unitarias de Flask se ejecutaron correctamente mediante `python -m unittest -v`.
- Pipenv verificó la consistencia del archivo de bloqueo y sincronizó las dependencias.
- `pip-audit` informó `No known vulnerabilities found` para las dependencias analizadas.
- Doxygen generó correctamente los directorios de documentación HTML y LaTeX.
- Docker construyó correctamente la imagen `flask-vulnerable:latest`.

**Estado de validación:** las comprobaciones anteriores se realizaron localmente. La ejecución integral del pipeline en Jenkins queda pendiente de validación.

El resultado de `pip-audit` se limita a las dependencias revisadas y no representa una auditoría completa de la aplicación.

## Ejecución local del proyecto Spring Boot

### Requisitos

- Java 21.
- Git.
- Docker Desktop, si se desea ejecutar la aplicación en un contenedor.

### Compilar el proyecto

Desde la raíz del repositorio, ejecutar en Windows:

```powershell
.\mvnw.cmd clean package
```

### Ejecutar la aplicación

```powershell
.\mvnw.cmd spring-boot:run
```

La aplicación estará disponible en:

[http://localhost:8080/](http://localhost:8080/)

## Ejecución local del proyecto Flask

### Requisitos

- Python 3.14.
- Pipenv.
- Docker Desktop, si se desea construir la imagen.
- Doxygen, si se desea generar la documentación.

### Instalar dependencias

Desde la carpeta `flask-vulnerable/`:

```powershell
python -m pipenv sync --dev
```

### Ejecutar pruebas unitarias

```powershell
python -m pipenv run python -m unittest -v
```

### Analizar dependencias

```powershell
python -m pipenv run pip-audit
```

### Generar documentación

```powershell
doxygen Doxyfile
```

La documentación HTML se genera en `docs/html/`. Para visualizarla, abrir `docs/html/index.html` en un navegador.

### Construir imagen Docker

```powershell
docker build -t flask-vulnerable:latest .
```

Para comprobar que la imagen existe:

```powershell
docker images flask-vulnerable
```

## Ejecución del pipeline en Jenkins

Para ejecutar los pipelines, se debe acceder a Jenkins, seleccionar el trabajo correspondiente y utilizar la opción **Build Now**.

Para la actividad 3.3.2, el trabajo asociado es `dependencias-seguras`.

El pipeline de Flask está definido en `flask-vulnerable/Jenkinsfile` y contempla la instalación y verificación de dependencias, las pruebas unitarias, el análisis de seguridad y la construcción de la imagen Docker.

La construcción de la imagen se verificó localmente. La ejecución completa de este pipeline en Jenkins está pendiente de validación.

## Estructura del repositorio

```text
hello-world-devsecops/
├── src/
│   ├── main/
│   └── test/
├── flask-vulnerable/
│   ├── app.py
│   ├── test_app.py
│   ├── requirements.txt
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── Dockerfile
│   ├── Jenkinsfile
│   ├── Jenkinsfile-docs.txt
│   ├── Doxyfile
│   ├── mainpage.dox
│   ├── .gitignore
│   └── docs/
│       ├── html/
│       └── latex/
├── .gitignore
├── Dockerfile
├── Jenkinsfile
├── mvnw
├── mvnw.cmd
└── pom.xml
```

## Alcance y limitaciones

- Los pipelines se ejecutan manualmente desde Jenkins.
- No se configuró un webhook para activar automáticamente el pipeline al actualizar GitHub.
- El análisis de `pip-audit` se limita a las dependencias instaladas y analizadas.
- La construcción de una imagen Docker no garantiza por sí sola que la aplicación se ejecute correctamente.
- La generación de documentación con Doxygen depende de los comentarios y configuraciones incorporados al proyecto.
- La ejecución integral del pipeline de la actividad 3.3.2 en Jenkins está pendiente de validación.
- Los proyectos están orientados a prácticas educativas y pruebas en un entorno local, no a un entorno productivo.

## Repositorio

[https://github.com/Gabo1454/hello-world-devsecops](https://github.com/Gabo1454/hello-world-devsecops)

## Propósito educativo

Este repositorio permite practicar la integración entre control de versiones, automatización de compilaciones, pruebas unitarias, gestión de dependencias, análisis de vulnerabilidades conocidas, documentación técnica y construcción de imágenes Docker, incorporando progresivamente buenas prácticas de DevSecOps.