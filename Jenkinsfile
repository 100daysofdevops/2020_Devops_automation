pipeline {
  agent any
  stages {
    stage('mycheckout') {
      steps {
        echo 'hello pipeline'
      }
    }

    stage('my-script') {
      parallel {
        stage('my-script') {
          steps {
            sh 'echo $Name'
          }
        }

        stage('parallel_stage') {
          steps {
            sh 'echo "This is parallel stage"'
          }
        }

        stage('archiveartifacts') {
          steps {
            archiveArtifacts(artifacts: 'mt-test.zip', fingerprint: true)
          }
        }

      }
    }

  }
  environment {
    Name = 'Prashant'
  }
}