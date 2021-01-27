# Setup XQuartz X11 server on Mac

The XQuartz X11 server will be used to allow us visualise GUI programs, which are running inside the Docker container, on the host Mac machine. The following guide has been adapted from [this](https://sourabhbajaj.com/blog/2017/02/07/gui-applications-docker-mac/) link.

1. Install XQuartz
    1. From the [XQuartz website](https://www.xquartz.org/) 
    2. Using homebrew
        ```bash
        brew cask install xquartz
        ```
2. Run XQuartz
    1. Start XQuartz from command line using:
        ```bash
        open -a XQuartz
        ```
    2. In the XQuartz preferences, go to the `Security` tab and make sure `Allow connections from network clients` is ticked.
    3. Exit and restart XQuartz to allow the updated preferences to take affect.
3. Identify and add your Host Machine IP to Xhost
    1. Run the following command in a terminal to find your Host Machine IP:
        ```bash
        IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
        ```
    2. Check if the `IP` enviromental variable has been set correctly:
        ```bash
        echo $IP
        ```
       If blank and you are on wifi, try `en1` instead of `en0` in Step (i).
    3. Add the IP using Xhost:
        ```bash
        xhost + $IP
        ```
       If this produces an error, try:
        ```bash
        /usr/X11/bin/xhost + $IP
        ```