# Troubleshooting

1. The following error may be encountered when trying to execute the "docker run" command:
    ```bash
    Bind for 0.0.0.0:10000 failed: port is already allocated.
    ```
   Solutions:
   1. check that you do not have another instance of the heart-biomechanics container running, by opening the docker desktop application as shown below.
    ![Container running on docker desktop](./docker_desktop_running_container.png)    
   If another instance is running, click on the container and click the stop button button to close the container, and try the command above again. 
   
   2. If the issue persists, then port number 10000 may be in use by another service. Replace the port number 10000 with another number e.g. 20000 and retry.

