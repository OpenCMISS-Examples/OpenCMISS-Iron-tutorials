# Functional testing

Documentation for running the OpenCMISS-Iron functional testing framework can be found in the following [link](https://github.com/OpenCMISS/functional_test_framework).

For convenience, a script is provided for setting up the functional testing framework and running all the tests with a OpenCMISS-Iron docker installation.

This script will create a new folder in the `~/work/functional-tests` folder within the docker container (also accessible from your host operating system's `oc/opt` folder as described on the Getting started, installation, docker documentation page).

1. Navigate to the instructions on the Getting started, running, terminal documentation page.

2. Follow the instructions for your operating system until the step asking you to `run the following`

3. Copy the command for running the docker container and paste it into your terminal or PowerShell.

4. Replace the `start.sh` script with `start-functional-tests.sh`

5. Run the command to execute the tests.

6. Type exit to shutdown the docker container.


To rerun the tests, on your host operating system, remove the `oc/opt/functional-tests` folder and rerun the steps above.


