pipeline {
  agent any
stages {
  stage('checkout') {
    steps {
      git branch: 'main',
      credentialsId: 'hello',
      url: 'https://github.com/Suryalucky10/Python-Projects.git'
}
}
stage('Build') {
  steps {
    echo 'building project'
}
}
stage('test') {
  steps {
    echo 'running tests'
}
}
}
}
