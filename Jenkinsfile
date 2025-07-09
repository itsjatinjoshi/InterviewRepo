pipeline {
    agent any {
        customWorkspace 'C:\\Project'
    }

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
        stage('Activate Virtual Environment') {
            steps {
                bat '''
                cd C:\\Project\\InterviewRepo
                call venv\\Scripts\\activate.bat
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install necessary Python packages
                    bat "pip install -r requirements.txt"
                }
            }
        }
        stage('Run Python File') {
            steps {
                script {
                    cd C:\\Project\\InterviewRepo
                    "%PYTHON%" file.py
                }
            }
        }
    }
}