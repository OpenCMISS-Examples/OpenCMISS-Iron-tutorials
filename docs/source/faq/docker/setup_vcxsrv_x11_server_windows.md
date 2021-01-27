# Setup VcXsrv X11 server on Windows

The VcXsrv X11 server will be used to allow us visualise GUI programs, which are running inside the Docker container, on the host Windows machine. The following guide has been adapted from [this](https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde) link.

1. Download VcXsrv from its [SourceForge repository](https://sourceforge.net/projects/vcxsrv/) 

2. Install VcXsrv with default options.
3. Run Xlaunch which gets installed by VcXsrv, and perform the intial configuration as follows:
    1. Display setting: select the "multiple windows" option, and click "Next".
    2. Client startup: check the "Start no client" option, and click "Next".
    3. Extra setting: In addition to the default options, make sure "Disable access control" is enabled, and click "Next".
    4. Click "Finish".
4. Open a PowerShell terminal and set your IP address as an environmental variable.
    1. Run ```ipconfig```
    2. Copy the IP address of your network adapter. It is typically listed under the *Ethernet adapter Ethernet:* category and the *IPv4 Address* field e.g. *135.246.218.122*.
    3. Run the following command to save your IP address as an environmental variable ```$env:IPAddress = "YOUR_IP"```, where YOUR_IP is the IP number you copied from the previous step. The quotation marks ("") need to be included in this command.