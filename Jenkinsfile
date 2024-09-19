// Windows
pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'ivgiko'
        DOCKER_PASSWORD = 'dckr_pat_R85kHUzF2Wz_J0yuXYTAmGurJLQ'
    }

    stages {
        stage('Checkout Repository') {
            steps {
                git url: 'https://github.com/Ivgiko/WorldOfGames.git', branch: 'main'
            }
        }
        
        stage('Build and Run Docker Container') {
            steps {
                script {
                    bat 'docker-compose up --build -d'
                }
            }
        }

        stage('Test with e2e.py') {
            steps {
                script {
                    def result = bat(script: 'docker-compose run web python /app/tests/e2e.py', returnStatus: true)

                    if (result == -1) {
                        error "e2e.py returned -1, failing the pipeline."
                    }
                }
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                script {
                    // Login to DockerHub
                    bat "docker login -u ${env.DOCKER_USERNAME} -p ${env.DOCKER_PASSWORD}"
                    
                    // Tag and push the Docker image
                    bat 'docker tag worldofgames4-web:latest ivgiko/worldofgames4-web:latest'
                    bat 'docker push ivgiko/worldofgames4-web:latest'
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    bat 'docker-compose down'
                }
            }
        }
    }
}




 // macOS/Linux
 /*
pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'ivgiko'
        DOCKER_PASSWORD = 'dckr_pat_R85kHUzF2Wz_J0yuXYTAmGurJLQ'
    }

    stages {
        stage('Checkout Repository') {
            steps {
                git url: 'https://github.com/Ivgiko/WorldOfGames.git', branch: 'main'
            }
        }
        
        stage('Build and Run Docker Container') {
            steps {
                script {
                    sh 'docker-compose up --build -d'
                }
            }
        }

        stage('Test with e2e.py') {
            steps {
                script {
                    def result = sh(script: 'docker-compose run web python /app/tests/e2e.py', returnStatus: true)

                    if (result == -1) {
                        error "e2e.py returned -1, failing the pipeline."
                    }
                }
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                script {
                    sh "docker login -u ${env.DOCKER_USERNAME} -p ${env.DOCKER_PASSWORD}"
                    sh 'docker tag worldofgames4-web:latest ivgiko/worldofgames4-web:latest'
                    sh 'docker push ivgiko/worldofgames4-web:latest'
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }
}
*/
