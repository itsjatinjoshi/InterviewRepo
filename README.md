# Jenkins Pipeline Interview Test

This repository contains files for a Jenkins pipeline interview test. The goal is to implement a Jenkins pipeline that clones a GitHub repository, runs a Python script, and sends an email notification. The pipeline should handle errors gracefully and provide appropriate logging.

## Files Included

1. **`pipeline.Jenkinsfile`**  
   - A Jenkins pipeline script that defines the stages for cloning a repository, running a Python script, and sending an email notification.
   - The pipeline is parameterized to accept the following inputs:
     - `repo`: GitHub repository URL.
     - `branch`: Branch to clone.
     - `targetDir`: Directory to clone the repository into.

2. **`file.py`**  
   - A Python script that processes a CSV file (`sales.csv`) and generates a bar chart of total sales by product.
   - The script uses the following Python libraries:
     - `pandas`
     - `matplotlib`
   - The output is saved as `sales_report.png`.

3. **`sales.csv`**  
   - A sample CSV file containing sales data for different products.

## Instructions

### Step 1: Push the Files to Your GitHub Repository
1. Create a new repository on your GitHub account.
2. Push all files from the zip file to the root of your repository.
3. Ensure the repository is private.

### Step 2: Set Up the Jenkins Pipeline
1. Open Jenkins and create a new pipeline job.

### Step 3: Implement the Pipeline
You are required to modify the `pipeline.Jenkinsfile` to complete the following stages:

#### Clone the Repository
- Ensure the repository is cloned into the specified `targetDir`.

#### Run the Python Script
- Set up a Python virtual environment.
- Install dependencies from `requirements.txt`.
- Execute `file.py`.

#### Send Email Notification
- Use the Gmail SMTP server to send an email.
- Attach the `sales_report.png` file and pipeline logs to the email.

### Step 4: Test the Pipeline
1. Trigger the pipeline in Jenkins with the required parameters:
   
2. Verify that:
   - The repository is cloned successfully.
   - The Python script runs and generates `sales_report.png`.
   - An email is sent with the required attachments.

### Notes
- Follow the comments in the `pipeline.Jenkinsfile` and `file.py` for detailed requirements for each stage.
- Ensure that the pipeline handles errors gracefully and logs meaningful messages.
- Use Groovy methods in the Jenkinsfile for better readability and maintainability.

### Interview Guidelines
- You have 30 minutes to ask any questions about the task.
- Use the provided files as a starting point and modify them to meet the requirements.
- Focus on implementing the pipeline stages step by step.
- Ensure your solution is functional and adheres to the requirements.

Good luck!