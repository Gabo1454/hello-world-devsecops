
# Hello World DevSecOps

Proyecto de ejemplo para practicar integración y despliegue continuo (CI/CD) utilizando Jenkins, GitHub, Maven, Docker y herramientas de seguridad para la gestión de dependencias.

El repositorio contiene dos proyectos de ejemplo desarrollados en actividades diferentes: una aplicación Spring Boot en Java y una aplicación Flask en Python.

## Descripción

El objetivo del repositorio es practicar la automatización del ciclo de desarrollo de software, incluyendo la compilación, las pruebas automatizadas, el análisis de dependencias y la construcción de imágenes Docker.

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
- **Jenkins:** ejecución automatizada de las etapas del pipeline.
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

En esta actividad se configuró un pipeline de Jenkins para automatizar la gestión de dependencias y realizar comprobaciones de seguridad en una aplicación Flask desarrollada en Python.

El proyecto se encuentra en la carpeta `flask-vulnerable/` y utiliza Pipenv para administrar las dependencias y mantener el archivo `Pipfile.lock`.

El pipeline se configuró mediante el archivo `flask-vulnerable/Jenkinsfile` y se organizó en cinco etapas:

1. **Build:** prepara el entorno Python, instala Pipenv y verifica el archivo de bloqueo de dependencias.
2. **Test:** instala las dependencias necesarias y ejecuta las pruebas unitarias automatizadas.
3. **Analyze:** utiliza `pip-audit` para buscar vulnerabilidades conocidas en las dependencias analizadas y verifica el estado del archivo de bloqueo.
4. **Dependency Management:** sincroniza las dependencias definidas en Pipenv y comprueba que el archivo de bloqueo esté actualizado.
5. **Deploy:** construye la imagen Docker de la aplicación Flask.

#### Resultados obtenidos

La ejecución del pipeline finalizó correctamente con el estado `Finished: SUCCESS`.

- Las pruebas unitarias finalizaron correctamente.
- `pip-audit` informó `No known vulnerabilities found` para las dependencias analizadas.
- Pipenv verificó y sincronizó las dependencias del proyecto.
- Docker construyó correctamente la imagen `flask-vulnerable:latest`.

El resultado del análisis se limita a las dependencias revisadas y no representa una auditoría completa de la aplicación.

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

http://localhost:8080/

## Ejecución del pipeline en Jenkins

Para ejecutar los pipelines, se debe acceder a Jenkins, seleccionar el trabajo correspondiente y utilizar la opción **Build Now**.

Para la actividad 3.3.2, el trabajo configurado es `dependencias-seguras`.

El pipeline de Flask construye la imagen Docker `flask-vulnerable:latest`. La construcción de esta imagen se verificó correctamente, pero esto no implica que el contenedor haya sido ejecutado ni que el despliegue de la aplicación se haya comprobado.

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
│   └── Jenkinsfile
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
- El análisis de `pip-audit` se limita a las dependencias que se le indicaron.
- La construcción de una imagen Docker no garantiza por sí sola que la aplicación se ejecute correctamente.
- Los proyectos están orientados a prácticas educativas y pruebas en un entorno local, no a un entorno productivo.

## Repositorio

https://github.com/Gabo1454/hello-world-devsecops

## Propósito educativo

Este repositorio permite practicar la integración entre control de versiones, automatización de compilaciones, pruebas unitarias, gestión de dependencias, análisis de vulnerabilidades conocidas y construcción de imágenes Docker, incorporando progresivamente buenas prácticas de DevSecOps.
