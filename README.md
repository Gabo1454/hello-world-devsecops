# Hello World DevSecOps

Proyecto de ejemplo desarrollado con Spring Boot para implementar un pipeline básico de integración y despliegue continuo (CI/CD) utilizando Jenkins, Maven y Docker.

## Descripción

La aplicación consiste en un servicio web sencillo que responde con un mensaje de bienvenida al acceder a la ruta raíz (`/`).

El objetivo principal es utilizar esta aplicación como base para practicar la automatización del ciclo de construcción, pruebas y despliegue mediante un pipeline definido en un archivo `Jenkinsfile`.

## Tecnologías utilizadas

- **Java 21:** lenguaje y entorno de ejecución.
- **Spring Boot:** desarrollo de la aplicación web.
- **Maven Wrapper:** compilación y ejecución de pruebas.
- **Git y GitHub:** control de versiones y almacenamiento del código fuente.
- **Jenkins:** ejecución del pipeline CI/CD.
- **Docker:** empaquetado y ejecución de la aplicación en un contenedor.

## Funcionamiento

El proyecto cuenta con tres etapas principales definidas en el archivo `Jenkinsfile`:

1. **Build:** compila el proyecto mediante Maven Wrapper y genera el archivo JAR.
2. **Test:** ejecuta las pruebas automatizadas disponibles en el proyecto.
3. **Deploy:** construye la imagen Docker y ejecuta un contenedor con la aplicación.

El pipeline se inicia manualmente desde Jenkins mediante la opción **Build Now**.

## Ejecución local

### 1. Requisitos

- Java 21.
- Git.
- Docker Desktop, si se desea ejecutar la aplicación en un contenedor.

### 2. Compilar el proyecto

En Windows, desde la raíz del repositorio, ejecutar:

```powershell
.\mvnw.cmd clean package
```

### 3. Ejecutar la aplicación

Después de compilar el proyecto, ejecutar:

```powershell
.\mvnw.cmd spring-boot:run
```

La aplicación estará disponible en:

http://localhost:8080/

## Ejecución mediante Docker y Jenkins

El pipeline utiliza el archivo `Dockerfile` para construir la imagen:

`hello-world-devsecops:latest`

Después, ejecuta el contenedor:

`hello-world-devsecops-test`

La configuración actual publica el puerto `8082` del equipo anfitrión y lo conecta con el puerto `8080` del contenedor.

Una vez finalizado el despliegue, la aplicación puede consultarse en:

http://localhost:8082/

Para ejecutar el pipeline, se debe acceder a Jenkins, seleccionar el trabajo configurado y pulsar **Build Now**.

## Estructura del proyecto

```text
hello-world-devsecops/
├── src/
│   ├── main/
│   │   └── java/
│   │       └── hello_world_devsecops/
│   └── test/
├── .gitignore
├── Dockerfile
├── Jenkinsfile
├── mvnw
├── mvnw.cmd
└── pom.xml
```

## Alcance y limitaciones

Este proyecto implementa un pipeline CI/CD básico para un entorno local de prueba.

- La ejecución del pipeline se inicia manualmente desde Jenkins.
- No se configuró un webhook para activar el pipeline automáticamente al actualizar GitHub.
- No se incorporaron herramientas específicas de análisis de vulnerabilidades.
- El despliegue se realiza localmente mediante Docker y no corresponde a un entorno productivo.

## Repositorio

https://github.com/Gabo1454/hello-world-devsecops

## Propósito educativo

El proyecto permite comprender la integración entre el control de versiones, la compilación automatizada, las pruebas y el despliegue mediante contenedores, como base para futuras implementaciones de DevSecOps.