node('docker') {

    stage 'Checkout'
        checkout scm
    stage 'Build & UnitTest'
        sh "docker build -t conduit:B${BUILD_NUMBER} -f Dockerfile ."
        sh "docker build -t conduit:test-B${BUILD_NUMBER} -f Dockerfile.Integration ."
}