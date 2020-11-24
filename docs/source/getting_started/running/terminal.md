# Running from a command line terminal

## For a Docker installation
Start the OpenCMISS-Iron Docker container by executing the following command (ensure that there are no trailing spaces following the end-of-line deliminators):

### Running the Docker container

#### Linux
1. Open a new terminal on your host machine.
2. Run the following:
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
   
    ``` Important:: Ensure that there are no trailing spaces following the end of line backslash deliminators.
    ```
      
    ``` Important:: Repeat the above command if you recieve an error like: 'docker: Error response from daemon'.
    ```

#### Mac
1. Open a new terminal on your host machine.

2. Check that you are using the bash shell:
    ```bash
    echo $SHELL
    ```
3. If the command above does not print `/bin/bash` then start a bash shell:
    ```bash
    bash
    ```
4. Run the following:   
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
   
    ``` Important:: Ensure that there are no trailing spaces following the end of line backslash deliminators.
    ```
      
    ``` Important:: Repeat the above command if you recieve an error like: 'docker: Error response from daemon'.
    ```      

#### Windows
1. Open a new PowerShell on your host machine.
2. Run the following:       
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
   
    ``` Important:: Ensure that there are no trailing spaces following the end-of-line tilda deliminators.
    ```
   
    ``` Important:: Repeat the above command if you recieve an error like: 'docker: Error response from daemon'.
    ```


### Running OpenCMISS-Iron from the Docker container
The command in the previous section will open a new bash terminal within the running OpenCMISS-Iron Docker container as shown below:
![Start bash terminal in running container](./docker_start_bash_terminal.png)

In the Docker terminal, either: 
1. run python from the terminal: 
    ```bash
    python
    ```
    and load the OpenCMISS-Iron python module:
    ```python
    # Import python modules
    from opencmiss.iron import iron
    ```
2. or run an python script containing OpenCMISS-Iron library calls directly from the terminal:
      ```bash
    python your_python_script.py
        ```   
