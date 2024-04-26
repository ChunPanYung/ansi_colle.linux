pipeline {
    agent { label 'python' }
    parameters {
        gitParameter branchFilter: 'origin/(.*)', defaultValue: 'main',
            name: 'BRANCH', type: 'PT_BRANCH'
    }
    stages {
        stage('Test') {
            steps{
                git branch: "${params.BRANCH}",
                    url: 'https://github.com/ChunPanYung/ansi_colle-linux.git'
            }
        }
    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
