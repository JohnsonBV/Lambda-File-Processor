pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-2'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/JohnsonBV/Lambda-File-Processor.git'
            }
        }

        stage('Zip Lambda') {
            steps {
                sh 'zip lambda.zip lambda_function.py'
            }
        }

        stage('Update Lambda') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-lambda-creds'
                ]]) {
                    sh '''
                        aws lambda update-function-code \
                          --function-name fileProcessorLambda \
                          --zip-file fileb://lambda.zip \
                          --region us-east-2
                    '''
                }
            }
        }
    }
}

