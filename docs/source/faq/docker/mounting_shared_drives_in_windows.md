# Mount a Windows shared drive in a Docker container

### Linux, Mac and Windows
1. Open a new terminal or PowerShell.
2. Mount the shared drive by executing the following command:
    ```bash
    docker exec -it --user root -e UPI=USER -e GRANT_SUDO=yes opencmiss-iron mount-shared-drive.sh
    ```
    Replace ```USER``` in the command above with your username credentials for the mounted drive.
3. You will be prompted for your password. Enter it.
4. Exit the terminal/PowerShell.

The shared drive will now be available within the running container in the path specified in the `mount-shared-drive.sh script`, and can be accessed e.g. within the Juypterlab interactive session.