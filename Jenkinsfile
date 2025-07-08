pipeline {
    agent any

    stages {
        stage('Clone to custom directory') {
            steps {
                bat '''
                if not exist C:\\Project\\InterviewRepo (
                    git clone https://github.com/your-username/InterviewRepo.git C:\\Project\\InterviewRepo
                ) else (
                    cd C:\\Project\\InterviewRepo
                    git pull
                )
                '''
            }
        }

        stage('Run script using existing venv') {
            steps {
                bat '''
                cd /d C:\\Project\\InterviewRepo\\venv\\Scripts
                call activate

                cd /d C:\\Project\\InterviewRepo
                python file.py
                '''
            }
        }
    }
}