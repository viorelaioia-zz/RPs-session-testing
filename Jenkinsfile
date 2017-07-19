@Library('fxtest@1.6') _

/** Desired capabilities */
def capabilities = [
  browserName: 'Firefox',
  version: '53.0',
  platform: 'Windows 10',
  idleTimeout: '910'
]

pipeline {
  agent {label 'mesos-testing'}
  options {
    timestamps()
    timeout(time: 1, unit: 'HOURS')
  }
  environment {
    VARIABLES = credentials('SESSION_TESTING_VARIABLES')
    PYTEST_ADDOPTS =
      "-n=auto " +
      "--tb=short " +
      "--driver=SauceLabs " +
      "--variables=capabilities.json " +
      "--variables=${VARIABLES}"
    SAUCELABS_API_KEY = credentials('SAUCELABS_API_KEY')
  }
  stages {
    stage('Lint') {
      steps {
        sh "tox -e flake8"
      }
    }
    stage('Test') {
      steps {
        writeCapabilities(capabilities, 'capabilities.json')
        sh "tox -e py27"
      }
      post {
        always {
          archiveArtifacts 'results/*'
          junit 'results/*.xml'
          publishHTML(target: [
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: 'results',
            reportFiles: "py27.html",
            reportName: 'HTML Report'])
        }
      }
    }
  }
}