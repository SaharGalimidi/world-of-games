pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/SaharGalimidi/world-of-games/'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SaharGalimidi/world-of-games.git']])
            }
        }

        stage('Verify Docker Installation') {
            steps {
                script {
                    sh 'docker --version'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t world-of-games .'
                }
            }
        }


        stage('Test') {
            steps {
                script {
                    // Wait for the Flask app to be fully up and running
                    sleep 10
                    
                    // Run e2e.py inside the Flask app container and capture the exit status
                    def testResult = sh script: 'docker exec flask-app python3 e2e.py', returnStatus: true
                    if (testResult != 0) {
                        error('End-to-end tests failed.')
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Stop and remove the Flask app container
                    sh 'docker stop flask-app'
                    sh 'docker rm flask-app'
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
