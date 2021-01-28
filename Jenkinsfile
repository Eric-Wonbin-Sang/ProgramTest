pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.5.1'
                }
            }
            steps {
                sh 'python -m py_compile sources/main.py'
                stash(name: 'compiled-results', includes: 'sources/main.py')
            }
        }
        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'python:3.5.1'
            }

            steps {
                sh 'python --version'
                sh 'python main.py'
            }
        }
    }
}
