pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Checkout') {
            steps {
                deleteDir()
                echo env.BRANCH_NAME
                checkout scmGit(
                    branches: [[name: "${env.BRANCH_NAME}"]],
                    extension: [cloneOption(shallow: true)],
                    userRemoteConfig: [
                        [url: 'https://github.com/ChunPanYung/ansi_colle-linux.git']
                    ]
                )
            }
        }  // Eng stage('Checkout')
        stage('Process') {
            steps {
                sh 'ls -la'
            }
        }  // Eng stage('Process')

    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
