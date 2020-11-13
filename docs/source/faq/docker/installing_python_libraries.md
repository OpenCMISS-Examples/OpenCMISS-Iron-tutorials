# Installing python libraries

New python libraries can be installed from a bash terminal running in the Docker container using the following:
``` bash
/opt/conda/bin/pip install --user 'tensorflow-cpu==2.2.0'
```
This installs the module in the `~/.local` within the Docker container, which is mapped to `oc/usr/local/` on the host machine.

``` Important:: Once new packages are installed, to use them with JupyterLab, the kernel needs to be restarted. This can be achieved by selecting the Kernel menu on JupyterLab and selecting Restart Kernel.
```