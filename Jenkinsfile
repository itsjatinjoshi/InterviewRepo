pipeline {
    agent any

    stages {
        stage('Trust Git Directory') {
            steps {
                bat 'git clone https://github.com/itsjatinjoshi/InterviewRepo.git'
            }
        }

         stage("Execute the file.py file") {
            steps {
                bat '''
                REM Mark repo as safe to prevent Git security warning
                git config --global --add safe.directory C:/Project/InterviewRepo

                REM Change to script directory and pull latest changes
                cd /d C:\\Project\\InterviewRepo
                git pull

                REM Activate virtual environment
                call venv\\Scripts\\activate

                REM Run Python script
                python file.py
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Script or Git operation failed.'
        }
        success {
            echo '✅ Successfully ran the Python script.'
        }
    }
}
