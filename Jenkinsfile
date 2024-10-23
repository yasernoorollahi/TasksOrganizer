pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from the Git repository
                git url: 'https://your-git-repo-url.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Simulate a build step
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                // Simulate a test step
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                // Simulate a deployment step
                echo 'Deploying the project...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
