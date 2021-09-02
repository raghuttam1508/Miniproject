pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Build') {
            steps {
                echo 'Build World'
            }
        }
        stage('END') {
            steps {
                echo 'END World'
            }
        }
    }

    post
    {
        always
        {
            emailext body: 'Test successful', subject: 'Test', to: 'raghu.parvatikar@gmail.com'
        }
    }
}
