=========
Tutorials
=========

Tutorials that show how to use different features OpenCMISS-Iron are listed below:

.. toctree::
  :maxdepth: 1

  basics
  mesh_io
..  tutorials/finite_elasticity

How to run tutorials
--------------------

1. Navigate to https://github.com/OpenCMISS-Examples/OpenCMISS-Iron-tutorials
2. Download the repository as a zip as shown in the screenshot below:

  .. image:: tutorials/download_tutorials.png
    :width: 600
    :alt: Download tutorials

3. Extract the zip file.

  - If you will be running the tutorial using an OpenCMISS-Iron Docker container, move the extracted folder into a directory that can be accessed from an OpenCMISS-Iron Docker container (ie, a directory that is mounted within the container), such as your main working folder (``opt``). By default, this is located in:

  - ``~/oc/opt`` on Linux and Mac; or

  - ``C:/Users/${env:UserName}/Documents/oc/opt`` on Windows.

  See the *Installation* Section of the *Getting Started* Section for more information regarding the directories that are mounted with the Docker Containers.

4. *If you are not using OpenCMISS-Iron Dockers*:

  1. Download the :download:`threejs_visualiser.py <../../tools/threejs_visualiser.py>` python script that will be used for embedding visualisations.

  2. Specify the folder containing this script directly in the Jupyter notebook of a given tutorial by adding the following lines at the top of the notebook:

  .. code-block:: python

    import sys
    # Specify path to the threejs_visualiser.py.
    sys.path.insert(1, 'path/to/threejs_visualiser.py')

5. Open a given tutorial (located in the `tutorials` folder of the downloaded repository) in your software of choice.

.. Note::

    If you are new to OpenCMISS, we recommend using the OpenCMISS-Iron Dockers, and following the instructions for running JupyterLab (See the *Installation* and *Running* Sections of the *Getting Started* Section for more information).



