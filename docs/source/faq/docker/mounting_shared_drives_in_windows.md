# Mount a Windows shared drive in a Docker container

``` Important:: This guide is specific to mounting shared drives that are compatible with a the cifs protocol. Please consult your IT team or online resources prior to running the commands described below. We cannont take responsibility for any loss of data that you may encounter when using these instructions. If you encounter any issues please contact your IT team or online resources, as the OpenCMISS developer team are not experts in mounting drives. 
```

### Linux, Mac and Windows
1. Edit the `mount-shared-drive.sh` script located in the `oc/usr/bin` folder and replace the following fields for the shared network drive that you wish to mount. 
    - IP_ADDRESS
    - DRIVE_PATH
    - USER
    - DOMAIN
2. Ensure your OpenCMISS-Iron Docker is running following the instructions in the 'Installation via Docker on local Windows, Linux, and Mac machines' Section of the 'Getting Started' documentation. When issuing the `docker run` command, include a `--privileged` argument.
3. Open a new terminal or PowerShell.
4. Mount the shared drive by executing the following command:
    ```bash
    docker exec -it --user root -e UPI=USER -e GRANT_SUDO=yes opencmiss-iron mount-shared-drive.sh
    ```
    Replace ```USER``` in the command above with your username credentials for the mounted drive.
5. You will be prompted for your password. Enter it.
6. Exit the terminal/PowerShell.

The shared drive will now be available within the running container in the path specified in the `mount-shared-windows-drive.sh script`, and can be accessed e.g. within the Juypterlab interactive session.
