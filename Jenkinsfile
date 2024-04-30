pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Prepare inventories') {
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
        stage('Ansible') {
            environment {
                ANSIBLE_INVENTORY_FILE = credentials 'hosts.cfg'
            }
            steps {
                echo "Path is: ${env.ANSIBLE_INVENTORY_FILE}"
            }
        }  // End stage('Ansible')

    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
