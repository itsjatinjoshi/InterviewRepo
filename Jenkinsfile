pipeline {
    agent any
    stages {
        stage("Clone the repo") {
            steps {
                // If Jenkins is already set to clone from SCM, this is optional
                bat 'git config --global --add safe.directory "*"'
            }
        }

        stage("Execute the file.py file") {
            steps {
                bat '''
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
