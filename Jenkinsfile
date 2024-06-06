pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning The Code From GitHub'
                deleteDir() // Clean up the workspace before cloning
                withCredentials([string(credentialsId: 'GitHub', variable: 'GITHUB_TOKEN')]) {
                    sh 'git clone https://$GITHUB_TOKEN@github.com/Pradip-web-Bariflolabs/Aqua-culture_IOT_Dashboard.git'
                    dir('Aqua-culture_IOT_Dashboard') {
                        sh 'git checkout main'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building The Image'
                dir('Aqua-culture_IOT_Dashboard') {
                    sh 'docker build -t aqua .'
                }
            }
        }

        stage('Push To DockerHub') {
            steps {
                echo 'Pushing The Image To DockerHub'
                withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPass', usernameVariable: 'dockerHubUser')]) {
                    sh '''
                        #!/bin/bash
                        echo "$dockerHubPass" | docker login -u "$dockerHubUser" --password-stdin
                        docker tag aqua ${dockerHubUser}/aqua:latest
                        docker push ${dockerHubUser}/aqua:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying The Container'
                dir('Aqua-culture_IOT_Dashboard') {
                    sh 'docker-compose down && docker-compose up -d'
                }
            }
        }
    }
}
