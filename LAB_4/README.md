# LAB 4

## Хід роботи

1. Learned about docker in the official documentation
2. Run following commands to test is docker installed successfully:
   ```
   sudo docker -v
   sudo docker -h
   sudo docker run docker/whalesay cowsay Docker is fun
    ```
   Output:
   ```
   $ sudo docker -v
   $ sudo docker -h
   $ sudo docker run docker/whalesay cowsay Docker is fun
   ``` 
   Execution output for these commands located at `test_output.txt` file of this repo.
3. Learned the Dockerfile documentation
4. Create new Dockerfile with Django web app from previous lab
5. Created new DockerHub [repository](https://hub.docker.com/repository/docker/cieldidux/lab4) for this lab 
6. Build and push [image](https://hub.docker.com/layers/129019399/cieldidux/lab4/django/images/sha256-b9c6b3b21d634fa752915894e47d88da68434792927f3a78ef4836e76b5fe7fa?context=explore) to the repo:
   ```
   sudo docker build --tag cieldidux/lab4:django .
   sudo docker push cieldidux/lab4:django
   ```
7. Run the docker image with 
   ```
   sudo docker run -it --name=django-page --rm --publish 8000:8000 cieldidux/lab4:django
   ```
   Web page works well
8. Create container for minotoring utility:
   1. Create Dockerfile.monitor
   2. Build image with 
      ```
      $ sudo docker build --tag monitor_utility:django --file Dockerfile.monitor . 
      ```
   3. Run both containers.
      ```
      $ sudo docker run -it --name=django-page --rm --publish 8000:8000 cieldidux/lab4:django
      $ sudo docker run --net=host --name=monitor-util --rm -it monitor_utility:django
      ```
	  При запуску дуругого контейнера можна побачити що на терміналі де запускувся сайт приходить інформація.
	  ```
	  [07/Dec/2020 16:44:20] "GET /health HTTP/1.1" 301 0
	  [07/Dec/2020 16:44:20] "GET /health/ HTTP/1.1" 200 90
	  Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS.
	  Bad Request: /
	  [07/Dec/2020 16:44:35] "GET / HTTP/1.1" 400 58864
	  Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS.
	  Bad Request: /favicon.ico
	  [07/Dec/2020 16:44:51] "GET / HTTP/1.1" 200 166
	  [07/Dec/2020 16:45:40] "GET / HTTP/1.1" 200 166
	  ```

