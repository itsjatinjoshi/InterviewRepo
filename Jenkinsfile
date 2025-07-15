// This is an Interview test for a Jenkins pipeline.
// The pipeline will clone a GitHub repository, run a Python script, and send an email notification.
// The pipeline should be parameterized to accept the repository URL, branch, and target directory.
// The pipeline should also handle errors gracefully and provide appropriate logging.
// The pipeline should use Groovy methods for better readability and maintainability.
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Python39\\python.exe' // Adjust this path to your Python installation
    }

    parameters {
        string(name: 'repo', defaultValue: '', description: 'GitHub repository URL')
        string(name: 'branch', defaultValue: '*/master', description: 'Branch name')
        string(name: 'targetDir', defaultValue: 'C:\\Project\\InterviewRepo', description: 'Target checkout directory')
        string(name: 'auth', defaultValue: '', description: 'GitHub credentials ID')
    }

    stages {

        stage('Clone Repo') {
            steps {
                script {
                    bat "git config --global --add safe.directory \"${params.targetDir}\""
                }

                checkout([
                    $class: 'GitSCM',
                    branches: [[name: params.branch]],
                    userRemoteConfigs: [[url: params.repo, credentialsId: params.auth]],
                    extensions: [
                        [$class: 'RelativeTargetDirectory', relativeTargetDir: params.targetDir]
                    ]
                ])
            }
        }

        stage('Run Python Script') {
            steps {
                dir(params.targetDir) {
                    bat """
                        ${env.PYTHON} -m venv venv
                        call venv\\Scripts\\activate.bat
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        python file.py
                    """
                }
            }
        }

        stage('Send Email Notification') {
            steps {
                echo 'TODO: Add email sending logic here.'
                // Use emailext once SMTP is configured
                // See earlier response for full example
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed."
            // Optionally send failure email here
        }
    }
}
