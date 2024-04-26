pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Checkout') {
            steps{
                deleteDir()
                checkout scmGit(
                    branches: [[name: env.BRANCH_NAME]],
                    extension: [cloneOption(shallow: true)],
                    userRemoteConfig: [
                        [url: 'https://github.com/ChunPanYung/ansi_colle-linux.git']
                    ]
                )
            }
        }

        stage('Process') {
            sh 'ls -la'
        }
    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
