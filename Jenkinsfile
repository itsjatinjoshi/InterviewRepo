pipeline {
    agent any

    stages {
        stage('Clone to custom directory') {
            steps {
                bat '''
                cd  C:\\Project
                git clone https://github.com/your-username/InterviewRepo.git
                '''
            }
        }

        stage('Create virtual environment') {
            steps {
                bat '''
                cd /d %WORKSPACE%
                if not exist venv (
                    python -m venv venv
                )
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                cd /d %WORKSPACE%\\venv\\Scripts
                call activate

                cd /d %WORKSPACE%
                python file.py
                '''
            }
        }
    }
}