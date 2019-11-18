# Hello-World-Api-WebApp using Flask

## Artifacts used to develop this simple web application :
* Python
* Flask - Flask is a Python web framework, it is a third-party Python library used for developing web applications.
* Git - Source control
* Gitgub - Interface for this repository
* Docker - To containerise this web application and expose the application service 
* Linux - AWS AMI --> Alpine Linux 3.10.1-19b85397-1476-4b55-a313-2a543eae6021-ami-017a39af3404e180e.4 

Build the image using the following command

```bash
$ docker build -t webapp-simple:1 .
```
I am using version as 1 for initial build, you can customoise the image for your needs and change the version number for better tracking and differentiation.

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 webapp-simple:1
```

API endpoint will be accessible at http:hostname:5000/api

Web app will be accessible at http://hostname:5000/index

Port 5000 is default used in Flask fremework, you can change it if needed, otherwise you can change the tcp port that you are exposing to internet like http port as 80. simply run below to use default http port as below 

```bash
$ docker run -d -p 80:5000 webapp-simple:1
```
### Testing
I have tested the application and works fine for me. Please navigate to "testing" folder and verify execution and testing results.
