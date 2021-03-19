# Setup X11 on linux

If you get an error e.g. ```can't connect to X11 window server using ':0'```, run the following command in your host terminal prior to running the ```docker run``` command:
```bash
xhost +
```
For more details on xhost, please see the following [link](https://www.stitson.com/pub/book_html/node72.html).
