><h3>Assignment for DevOps Traineeship</h3><br>
><p>-First, I created a Dockerfile for building a docker image which contains application code and required modules. This application is simple application created using html and php. It runs on Apache web-server and uses AWS RDS-MySQL as a database.</p>
><p>-Then build a docker image and pushed it to the private registry in AWS ECR(Elastic Container Registry).</p>
><p>-Created and configured a cluster in AWS ECS.</p>
><p>-Written a AWS Lambda function which create/start a service with EC2 launch type in ECS cluster. This service runs a docker container which runs an application in apache web-server.</p>
><p>-For triggering lambda function, an api endpoint was created using API Gateway.</p>
><p>-So the whole process is when you run the api endpoint, it will trigger the lambda function which create/start a service with EC2 launch type in ECS cluster. This service will run a docker container which contains the application.</p>
