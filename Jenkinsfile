pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Process') {
            steps {
                sh 'ls -la'
                sh '''
                echo $USER
                echo $PATH
                ls /usr/local/bin
                ls ~/.local/bin
                ansible --version
                '''
            }
        }  // Eng stage('Process')

    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
