pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/SaharGalimidi/world-of-games'
        IMAGE_NAME = 'world-of-games'
        BRANCH_NAME = 'main'
    }

    triggers {
        pollSCM('H/5 * * * *')  // Poll the repository every 5 minutes
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${REPO_URL}", branch: "${BRANCH_NAME}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:latest").inside {
                        sh 'python e2e.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Build completed.'
        }
        success {
            echo 'The build and tests were successful.'
        }
        failure {
            echo 'The build or tests failed.'
        }
    }
}
