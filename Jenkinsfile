pipeline{
    agent any
    stages{
        stage("Clone the repo"){
            steps{
                sh "git clone https://github.com/itsjatinjoshi/InterviewRepo.git"
            }
        }
        stage("Execute the file.py file"){
            steps{
                REM Activate Python virtual environment and run file.py

                cd /d C:\Project\InterviewRepo\venv\Scripts
                call activate

                cd /d C:\Project\InterviewRepo
                python file.py
            }
        }
    }
}