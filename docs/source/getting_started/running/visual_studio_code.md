# Running from Visual Studio Code

This section describes how we can use OpenCMISS-Iron code from the 
Visual Studio Code Integrated Development Environment (IDE).

## For a Docker installation

### Running Visual Studio Code
The following Docker command can be used to start Visual Studio Code. 

Visual Studio Code will automatically be downloaded and installed in the `~/work/VSCode-linux-x64` folder, which is a folder on the host machine that is mounted within the Docker container. This means that Visual Studio Code will only need to be installed once and all settings will persist even after the Docker container is shutdown/restarted. The specific version of Visual Studio Code that is downloaded can be specified in the `oc/usr/bin/start-vs-code.sh` script. By default, Visual Studio Code 1.51.1 is installed.

#### Linux
Not supported due to a bug with displaying Visual Studio Code on the default X11 server provided by Ubuntu (described further [here](https://stackoverflow.com/questions/64814370/how-do-i-fix-a-blank-white-screen-for-visual-studio-code-run-remotely-through-x1))
#### Mac
1. Follow the instructions in the FAQ Docker 'Setup XQuartz X11 server on Mac' Section.

2. Run the OpenCMISS-Iron Docker:
    ```bash
    docker run \
         --rm \
         --name opencmiss-iron \
         -e DISPLAY=$IP:0 \
         -v /tmp/.X11-unix:/tmp/.X11-unix \
         -v ~/oc/opt:/home/jovyan/work \
         -v ~/oc/usr/local:/home/jovyan/.local \
         -v ~/oc/usr/cache:/home/jovyan/.cache \
         -v ~/oc/usr/config:/home/jovyan/.config \
         -v ~/oc/usr/java:/home/jovyan/.java \
         -v ~/oc/usr/PyCharm:/home/jovyan/.PyCharm \
         -v ~/oc/usr/etc/jupyter:/etc/jupyter \
         -v ~/oc/usr/bin/:/usr/local/bin \
         prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start-vs-code.sh
#### Windows
TBC