pipeline{
    agent any{
    stages{
        stage("Clean up"){
            steps{
                echo " Cleaning up job. "
                //deleteDir()
            }
        }
    }
    stages{
        stage("Clone the repo"){
            steps{
            sh "git clone https://github.com/itsjatinjoshi/InterviewRepo.git"
            }
        }
    }
    }
}