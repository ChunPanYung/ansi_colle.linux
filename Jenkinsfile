pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Ansible') {
            environment {
                ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
            }
            steps {
                ansibleAdhoc(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                    inventory: "jenkins ansible_connection=local", hosts: 'locahost',
                    moduleArguments: 'setup'
                )
            }
        }  // End stage('Ansible')

    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
