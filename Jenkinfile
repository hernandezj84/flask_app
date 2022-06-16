pipeline {
    agent {
        kubernetes {
            yaml '''
                spec:
                  containers:
                  - name: python3.9
                    image: python3.9
                    command:
                    - sleep
                    args:
                    - 99d
            '''
        }
    }
    stages{
        stage('run service and test') {
            steps {
                container('python3.9') {
                    script {
                        sh """
                            pip install -r requirements.txt
                            pytest
                        """
                    }
                }
            }
        }
    }
}