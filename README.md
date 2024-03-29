# Hello-World-Api-WebApp using Flask

## Artifacts used to develop this simple web application :
* Python
* Flask - Flask is a Python web framework, it is a third-party Python library used for developing web applications.
* Git - Source code control
* Github - Interface for this repository
* Docker - To containerise this web application and expose the application service 
* Linux - AWS AMI --> Alpine Linux 3.10.1-19b85397-1476-4b55-a313-2a543eae6021-ami-017a39af3404e180e.4 (Light weight docker pre-   installed OS)

Clone the repository to your local system using git, would be simple if it is linux to test this.

Build the image using the following command

```bash
$ docker build -t webapp-simple:1 .
```
I am using version as 1 for initial build, you can customoise the image for your needs and change the version number for better tracking and differentiation.

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 webapp-simple:1
```
If you are using AWS to do this exercise, please allow port 5000 or respective TCP port in your security group.

API endpoint will be accessible at http://hostname:5000/apimessage

Web app will be accessible at http://hostname:5000/index

Port 5000 is default used in Flask fremework, you can change it if needed, otherwise you can change the tcp port that you are exposing to internet like http port as 80. simply run below to use default http port as below 

```bash
$ docker run -d -p 80:5000 webapp-simple:1
```
### Testing
I have tested the application and works fine for me. Please open execution.log to verify the steps.

### Note
To make it simeple i have included index.html directly in webapp.py , you can use ### render_template ### module which gives ability to save html files in templates folder and refer them in webapp.py

### Use it for diffenet deployments/Environments

As of now i have done all my work in master branch, please create new feature branches (like dev, nonp, prod) to customise/enhance/modify the code to fit to your enviroment.

### CICD way

To achieve CICD for this web app, use some CICD tools like TeamCity, Jenkins, Codebuild etc to create a pipline and configure webhook in this repo.

So whenver a change is done or merged to master brach, a pipepline will be trigerred to build new docker image and run a container to make your changes effective.

In pipeline, write a simeple shell script which will take care of docker build and docker run (increment version) for all new changes.


### Do you need HA for this web app ?
* use Kubernetes cluster or Docker swarm :)

