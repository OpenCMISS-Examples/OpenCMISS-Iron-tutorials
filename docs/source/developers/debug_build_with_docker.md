# Creating a debug build with Docker on local Windows, Linux, and Mac machines

## Introduction
We can leverage the prebuilt OpenCMISS-Iron Docker images to build a developer version of OpenCMISS.  The instructions below outline how you can create a developer build of OpenCMISS-Iron using the prebuilt OpenCMISS-Iron Docker image on your Windows, Mac, or Linux host operating system. 

## First steps
The first step is to deploy the release version of the OpenCMISS-Iron docker by following the instructions on the installation page of the getting started section of this documentation.

It is recommended to perform this deployment in a new directory to where the non-developer version of OpenCMISS-Iron is deployed. This involves changing the folder on the host operating system which will be mapped inside the docker e.g. from `oc` mentioned in the installation documentation to `oc_development`. Remember to also update the commands for running the docker to use the updated host operating system directory.

## Building a debug version of OpenCMISS-Iron
Once OpenCMISS-Iron has been deployed, start a command line instance of the docker using the instructions on the running page of th getting started section of this documentation.  Again, remember to update folder mapping path to `oc_development` e.g. on Linux, the command for running the Docker in the terminal would be:
```bash
docker run \
    --rm \
    --name opencmiss-iron \
    -it \
    -v ~/oc_development/opt:/home/jovyan/work \
    -v ~/oc_development/usr/local:/home/jovyan/.local \
    -v ~/oc_development/usr/cache:/home/jovyan/.cache \
    -v ~/oc_development/usr/etc/jupyter:/etc/jupyter \
    -v ~/oc_development/usr/bin/:/usr/local/bin \
    prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start.sh
```
Run the following commands in the terminal. This will copy the OpenCMISS-Iron build directory stored inside the Docker container to the mapped folder on the host operating system. This enables any changes to the source code to persist after a given instance of the Docker container is shutdown.

```bash
cp -r /home/jovyan/opencmiss-build /home/jovyan/work/opencmiss-build
rm -r /home/jovyan/work/opencmiss-build/setup-build
```

We will now build the debug version of OpenCMISS-Iron

```bash
mkdir -p /home/jovyan/work/opencmiss-build/setup-build
cd /home/jovyan/work/opencmiss-build/setup-build
cmake -DOPENCMISS_CONFIG_BUILD_TYPE=Debug -DOPENCMISS_LIBRARIES=iron -DOPENCMISS_PYTHON_EXECUTABLE=/opt/conda/bin/python -DOPENCMISS_ROOT=../opencmiss ../setup
cmake --build .

# Update the branch of iron that is built with OpenCMISS.
cd ../opencmiss/src/iron
git remote rename origin prime
git remote add origin https://github.com/PrasadBabarendaGamage/iron # Replace "PrasadBabarendaGamage" with the github account where your iron fork is located. Need to check that your version of iron is up-to-date with the version of OpenCMISS in the developer branch of the prime https://github.com/OpenCMISS/iron repo.
git fetch origin
git checkout latest # Replace "latest" with your branch of interest.

cd /home/jovyan/work/opencmiss-build/opencmiss/build/iron/debug
make clean
make
make install

# Re-build the Debug, which will now use the custom iron library fork that was specified above)
cd /home/jovyan/work/opencmiss-build/setup-build
cmake -DOPENCMISS_CONFIG_BUILD_TYPE=Debug -DOPENCMISS_LIBRARIES=iron -DOPENCMISS_PYTHON_EXECUTABLE=/opt/conda/bin/python -DOPENCMISS_ROOT=../opencmiss ../setup
cmake --build .
```

Add to the following line to at the bottom of `/home/jovyan/work/bashrc` to override the default location of the default/release build of OpenCMISS-Iron library located inside the docker container.
```bash
export PYTHONPATH=/home/jovyan/work/opencmiss-build/opencmiss/install/lib/python3.8/opencmiss.iron:$PYTHONPATH
```
Exit the terminal/docker and enter the docker again for the updates to PYTHONPATH to take effect, or paste the above export command into the terminal.

## Modifying the source code and updating the debug build
After modifying the source code, run the following commands in the terminal to rebuild the debug version.
```bash
cd /home/jovyan/work/opencmiss-build/opencmiss/src/iron
# make edits in iron/src files, etc.

# Rebuild debug version of iron after modifying iron source files
cd /home/jovyan/work/opencmiss-build/opencmiss/build/iron/debug
make clean
make
make install
```

## Updating the release build
After modifying the source code, run the following commands in the terminal to rebuild the release version.
```bash
cd /home/jovyan/work/opencmiss-build/opencmiss/build/iron/release
make clean
make
make install
```

## Setting up the Totalview debug tool
Install totalview in `/home/jovyan/work/` within the docker e.g. once installed, the Totalview executables would be stored in `/home/jovyan/work/toolworks/totalview.2021.4.10/bin`.

Add to the following line to at the bottom of `/home/jovyan/work/bashrc`. Update the path to Totaview based on the version that you installed. This step is only required to be performed once.
```bash
export PATH=/home/jovyan/work/toolworks/totalview.2021.4.10/bin:$PATH
```

## Using the Totalview debug tool
Run the following command to start debugging the OpenCMISS-Iron library.
```bash
tv8 pyton -a /path/to/your/opencmiss/python/script
```