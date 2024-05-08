pipeline {
    agent { label 'python' }
    // parameters {}
    options {
        timeout(time: 1, unit: 'HOURS')
    }
    environment {
        ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
    }
    parameters {
        choice(name: 'PLAYBOOK', choices: ['install.yml', 'linux.yml'])
        string(name: 'TAGS', description: 'Ansible tags')
    }

    stages {
        stage('Ansible') {
            steps {
                sh """
                sha256sum ${env.ANSIBLE_INVENTORY_FILE}
                """
                ansiColor('xterm') {
                    ansibleAdhoc(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        colorized: true,
                        inventory: "${ANSIBLE_INVENTORY_FILE}",
                        tags: 'fedora',
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
