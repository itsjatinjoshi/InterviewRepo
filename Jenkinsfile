// This is an Interview test for a Jenkins pipeline.
// The pipeline will clone a GitHub repository, run a Python script, and send an email notification.
// The pipeline should be parameterized to accept the repository URL, branch, and target directory.
// The pipeline should also handle errors gracefully and provide appropriate logging.
// The pipeline should use Groovy methods for better readability and maintainability.
pipeline {
    agent any

// Define the parameters for the pipeline here
    parameters {
        string(name: 'repo', defaultValue: '', description: 'GitHub repository URL')
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: params.branch]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [
                        [$class: 'CloneOption', depth: 0, noTags: false, reference: '', shallow: false, timeout: 6000],
                        [$class: 'RelativeTargetDirectory', relativeTargetDir: params.targetDir],
                        [$class: 'CheckoutOption', timeout: 6000],
                        [$class: 'PruneStaleBranch'],
                        [$class: 'AuthorInChangelog'],
                        [$class: 'GitLFSPull']
                    ],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: params.repo, credentialsId: params.auth]]
                ])
            }
        }


// Run the python script in virtual environment
// make sure to use requirements.txt to install dependencies

        stage('Run Python Script') {
            steps {
                dir(params.targetDir) {
                    bat '''
                    "%PYTHON%" -m venv venv
                    call venv\\Scripts\\activate.bat

                    pip install --upgrade pip
                    pip install -r requirements.txt

                    "%PYTHON%" file.py

                    echo 'TODO: Implement script execution here.'
                    '''
                }
            }
        }

// check the result of pipeline and send email notification 
// use Gmail SMTP server for sending email
// attach the result of python script and pipeline logs to the email
        stage('Send Email Notification') {
            steps {
                echo 'TODO: Add email sending logic here.'
            }
        }
    }

    
}
