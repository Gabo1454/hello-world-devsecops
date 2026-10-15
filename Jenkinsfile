pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'mvnw.cmd clean package -DskipTests'
            }
        }

        stage('Test') {
            steps {
                bat 'mvnw.cmd test'
            }
        }

        stage('Deploy') {
            steps {
                bat '"C:\\Users\\gaboa\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t hello-world-devsecops:latest .'
                bat '"C:\\Users\\gaboa\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f hello-world-devsecops-test'
                bat '"C:\\Users\\gaboa\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name hello-world-devsecops-test -p 8082:8080 hello-world-devsecops:latest'
            }
        }
    }
}
