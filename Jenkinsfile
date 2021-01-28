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
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                }
                sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F main.py'"

                sh 'python --version'
                sh 'python main.py'
            }

            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/main"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                    sh 'python --version'
                }
            }
        }
    }
}
