pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando código fuente...'
                sh 'python3 -m py_compile app.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'python3 test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando aplicacion en entorno de prueba...'
                sh 'python3 app.py'
            }
        }
    }
}
