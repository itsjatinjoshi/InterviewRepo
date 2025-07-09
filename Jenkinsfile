pipeline {
    agent any {
        // Set custom workspace location
        customWorkspace 'C:\\Project'
    }

    environment {
        // Define the Python executable path explicitly if needed
        PYTHON = 'C:\\Users\\Jatin\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'
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

        stage('Install Dependencies') {
            steps {
                bat '''
                cd C:\\Project\\InterviewRepo
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Python File') {
            steps {
                bat '''
                cd C:\\Project\\InterviewRepo
                call venv\\Scripts\\activate.bat
                python file.py
                '''
            }
        }
    }
}
