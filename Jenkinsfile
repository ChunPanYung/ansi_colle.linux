pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Ansible') {
            environment {
                ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
            }
            steps {
                ansiColor('xterm') {
                    ansibleAdhoc(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        colorized: true,
                        inventoryContent: '''
                        [linux]
                        localhost ansible_connection=local
                        ''',
                        hosts: 'linux',
                        module: 'setup'
                    )
                }
            }
        }  // End stage('Ansible')

    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
