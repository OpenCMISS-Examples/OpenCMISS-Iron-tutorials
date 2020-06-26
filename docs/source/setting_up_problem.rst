Setting up an OpenCMISS-Iron problem from scratch
=================================================

This section demonstrates how an OpenCMISS-Iron problem can be setup from scratch in python. The code excerpts in this section can be run interactively by entering it directly into the Python interpreter, which can be started by running python in a terminal.

.. note::
   The python code in this tutorial follows the `Google python style guide <http://google.github.io/styleguide/pyguide.html/>`_, which is based on the `PEP8 standard <https://www.python.org/dev/peps/pep-0008/>`_.

Loading OpenCMISS-Iron library
------------------------------

In order to use OpenCMISS we have to first import the opencmiss.iron module from the opencmiss package:

  .. code-block:: python

    from opencmiss.iron import iron

Assuming OpenCMISS has been correctly built with the Python bindings by following the instructions in the programmer documentation, we can now access all the OpenCMISS functions, classes and constants under the iron namespace.

The next section describes how we can interact with the OpenCMISS-Iron library through an object-oriented API.

OpenCMISS-Iron objects
----------------------


