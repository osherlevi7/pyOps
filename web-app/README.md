# Flask web app using python 

### TREE 
    - web-app 
        - Dockerfile
        - templates/
            - hello.html
        - app.py


### Build the App inside Docker container 
    $ docker build . -t <repo>/<image-name>

### Run the container 
    $ docker run -d <repo>/<image-name>