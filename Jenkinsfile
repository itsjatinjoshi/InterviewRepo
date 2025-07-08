pipeline {
    agent any

    stages {
        stage('Trust Git Directory') {
            steps {
                bat 'git config --system --add safe.directory "C:/Project/InterviewRepo"'
            }
        }

        stage('Run Python Script') {
            steps {
                bat '''
                cd /d C:\\Project\\InterviewRepo
                python file.py
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Something went wrong. Check the logs.'
        }
    }
}
