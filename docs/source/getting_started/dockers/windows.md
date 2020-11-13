# Running via Docker on Windows

## Directory setup
Create the following work folders:
1. Folder where the heart-biomechanics code and its dependencies will be stored:
    ```
    C:\Users\upi\Documents\opt
    ```  
2. Folders where new python modules installed by the user will be stored:
    ```
    C:\Users\upi\Documents\usr\local
    C:\Users\upi\Documents\usr\cache
    ```  

Replace ```upi``` in the above command with your windows login name.

## Setup
### Install docker for Windows

1. Install docker desktop.
2. Start docker.
3. Go to the ```Settings``` page and check that the 
```Use the WSL 2 based engine``` option is turned off.`

## Execution
The following steps describe how to run the docker each time you want to run
simulations.

### Running the docker image
1. Open a Windows PowerShell
2. Run the following command:
   ```bash
    docker run --rm -p 10001:22 -p 10000:8888 -e JUPYTER_ENABLE_LAB=yes --privileged -v c/Users/upi/Documents/opt:/home/jovyan/work -v c/Users/upi/Documents/usr/local:/home/jovyan/.local -v c/Users/upi/Documents/usr/cache:/home/jovyan/.cache prasadbabarendagamage/opencmiss-iron:1.0-minimal
   ```
   Replace ```upi``` in the above command with your windows login name.

```Note:: This step will take some time.
```

This will start the JupyterLab server on port 8888 within the docker container.
![Container running on docker desktop](/images/running_heart_biomechanics_docker_container.png) 

A JupyterLab interactive session can be started in the browser of your host windows machine by copying and pasting the url with the access token (highlighted in yellow) into a web browser (e.g. chrome). 

However, note that the above url will give a ```This site can’t be reached 127.0.0.1 refused to connect``` error. This is because the ```docker run``` command above maps port number 8888 within the container to port number 10000 on the host windows machine. Replace 8888 with 10000 and the JupyterLab interactive session will load as expected on your web browser.

``` Important:: The working opt directory created in the host windows machine in Section 3.1 is mapped to "/home/jovyan/work" within the container. Only items within this folder will persist once the container is shutdown. Any files outside this container will not be recoverable (running a container can be thought of as getting a new computer with a fresh installation - only items in the mapped drive will be available the next time you start the container using the commands in Section 3.3.1). 
```

### Connecting to a running container:

1. Open a new windows PowerShell.
2. Take note of the ID of the running OpenCMISS-Iron container:
    ```bash
    docker container ls
    ````
   The ID of the container is shown in the left-most column (as highlighed in the following screenshot).
   ![List of running containers](/images/listing_running_docker_containers.png)
3. Connect to the running container:
    ```bash
    docker exec -it --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes CONTAINER_ID start.sh 
    ```
   Replace ```CONTAINER_ID``` in the above command with the container ID from step 2.
   This will open a new bash terminal within the running container with sudo (admin) access as shown below:
  ![List of running containers](/images/running_terminal_in_docker_container.png)
   
4. Mount the eResearch drive
    ```bash
    sudo mkdir -p /eresearch/heart
    sudo mount -v -t cifs //10.10.150.143/research/resmed201900006-biomechanics-in-heart-disease/ /eresearch/heart -o username=upi,domain=uoa,vers=3.0
    ```
    Replace ```upi``` in the command above with your University upi.

The eResearch drive will now be available within the running container in the following path: ```/eresearch/heart```. This can be accessed within the Juypterlab interactive session.

### Start the ssh server.
If you wish to use Pycharm to remotely run and debug heart-biomechanics code, then also run the following command in the running container.
```bash
sudo /usr/sbin/sshd -D &
```
This will start up an ssh server to allow you to connect to python interpreters inside the container from Pycharm running on your host windows machine.

## First run setup
If you have not run the heart-biomechanics code before, the following steps will also needed to be performed within the running container (the same terminal openned within the container from the previous section can be used to excute these steps).
``` Important:: The steps below only need to be run on fresh installations of the docker.
```

### Install heart-biomechanics dependencies
``` bash
pip install --user 'tensorflow-cpu==2.2.0'
```

### Clone heart-biomechanics repository
``` bash
cd /home/jovyan/work
git clone https://github.com/GITHUB_USER_NAME/heart-biomechanics.git
```
Replace ```GITHUB_USER_NAME``` in the above command with your github user name.

This will clone the master branch of the heart-biomechanics code.

### Clone heart-biomechanics dependencies
``` bash
cd /home/jovyan/work
git clone https://github.com/PrasadBabarendaGamage/mesh-tools.git
git clone https://github.com/PrasadBabarendaGamage/utilities.git
git clone https://github.com/PrasadBabarendaGamage/pca.git
git clone https://github.com/PrasadBabarendaGamage/parameter-estimation.git
git clone https://github.com/PrasadBabarendaGamage/morphic.git
```

## Troubleshooting
1. The following error may be encountered when trying to execute the "docker run" command:
    ```bash
    Bind for 0.0.0.0:10000 failed: port is already allocated.
    ```
   Solutions:
   1. check that you do not have another instance of the heart-biomechanics container running, by opening the docker desktop application as shown below.
    ![Container running on docker desktop](/images/docker_desktop_running_container.png)    
   If another instance is running, click on the container and click the stop button button to close the container, and try the command above again. 
   
   2. If the issue persists, then port number 10000 may be in use by another service. Replace the port number 10000 with another number e.g. 20000 and retry.

