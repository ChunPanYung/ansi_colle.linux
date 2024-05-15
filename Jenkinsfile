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
        string(name: 'ANSIBLE_RUN_TAGS', description: 'Ansible tags')
        choice(name: 'ANSIBLE_VERBOSITY', choices: [0, 10, 20, 30],
            description: 'Set verbose level on ansible output.'
        )
    }

    stages {
        stage('Ansible') {
            environment {
                // Setup Ansible Environment Variable
                ANSIBLE_LOAD_CALLBACK_PLUGINS = "True"
                ANSIBLE_STDOUT_CALLBACK = "yaml"
                ANSIBLE_RUN_TAGS = "${params.ANSIBLE_RUN_TAGS}"
                ANSIBLE_VERBOSITY = "${params.ANSIBLE_VERBOSITY}"
            }
            steps {
                ansiColor('xterm') {
                    ansiblePlaybook(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        inventory: '${ANSIBLE_INVENTORY_FILE}',
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
