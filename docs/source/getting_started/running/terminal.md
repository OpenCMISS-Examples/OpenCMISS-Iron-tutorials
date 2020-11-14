# Running from a command line terminal

## For a Docker installation
1. Open a new terminal or PowerShell on your host machine.
2. Start the OpenCMISS-Iron Docker container by executing the following command:
    i. Linux and Mac
    
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

    ii Windows
    
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
    This will open a new bash terminal within the running OpenCMISS-Iron Docker container with sudo (admin) access as shown below:
    ![Start bash terminal in running container](./docker_start_bash_terminal.png)
    
3. In the Docker terminal from Step 2, either: 
    1. run python from the terminal: 
        ```bash
        python
        ```
        Load the OpenCMISS-Iron python module.
        ```python
        # Import python modules
        from opencmiss.iron import iron
        ```
    2. or run an python script containing OpenCMISS-Iron library calls directly from the terminal:
          ```bash
        python your_python_script.py
        ```   
