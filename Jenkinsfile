pipeline {
    agent { label 'python' }
    parameters {
        choice(name: 'PLAYBOOK', choices: ['ansi_colle.mods.ping',
            'ansi_colle.linux.wsl', 'ansi_colle.mods.linux'
        ])
        string(name: 'ANSIBLE_RUN_TAGS', description: 'Ansible tags')
        choice(name: 'ANSIBLE_VERBOSITY', choices: [0, 10, 20, 30],
            description: 'Set verbose level on ansible output.'
        )
    }

    options {
        timeout(time: 1, unit: 'HOURS')
    }

    environment {
        ANSIBLE_INVENTORY_FILE = credentials('LINUX_INVENTORY_FILE')
        ANSIBLE_SSH_PRIVATE_KEY = credentials('ANSIBLE_SSH_PRIVATE_KEY')

        ANSIBLE_LOAD_CALLBACK_PLUGINS = "True"
        ANSIBLE_STDOUT_CALLBACK = "yaml"
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    stages {
        stage('Install Ansible Collections') {
            steps {
                ansiColor('xterm') {
                    ansiblePlaybook(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        colorized: true,
                        inventoryContent: 'localhost ansible_connection=local',
                        playbook: 'playbooks/install.yml'
                    )
                }
            }
        }  // End stage('Install Ansible Collections')

        stage('Execute Ansible Collections') {
            environment {
                // Setup Ansible Environment Variable
                ANSIBLE_RUN_TAGS = "${params.ANSIBLE_RUN_TAGS}"
                ANSIBLE_VERBOSITY = "${params.ANSIBLE_VERBOSITY}"
            }
            steps {
                ansiColor('xterm') {
                    ansiblePlaybook(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        colorized: true,
                        inventory: '${ANSIBLE_INVENTORY_FILE}',
                        playbook: "${params.PLAYBOOK}"
                    )
                }
            }
        } // End stage('Execute Ansible Collections')
    }  // End stages
    post {
        always {
            echo 'End of Jenkins Job.'
        }
    }
}
