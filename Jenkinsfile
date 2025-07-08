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