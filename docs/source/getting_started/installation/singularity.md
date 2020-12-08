# Installation via Singularity on Linux HPC machines

## Introduction
In this section we describe how to install OpenCMISS-Iron via [Singularity](https://sylabs.io/) on high performance computing machines. Prior to beginning, ensure that your IT administrators have installed Singularity on your HPC machines. 

We will use the same folder structure that was outlined in the OpenCMISS-Iron Docker 'Installation instructions'.

## Setup

1. Open a new terminal.
2. Check that you are using the bash shell:
    ```bash
    echo $SHELL
    ```
3. If the command above does not print `/bin/bash` then start a bash shell:
    ```bash
    bash
    ```
   
4. Extract the OpenCMISS-Iron folder structure:
    ```bash
    cd ~ # Enter your home directory.
    wget https://opencmiss-iron-tutorials.readthedocs.io/en/latest/_static/oc.zip
    ```

5. Set a new environmental variable to specify where you will extract the OpenCMISS-Iron folder structure.
    ```bash
    export OC_DIR=/path/to/your/oc_dir
    ```
   
6. Test run the OpenCMISS-Iron container using the following command (ensure that there are no trailing spaces following the end-of-line backslashes deliminators):
    ```bash
    singularity run docker://prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start.sh
    ```
    ``` Important::  This will open a terminal inside the running OpenCMISS-Iron Singularity container. Note that, Singularity only allows you to access the container using the same username as the one you used to start the container (i.e. it doesn't use the user 'jovyan' that we had pre-configured when using Docker containers). By default, Singularity also mounts your $HOME directly inside the container, therefore, unlike the OpenCMISS-Iron Docker installations, we don't need to mount additional folders, unless you would like to access folders outside your home drive. If you wish to add such a folder, you can use the same mount syntax described in the OpenCMISS-Iron Docker Installation instructions, and replace the '-v' optional argument key with '-B'. 
    ```   
   
7. Shutdown the container.
   
## Post-install setup
Follow the post-install setup instructions on the OpenCMISS-Iron Docker Installation instructions.
