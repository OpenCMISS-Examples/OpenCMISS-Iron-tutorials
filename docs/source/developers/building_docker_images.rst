Building docker images
======================
This section describes how to build the OpenCMISS-Iron docker images.

Setting up dockerfiles
----------------------

.. literalinclude:: ../dockerfiles/OpenCMISS/base-notebook/Dockerfile
   :language: dockerfile
   :linenos:

Building images
---------------
docker build --progress plain -t opencmis-iron:1.0-minimal-ssh .


SSH into running docker container
---------------------------------
.. code-block:: bash

  echo 'jovyan:opencmiss' | chpasswd
  # Start ssh server
  sudo /usr/sbin/sshd -D

  ssh jovyan@localhost -p 1000

Run conda python from an ssh shell
----------------------------------
.. code-block:: bash

  /opt/conda/bin/python

Install python packages
-----------------------

.. code-block:: bash

  /opt/conda/bin/pip install --user seaborn


Pycharm Environmental variables
-------------------------------

.. code-block:: bash

  PYTHONUNBUFFERED=1;PYTHONPATH=/home/jovyan/opencmiss-build/opencmiss/install/lib/python3.8/opencmiss.iron:/home/jovyan/work/mesh-tools:/home/jovyan/work/morphic


Loading private docker images
-----------------------------

.. code-block:: bash

  cd path/to/dockerfile
  docker build --progress plain -t opencmis-iron:1.0-minimal-ssh .
  docker save -o opencmis-iron:1.0-minimal-ssh.tar opencmis-iron:1.0-minimal-ssh


Enter the following command:

.. code-block:: bash

  docker load --input "Z:\Software\Dockers\Saved images\opencmis-iron:1.0-minimal-ssh.tar"

replacing ```Z:\``` in the above command with the drive letter of your mounted eResearch drive.
  
.. Note::

  This step will take some time.