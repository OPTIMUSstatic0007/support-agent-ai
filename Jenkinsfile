pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        VENV = ".venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                bat '''
                python --version
                pip --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                python -m venv %VENV%
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Validate Source') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                python -m compileall app
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }

        always {
            cleanWs()
        }
    }
}