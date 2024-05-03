pipeline {
    agent { label 'python' }
    // parameters {}
    stages {
        stage('Ansible') {
            environment {
                ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
            }
            steps {
                sh """
                sha256sum ${env.ANSIBLE_INVENTORY_FILE}
                """
                ansiColor('xterm') {
                    ansibleAdhoc(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        colorized: true,
                        hostKeyChecking: false,
                        inventory: "${ANSIBLE_INVENTORY_FILE}",
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
