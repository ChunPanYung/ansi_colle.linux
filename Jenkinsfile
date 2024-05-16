pipeline {
    agent { label 'python' }
    parameters {
        choice(name: 'PLAYBOOK', choices: ['ansi_colle.linux.linux',
            'ansi_colle.linux.wsl', 'ansi_colle.mods.ping'
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
        ANSIBLE_INVENTORY_FILE = credentials('ANSIBLE_INVENTORY')
        ANSIBLE_SSH_PRIVATE_KEY = credentials('ANSIBLE_SSH_PRIVATE_KEY')

        ANSIBLE_LOAD_CALLBACK_PLUGINS = "True"
        ANSIBLE_STDOUT_CALLBACK = "yaml"
    }

    stages {
        stage('Install Ansible Collections') {
            steps {
                ansiColor('xterm') {
                    ansiblePlaybook(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        colorized: true,
                        inventory: '${ANSIBLE_INVENTORY_FILE}',
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
                sh 'cat ${env.ANSIBLE_SSH_PRIVATE_KEY}'
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
