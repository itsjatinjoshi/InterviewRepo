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
        string(name: 'branch', defaultValue: '*/master', description: 'Branch name')
        string(name: 'targetDir', defaultValue: 'InterviewRepo', description: 'relativeTargetDir')
        string(name: 'auth', defaultValue: '', description: 'Credentials ID for GitHub')
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
            script {
                def reportPath = "${params.targetDir}/sales_report.png"
    
                if (fileExists(reportPath)) {
                    emailext(
                        subject: "Jenkins Job '${env.JOB_NAME}' Succeeded",
                        body: """<p>The job <b>${env.JOB_NAME}</b> completed successfully.</p>
                                 <p>Python script output <code>sales_report.png</code> is attached.</p>""",
                        to: "your.email@example.com", // Change this
                        attachmentsPattern: reportPath,
                        mimeType: 'text/html'
                    )
                } else {
                    emailext(
                        subject: "Jenkins Job '${env.JOB_NAME}' completed (no report found)",
                        body: "The job ran, but 'sales_report.png' was not found.",
                        to: "your.email@example.com",
                        mimeType: 'text/plain'
                    )
                }
            }
        }
    }

    
}
