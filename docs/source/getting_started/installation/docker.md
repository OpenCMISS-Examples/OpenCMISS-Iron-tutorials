# Installation via Docker on local Windows, Linux, and Mac machines

## Introduction
Tools such as VMware or VirtualBox have enabled users to create  [Virtual machines](https://en.wikipedia.org/wiki/Virtual_machine) to run different operating systems from their computer's native operating system. For example, a user could have Windows running natively on their computer (we will call this the host operating system), but with these tools, they can load an entirely different operating system on their host machine (for example a specific version of Linux). This is achieved by creating a new set of virtual hardware (e.g. cpu's, memory, hard drives, usb controllers, etc) upon which a virtual operating system is run. While being versatile, these virtual machines are resource intensive and have relatively lengthy bootup times (minutes).
 
[Docker](https://www.docker.com/why-docker) on the other hand is a similar tool that allows a user to create a virtualised operating system. However, rather than creating new virtualised hardware on which to run this virtual operating system, it runs the virtual operating system directly on the host machines hardware. This significantly reduces the memory and storage footprints compared with traditional virtual machines, and also reduces bootup times to a few seconds. The Docker tool enables you to prebuild light-weight operating systems along with any programs of interest and store them as Docker images (e.g. webservers, Jupyter notebook server, etc). These images can be hosted in an online repository such as [DockerHub](https://hub.docker.com/). When needed, they can be easily downloaded and run on your host computer. When an image is run, it creates what is known as a Docker container that is an isolated and reproducible instance of the operating system and your programs. You can then interact with the Docker container in a similar manner to how you would interact with a virtual machine e.g. mounting folders to access your files from the host system etc.

The OpenCMISS-Iron team have prebuilt OpenCMISS-Iron and a number of other useful tools within a Docker image. This provides a sandboxed environment for you to easily interact with OpenCMISS-Iron. 

The instructions below outline how you can install the OpenCMISS-Iron Docker image on your Windows, Mac, or Linux host operating system. The 'Running' Section of this getting started guide describes how you can interact with the container and OpenCMISS-Iron using a number of code development tools (e.g. JupyterLab, PyCharm, or Visual Studio Code).

``` seealso:: (Extra information) The OpenCMISS-Iron Docker image is based on the Jupyter Stacks "base-notebook" and "scipy-notebook" Docker images. Briefly, when the OpenCMISS-Iron Docker image is run, it creates a Linux container with a single unprivileged user called "jovyan" whom you can use to interact with the container. Through this user, you will have ownership over the "/home/jovyan" folder within the container. We can access files on our host operating system from within a running OpenCMISS-Iron container by mounting folders within "/home/jovyan". More information on the configuration of this user can before on https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html. 
```

## Directory setup
Before we install the OpenCMISS-Iron Docker, we will first create a set of folders within your host operating system. These folders will be mounted within the OpenCMISS-Iron Docker container when it is run to allow you to access the files in these folders from within the container (much like how you would map/mount a drive on Windows, Mac, or Linux). The following commands for running OpenCMISS-Iron Docker containers expect the following folder structure:
```
oc
└───opt
|       bashrc
|
└───usr
    |
    └───bin
    │       start.sh
    │       start-notebook.sh
    │       start-singleuser.sh
    │       start-ssh-server.sh
    |       start-pycharm.sh
    |       mount-shared-drive.sh
    │       fix-permissions
    |
    └───etc
    │   │
    │   └───jupyter
    │           jupyter_notebook_config.py
    │   
    └───local
    │   
    └───cache
    │   
    └───java
    │   
    └───config
    │   
    └───PyCharm

```
This folder structure contains:

1. `oc/opt` - this will be your main working directory.
2. `oc/usr/bin` - folder containing scripts for running different programs in the container e.g. jupyter servers etc.
3. `oc/usr/etc/jupyter` - folder containing jupyter notebook configuration. 
4. `oc/usr/local` and `oc/usr/cache` - folders where new python modules installed will be stored.
5. `oc/usr/java`, `oc/usr/config`, and `oc/usr/PyCharm` - folders used by Pycharm.


``` Important:: The working oc/opt directory created on the host machine will be mapped to "/home/jovyan/work" within the Docker container. Only items within this folder will persist once the container is shutdown. Any files outside this container will not be recoverable (running a Docker container can be thought of as getting a new computer with a fresh installation - only items in the mapped drive will be available the next time you start the Docker container). 
```

This folder structure associated files have been stored in the following zip file ([zip file](../../_static/oc.zip)). Simply extract the folder as described below:

### Linux and Mac
Go to your home directory and extract the zip file. For example, on linux `~` refers to `/home/$USER/`. Once extracted, the `oc` folder should be found in `/home/$USER/oc`.

### Windows
Move the downloaded zip file to your `my documents` folder (this is typically located in `C:/Users/USER_NAME/Documents/`, where USER_NAME is your Windows login name). Extract the zip file into this folder. Once extracted, the `oc` folder should be found in `C:/Users/USER_NAME/Documents/oc`.

``` Important:: Check the extracted folder to ensure that the zip file was extracted as 'C:/Users/USER_NAME/Documents/oc' and not 'C:/Users/USER_NAME/Documents/oc/oc'.
```

## Install docker

### Linux
1. Follow instructions on [Docker's engine install documentation](https://docs.docker.com/engine/install/).
        
2. Follow the instructions on the Manage Docker as a non-root user section on [Docker's linux-post install documentation](https://docs.docker.com/engine/install/linux-postinstall/) to add your username to the docker group. This will enable you to run docker without requiring super user permission. This is important to ensure that all the files generated by the docker are owned by the user and not the root user. 

3. Once installed, the docker service should already be running.
 
### Mac   
1. On Mac, install Docker Desktop for Mac (macOS) from docs.docker.com/engine/install/
2. Open the Docker Desktop For Mac app.

### Windows

1. Install docker desktop.
2. Start docker.
3. Go to the ```Settings``` page and check that the 
```Use the WSL 2 based engine``` option is turned off.`

## Setup

We will be interacting with the commandline interface to docker through the `docker run` command. We will briefly explain the commandline arguments associated with this command below and then illustrate how to use these commands to run and setup OpenCMISS-Iron containers on Windows, Mac, or Linux host operating systems. 

- `--name opencmiss-iron` This argument specifies the name of the container that the `docker run` command will create.
- `-it` Run the docker container in an interactive mode. This will allow us to open a terminal within the OpenCMISS-Iron container to perform some additional setup steps.
- `-v [host-src]:[container-dest]` Allows a folder, `[host-src]`, on the host operating system (such as our environment folder described in the previous step, to be mounted within the container in the location specified by `[container-dest]`. For example,  e.g. `-v ~/oc/opt:/home/jovyan/work` will mount a folder located at `~/oc/opt` on the host operating system to `/home/jovyan/work` in the container).
- The final argument that the `docker run` command requires is the name of the script to run within the the container when it starts up. The OpenCMISS-Docker image has been automatically configured to access scripts located in the `oc/usr/bin` folder folder without needing to specify their full path.
- The second to last argument of the `docker run` command indicates the location of the Docker image that you want to run e.g. `prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh` points to a image hosted on DockerHub.

More information on arguments for the `docker run` command can be found in the following [link](https://docs.docker.com/engine/reference/run/).

### Linux and Mac

1. Open a new terminal.
2. Check that you are using the bash shell:
    ```bash
    echo $SHELL
    ```
3. If the command above does not print `/bin/bash` then start a bash shell:
    ```bash
    bash
    ```
4. Run the following command (ensure that there are no trailing spaces following the end-of-line backslashes deliminators):
    ```bash
    docker run \
        --rm \
        --name opencmiss-iron \
        -it \
        -v ~/oc/opt:/home/jovyan/work \
        -v ~/oc/usr/local:/home/jovyan/.local \
        -v ~/oc/usr/cache:/home/jovyan/.cache \
        -v ~/oc/usr/etc/jupyter:/etc/jupyter \
        -v ~/oc/usr/bin/:/usr/local/bin \
        prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start.sh
    ```
    ``` Important:: Repeat the above command if you recieve an error like: 'docker: Error response from daemon'.
    ```   
   
### Windows
1. Open a new PowerShell (don't use a standard terminal, as it does not support commands that span multiple lines).
2. Run the following command (ensure that there are no trailing spaces following the end-of-line tilda deliminators)
    ```bash
    docker run `
        --rm `
        --name opencmiss-iron `
        -it `
        -v c/Users/${env:UserName}/Documents/oc/opt:/home/jovyan/work `
        -v c/Users/${env:UserName}/Documents/oc/usr/local:/home/jovyan/.local `
        -v c/Users/${env:UserName}/Documents/oc/usr/cache:/home/jovyan/.cache `
        -v c/Users/${env:UserName}/Documents/oc/usr/etc/jupyter:/etc/jupyter `
        -v c/Users/${env:UserName}/Documents/oc/usr/bin/:/usr/local/bin/ `
        prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start.sh
    ```
    This command will generate output similar to the figure shown below:
    ![Docker Windows pull](./docker_windows_first_pull.png) 

    ``` Important:: Repeat the above command if you recieve an error like: 'docker: Error response from daemon'.
    ```

    ``` Important:: Once this command is executed, pop-ups will show on the bottom right of the windows desktop requestion permission for docker to access folders as shown below. Select 'share it' for each case. 
    ```
    ![Docker Windows share-it permissions](./docker_windows_share_it_permissions.png) 

## Post-install setup

1. Install any modules you wish to use with OpenCMISS-Iron. We will install the python `meshio` package that is used in the OpenCMISS-Iron tutorials for exporting meshes to different formats, and the h5py package that provides support for loading and saving files in hdf5 format. 
    ``` bash
    /opt/conda/bin/pip install --user 'meshio==4.3.5' h5py
    ```
    ``` Important:: Once new packages are installed, to use them, the JupyterLab kernel needs to be restarted. This can be achieved by selecting the Kernel menu on JupyterLab and selecting 'Restart Kernel'.
    ```
2. **For running tutorials** Clone python modules used by the OpenCMISS tutorials:
    ``` bash
    mkdir ~/work
    cd ~/work
    git clone https://github.com/PrasadBabarendaGamage/mesh-tools.git
    git clone https://github.com/PrasadBabarendaGamage/morphic.git
    git clone https://github.com/PrasadBabarendaGamage/utilities.git   
    ```
    ``` Note:: When using a PowerShell, copy these commands one line at a time.
    ```   
3. Shutdown the Docker container.
    ``` bash
    exit
    ```
4. **For running tutorials** Specify the location of the python modules that you cloned in Step 2. This is typically achieved by updating your bashrc file. For more information on bashrc files, see the following external [link](https://support.nesi.org.nz/hc/en-gb/articles/360001194536-What-are-my-bashrc-bash-profile-for-). 

    Add the following to your `~/oc/opt/bashrc` file (this can be achieved using a text editor on your host operating system).

    ``` Note::  On Windows hosts, it is recommended to use a text editor that is compatible with linux files such as [Notepad++](https://notepad-plus-plus.org/downloads/). This is because the default notepad or wordpad programs on Windows use carriage returns as end-of-line deliminators, which are are not propertly recognised by linux.
    ```   

   ```bash
   export PATH=/opt/conda/bin/:$PATH
   export PYTHONPATH=/home/jovyan/work/mesh-tools:$PYTHONPATH
   export PYTHONPATH=/home/jovyan/work/morphic:$PYTHONPATH
   export PYTHONPATH=/home/jovyan/work/utilities:$PYTHONPATH
   
   export JUPYTER_PATH=/home/jovyan/work/mesh-tools:$JUPYTER_PATH
   export JUPYTER_PATH=/home/jovyan/work/morphic:$JUPYTER_PATH
   export JUPYTER_PATH=/home/jovyan/work/utilities:$JUPYTER_PATH      
   ```
   