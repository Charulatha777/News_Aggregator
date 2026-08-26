pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker build -t news-aggregator-test .
                    docker run --rm news-aggregator-test python -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t news-aggregator:latest .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f news-test || true
                    docker run -d --name news-test news-aggregator:latest
                '''
            }
        }

        stage('Test Container') {
            steps {
                sh '''
                    sleep 5
                    docker exec news-test python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:5000/health').read().decode())"
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                    docker rm -f news-test || true
                '''
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }

        failure {
            echo 'CI Pipeline failed!'
        }
    }
}