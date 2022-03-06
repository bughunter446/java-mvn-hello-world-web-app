node{
   // This stage is used to checkout the code from GitHub.
   stage('SCM Checkout'){
       sh "pwd"
       git credentialsId: 'rahul_github', url: 'https://github.com/rahulguna/java-mvn-hello-world-web-app.git'
   }
   // This stage is used to perform maven clean package build, so the war file is created.
   stage('Mvn Package'){
     sh "whoami"
     sh "sudo mvn clean install"
   }
   stage('SAST'){
      sh "echo SAST"
      //sh "java -jar /home/rahulguna/Downloads/spotbugs-4.0.6/lib/spotbugs.jar -textui -project /home/rahulguna/Downloads/Insecure_bank.fbp"
   }
   stage('Deploy'){
      sh "cp /var/lib/jenkins/workspace/Stargazer/target/mvn-hello-world.war /home/rahulguna/Documents/apache-tomcat-9.0.37/webapps/"
   }
   stage('DAST'){
      sh "echo DAST"
      sh "java -jar /home/rahulguna/Downloads/ZAP_2.9.0_Linux/ZAP_2.9.0/zap-2.9.0.jar -host localhost -port 8081 -cmd -quickurl http://localhost:8082/mvn-hello-world/ -quickprogress -quickout /home/rahulguna/Documents/zap_report.xml"
   }
}
