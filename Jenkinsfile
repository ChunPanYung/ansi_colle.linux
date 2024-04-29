pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Process') {
            steps {
                sh 'ls -la'
                sh 'ansible --version'
            }
        }  // Eng stage('Process')

    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
