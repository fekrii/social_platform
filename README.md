
  <h3 align="center">Social Platform Task</h3>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#Notes">Notes</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This project is a simple Social Platform app, it uses elastic-search for search feature , docker for deployement , JWT for token authentication, swagger for api documentaion and deployed on AWS Ec2 instance with gunicorn and nginx for static files handling <br>

you can run it locally, or with docker-compose or you can check it online on AWS from this <a href="http://ec2-35-164-43-8.us-west2.compute.amazonaws.com:8000/admin/">Link</a>

you can check the api swagger documentaion from : <i>swagger\/schema/<i/> either locally or with liveserver <br>
also you can check basic model and views documentaion from : <i>admin\/doc/<i/>






<!-- GETTING STARTED -->
## Getting Started

You can run this app locally or with Docker-compose

### Locally


* create virtual environment, and activate it then install the required packages from requirements.txt file
  ```sh
  pip install -r requirements.txt
  ```

* then run the local server 
  ```sh
  pip manage.py runserver
  ```
 
* then open your local server
  ```sh
  localhost:8000
  ```

#### at local host i used SQL lite DB but in production you can use MYSQL, you will find it's configuration commented in settings.py file

### Using Docker

#### there is two docker-compose files and two docker files one of each for development and the other for production
#### at this case we will user docker-compose.yml file

* first build docker image
  ```sh
  docker-compose build
  ```

* then run the image
  ```sh
  docker-compose up
  ```
  
* then open the server
  ```sh
  localhost:8000
  ```

<!-- Notes -->
## Notes

<ul>
  <li>superuser account is :
    <ul>
      <li>email: admin@mail.com</li>
      <li>password: admin</li>
    </ul>
  </li>
  <li>you will find a postman collection with all the requestes and its bodies</li>
  <li>while testing the api with swagger you must send <i>bearer</i> auth token with the requests</li>
  <li>when creating new post with the endpoint <i>/posts</i> you must send <i>post_type</i> field in the body which take travel, news, or event</li>
  <li>testes should be added</li>
  <li>more documentaion should be added maybe using sphinx</li>
  <li>ssl and domain configuration on ec2 should be added as well</li>
</ul>