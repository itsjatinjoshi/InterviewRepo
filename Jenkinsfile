pipeline {
    agent any

    stages {
        stage('Clone to custom directory') {
            steps {
                bat '''
                    cd C:\\Project
                    if not exist InterviewRepo (
                        git clone https://github.com/your-username/InterviewRepo.git
                    ) else (
                        cd InterviewRepo
                        git config --global --add safe.directory C:/Project/InterviewRepo
                        git pull
                    )
                '''
            }
        }
        stage('Create virtual environment') {
            steps {
                bat '''
                cd C:\\Project\\InterviewRepo
                if not exist venv (
                    "%PYTHON%" -m venv venv
                )
                '''
            }
        }
        stage('Install dependencies') {
            steps {
                bat '''
                cd C:\\Project\\InterviewRepo
                call venv\\Scripts\\activate.bat

                cd C:\\Project\\InterviewRepo
                "%PYTHON%" file.py
                '''
            }
        }
    }
}