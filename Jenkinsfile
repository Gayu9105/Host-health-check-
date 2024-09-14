pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Create and activate a virtual environment
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install psutil requests
                    '''
                }
            }
        }

        stage('Run Host Health Check') {
            steps {
                script {
                    // Run the health check script
                    sh '''
                        . venv/bin/activate
                        python host_health_check.py > health_check_results.txt
                        cat health_check_results.txt
                    '''
                }
            }
        }
    }

    post {
        always {
            // Archive the results
            archiveArtifacts artifacts: 'health_check_results.txt', fingerprint: true

            // Clean up the virtual environment
            sh 'rm -rf venv'
        }
        success {
            echo 'Host health check completed successfully!'
        }
        failure {
            echo 'Host health check failed. Please check the results.'
        }
    }
}
