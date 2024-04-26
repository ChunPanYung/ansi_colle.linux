pipeline {
    agent { label 'python' }
    stages {
        stage('Test') {
            steps{
                sh 'echo hello world!'
            }
        }
    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
