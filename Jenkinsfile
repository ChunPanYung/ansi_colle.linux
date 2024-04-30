pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Ansible') {
            environment {
                ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
                ANSIBLE_SSH_PRIVATE_KEY = credentials('ANSIBLE_SSH_PRIVATE_KEY')
            }
            steps {
                ansiColor('xterm') {
                    ansibleAdhoc(credentialsId: 'ANSIBLE_SSH_PRIVATE',
                        colorized: true,
                        inventory: "${env.ANSIBLE_INVENTORY_FILE}",
                        becomeUser: 'infinite4ever'
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
