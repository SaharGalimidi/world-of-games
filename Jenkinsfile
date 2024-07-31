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

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Start Service') {
            steps {
                sh '''
                    echo "Starting Flask service..."
                    nohup python3 main.py &
                    sleep 10
                    echo "Flask service started"
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'python3 e2e.py'  // Run tests as the root user
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
