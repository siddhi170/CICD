pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/siddhi170/CICD.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build & Test') {
            steps {
                sh '''
                source venv/bin/activate
                # Optional: add pytest for testing
                echo "Running Flask App"
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                source venv/bin/activate
                nohup python3 app.py &
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed. Check logs.'
        }
    }
}
