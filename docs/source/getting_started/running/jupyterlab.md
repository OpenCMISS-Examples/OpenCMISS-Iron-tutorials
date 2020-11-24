# Running with JupyterLab

The following instructions describe how to run JupyterLab with OpenCMISS-Iron using Docker. 

## Starting the Docker container
### Linux and Mac
```bash
docker run \
    --rm \
    --name opencmiss-iron \
    -p 10000:8888 \
    -e JUPYTER_ENABLE_LAB=yes \
    -v ~/oc/opt:/home/jovyan/work \
    -v ~/oc/usr/local:/home/jovyan/.local \
    -v ~/oc/usr/cache:/home/jovyan/.cache \
    -v ~/oc/usr/etc/jupyter:/etc/jupyter \
    -v ~/oc/usr/bin/:/usr/local/bin \
    prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh
```

``` Important:: Ensure that there are no trailing spaces following the end of line backslash deliminators.
```

### Windows
```bash
docker run `
    --rm `
    --name opencmiss-iron `
    -p 10000:8888 `
    -e JUPYTER_ENABLE_LAB=yes `
    -v c/Users/${env:UserName}/Documents/oc/opt:/home/jovyan/work `
    -v c/Users/${env:UserName}/Documents/oc/usr/local:/home/jovyan/.local `
    -v c/Users/${env:UserName}/Documents/oc/usr/cache:/home/jovyan/.cache `
    -v c/Users/${env:UserName}/Documents/oc/usr/etc/jupyter:/etc/jupyter `
    -v c/Users/${env:UserName}/Documents/oc/usr/bin/:/usr/local/bin/ `
    prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh
```

``` Important:: Ensure that there are no trailing spaces following the end-of-line tilda deliminators.
```

## Accessing JupyterLab

The above commands will start a JupyterLab server on port 8888 within the docker container.

A JupyterLab interactive session can be started in the browser of your host machine by copying and pasting the url with the access token (highlighted in yellow in the figure below) into a web browser (e.g. chrome). 

![Docker JupyterLab server url](./docker_jupyter_server_url.png) 

However, note that the above url will give a ```This site can’t be reached 127.0.0.1 refused to connect``` error. This is because the ```docker run``` command above maps port number 8888 within the container to port number 10000 on the host windows machine. Replace 8888 with 10000 in the url and the JupyterLab interactive session will load as expected in your web browser.

## Working with JupyterLab

The following resources can help you with learning the features of JupyterLab:
- [Main website](https://jupyter.org/)
- [Documentation](https://jupyterlab.readthedocs.io/en/stable/)
- [Tips and tricks](https://towardsdatascience.com/jupyter-notebooks-tips-and-tricks-4e995e7b1fd0)

