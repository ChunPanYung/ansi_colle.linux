pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Test') {
            steps{
                // git branch: "${params.BRANCH}",
                //     url: 'https://github.com/ChunPanYung/ansi_colle-linux.git'
                echo "hello world!"
                echo env.BRANCH_NAME
            }
        }
    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
