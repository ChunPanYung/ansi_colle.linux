pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Ansible') {
            environment {
                ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
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
