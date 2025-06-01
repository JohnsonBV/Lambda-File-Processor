pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-2"
        FUNCTION_NAME = "fileProcessorLambda"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/JohnsonBV/Lambda-File-Processor.git'
            }
        }

        stage('Zip Lambda') {
            steps {
                sh 'zip lambda.zip lambda_function.py'
            }
        }

        stage('Update Lambda') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-lambda-creds']]) {
                    sh """
                    aws lambda update-function-code \
                        --function-name $FUNCTION_NAME \
                        --zip-file fileb://lambda.zip \
                        --region $AWS_REGION
                    """
                }
            }
        }
    }
}

