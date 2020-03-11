pipeline {
  agent any
  stages {
    stage('mycheckout') {
      steps {
        echo 'hello pipeline'
      }
    }

    stage('my-script') {
      steps {
        sh 'echo $NAME'
      }
    }

  }
  environment {
    Name = 'Prashant'
  }
}