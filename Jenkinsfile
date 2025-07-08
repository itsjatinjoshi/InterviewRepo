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
                        git pull
                    )
                '''
            }
        }

        stage('Create virtual environment') {
            steps {
                bat '''
                cd /d %PROJECT%
                if not exist venv (
                    python -m venv venv
                )
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                cd /d %PROJECT%\\venv\\Scripts
                call activate

                cd /d %PROJECT%
                python file.py
                '''
            }
        }
    }
}