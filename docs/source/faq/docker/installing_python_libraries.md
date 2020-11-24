# Installing python libraries

1. Run an OpenCMISS-Iron Docker container using the instructions in the Running from terminal Section in the Getting Started Section.

2. New python libraries can be installed from the bash terminal running in the Docker container using the following command:

    ``` bash
    /opt/conda/bin/pip install --user 'tensorflow-cpu==2.2.0'
    ```
    This installs the module in the `~/.local` within the Docker container, which is mapped to `oc/usr/local/` on the host machine.
    
    ``` Important:: Once new packages are installed, to use them with JupyterLab, the kernel needs to be restarted. This can be achieved by selecting the Kernel menu on JupyterLab and selecting Restart Kernel.
    ```