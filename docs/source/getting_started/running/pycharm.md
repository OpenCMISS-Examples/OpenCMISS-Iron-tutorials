# Running from Pycharm

This section describes how we can use OpenCMISS-Iron code from the 
pycharm Integrated Development Environment (IDE).

## Preliminaries
If you are a student or a researcher, follow the link below to determine if you are eligible to sign up for a free educational license to use the Professional Edition:
    [link](https://www.jetbrains.com/community/education/#students). This will give you access to features e.g. code profiling etc, remote debugging, interacting with dockers.

Alternatively, you can download the free Community Edition, which is the default option made available as part of the OpenCMISS-Iron Docker instructions.

## For a Docker installation

### Running Pycharm
The following Docker command can be used to start PyCharm (PyCharm will automatically be downloaded and installed in the `~/work/PyCharm` folder). The specific version of PyCharm that is downloaded can be specified in the `oc/usr/bin/start-pycharm.sh` script. By default, PyCharm 2020.2.3 is installed. 

#### Linux and Mac
```bash
docker run \
    --rm \
    --name opencmiss-iron \
    -e DISPLAY=${DISPLAY} \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v ~/oc/opt:/home/jovyan/work \
    -v ~/oc/usr/local:/home/jovyan/.local \
    -v ~/oc/usr/cache:/home/jovyan/.cache \
    -v ~/oc/usr/config:/home/jovyan/.config \
    -v ~/oc/usr/java:/home/jovyan/.java \
    -v ~/oc/usr/PyCharm:/home/jovyan/.PyCharm \
    -v ~/oc/usr/etc/jupyter:/etc/jupyter \
    -v ~/oc/usr/bin/:/usr/local/bin \
    prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start-pycharm.sh
```

#### Windows
```bash
docker run \
    --rm \
    --name opencmiss-iron \
    -e DISPLAY=${DISPLAY} \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v ~/oc/opt:/home/jovyan/work \
    -v ~/oc/usr/local:/home/jovyan/.local \
    -v ~/oc/usr/cache:/home/jovyan/.cache \
    -v ~/oc/usr/config:/home/jovyan/.config \
    -v ~/oc/usr/java:/home/jovyan/.java \
    -v ~/oc/usr/PyCharm:/home/jovyan/.PyCharm \
    -v ~/oc/usr/etc/jupyter:/etc/jupyter \
    -v ~/oc/usr/bin/:/usr/local/bin \
    prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start-pycharm.sh

docker.exe run --rm -d ^
        --name pycharm-pro ^
        -e DISPLAY=YOUR_IP_ADDRESS:0.0 ^
        -v %TEMP%\.X11-unix:/tmp/.X11-unix ^
        -v %USERPROFILE%\pycharm-docker:/home/developer ^
        -v %USERPROFILE%\pycharm-docker\python2.7:/usr/local/lib/python2.7 ^
        -v %USERPROFILE%\pycharm-docker\python3.7:/usr/local/lib/python3.7 ^
        rycus86/pycharm-pro:latest

```

#### Configuring PyCharm
On the first run, you will need to configuring your python environment. 

Since the setting are mapped to a drive on your host machine, you will not need to repeat this setup next time you run the OpenCMISS-Iron Docker.