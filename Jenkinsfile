pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Process') {
            steps {
                sh 'ls -la'
                sh '''
                echo $USER
                ansible --version
                sh echo $PATH
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
