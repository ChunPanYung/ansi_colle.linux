pipeline {
    agent { label 'python' }
    // parameters {}
    options {
        timeout(time: 1, unit: 'HOURS')
    }
    environment {
        ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
        ANSIBLE_SSH_PRIVATE_KEY = credentials('ANSIBLE_SSH_PRIVATE_KEY')
    }
    parameters {
        choice(name: 'PLAYBOOK', choices: ['install.yml', 'linux.yml'])
        string(name: 'TAGS', description: 'Ansible tags')
        choice(name: 'VERBOSITY', choices: [0, 1, 2, 3],
            description: 'Set verbose level on ansible output.'
        )
    }

    stages {
        stage('Ansible') {
            steps {
                ansiColor('xterm') {
                    ansiblePlaybook(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        inventory: 'ANSIBLE_INVENTORY_FILE',
                        playbook: 'playbooks/install.yml',
                        colorized: true,
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
