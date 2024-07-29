// pipeline {
//     agent any

//     environment {
//         REPO_URL = 'https://github.com/SaharGalimidi/world-of-games'
//         IMAGE_NAME = 'world-of-games'
//         BRANCH_NAME = 'main'
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 git url: "${REPO_URL}", branch: "${BRANCH_NAME}"
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     docker.build("${IMAGE_NAME}:latest")
//                 }
//             }
//         }

//         stage('Test') {
//             steps {
//                 script {
//                     docker.image("${IMAGE_NAME}:latest").inside {
//                         sh 'python e2e.py'
//                     }
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             echo 'Build completed.'
//         }
//         success {
//             echo 'The build and tests were successful.'
//         }
//         failure {
//             echo 'The build or tests failed.'
//         }
//     }
// }


pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/SaharGalimidi/world-of-games'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                checkout([$class: 'GitSCM', branches: [[name: "${BRANCH_NAME}"]], userRemoteConfigs: [[url: "${REPO_URL}"]]])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    apt-get update &&
                    apt-get install -y python3 python3-pip &&
                    pip3 install -r requirements.txt &&
                    cp Scores.txt /Scores.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'python3 e2e.py'  # Run tests as the root user
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
