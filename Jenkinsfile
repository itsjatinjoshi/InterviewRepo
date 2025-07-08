pipeline{
    agent any{
    stages{
        stage("Clean up"){
            steps{
                echo "Cleaning up job. "
                deleteDir()
            }
        }
        stage("Clone the repo"){
            steps{
                sh "git clone https://github.com/itsjatinjoshi/InterviewRepo.git"
            }
        }
        stage("Execute the file.py file"){
            steps{
                sh "python file.py"
            }
        }
    }
    }
}