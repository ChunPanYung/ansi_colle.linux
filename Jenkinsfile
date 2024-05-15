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
        choice(name: 'VERBOSITY', choices: ['', '-v', '-vv', '-vvv'],
            description: '''Set verbose level on ansible output.
                Default is no verbosity.
            '''
        )
    }

    stages {
        stage('Ansible') {
            environment {
                ANSIBLE_TAGS = "${params.TAGS}"
                ANSIBLE_VERBOSITY = "${params.VERBOSITY}"
            }
            steps {
                ansiColor('xterm') {
                    ansiblePlaybook(credentialsId: 'ANSIBLE_SSH_PRIVATE_KEY',
                        inventory: '${ANSIBLE_INVENTORY_FILE}',
                        playbook: 'playbooks/install.yml',
                        tags: "${env.ANSIBLE_TAGS}",
                        colorized: true,
                        // extras: "${env.ANSIBLE_VERBOSITY}"
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
