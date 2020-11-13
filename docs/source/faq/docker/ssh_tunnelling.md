# Tunnelling into docker container using ssh

## Setup the SSH server
1. Ensure Step 1.3 of 'Running via Docker' have been performed.
1. Follow Step 1.4.1 to connect to a running container. 
2. Enter the following command in the bash shell created in the previous step.
    ```bash
    sudo start-ssh-server.sh
    ```
   This will enable remote access to the  docker container from your host machine through ssh tunnelling.
   
``` Important:: Running the script above, changes the password of the default user of the docker container (jovyan) to 'admin'.
```   

## SSH tunnelling into the running container
From a terminal or PowerShell on your host machine, enter the following:
```bash
ssh jovyan@localhost -p 10001
```
This will allow you to tunnel into the running container. 