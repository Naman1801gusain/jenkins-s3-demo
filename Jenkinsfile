pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Python Script') {
            steps {
                script {
                    echo 'Handing over control to Python...'
                    // This command runs your Python script
                    sh 'python3 deploy.py'
                }
            }
        }
    }
}
