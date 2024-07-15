// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://your-repository-url.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("world-of-games:latest")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    dockerImage.inside("--network host") {
                        sh 'docker-compose up -d'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python e2e.py'
                    } catch (Exception e) {
                        error("Tests failed")
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }
}
