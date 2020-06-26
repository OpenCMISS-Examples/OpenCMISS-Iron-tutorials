
Setting up an OpenCMISS-Iron problem from scratch
=================================================

This section demonstrates how an OpenCMISS-Iron problem can be setup from scratch in python. The code excerpts in this section can be run interactively by entering it directly into the Python interpreter, which can be started by running python in a terminal. The complete python code can be found in :download:`laplace_equation.py <../../src/python/laplace_equation.py>` in the `src/python/` folder.

.. note::
   The python code in this tutorial follows the `Google python style guide <http://google.github.io/styleguide/pyguide.html/>`_, which is based on the `PEP8 standard <https://www.python.org/dev/peps/pep-0008/>`_.

Loading OpenCMISS-Iron library
------------------------------

In order to use OpenCMISS we have to first import the opencmiss.iron module from the opencmiss package:

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START imports
   :end-before: #DOC-END imports

Assuming OpenCMISS has been correctly built with the Python bindings by following the instructions in the programmer documentation, we can now access all the OpenCMISS functions, classes and constants under the iron namespace.

The next section describes how we can interact with the OpenCMISS-Iron library through an object-oriented API.

OpenCMISS-Iron objects
----------------------

Creating and destroying objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Every OpenCMISS-Iron object can be created using the following steps that are illustrated for creating a coordinate system object:


1. Create an instance of the class of interest from the iron module, ie :python:`instance = iron.Class_name()`.

  .. code-block:: python

    coordinate_system = iron.CoordinateSystem()

2. Set default attributes of the object using the :python:`CreateStart` method. This requires the user to provide an identifier that is unique for each object class. This identifier is typically termed a user number.

  .. code-block:: python

    coordinate_system_user_number = 1
    coordinate_system.CreateStart(coordinate_system_user_number)

3. Customise the attributes of the object by calling class methods.

  .. code-block:: python

    coordinate_system.DimensionSet(3)


4. Finalise the object. An object cannot be used until it is finalised.

  .. code-block:: python

    coordinate_system.CreateFinish()


Once finalised, the parameters of the object cannot typically be modified. In order to modify the object, either another object needs to be defined with a different user number, or the object needs to be destroyed as shown below:

  .. code-block:: python

    coordinate_system.Destroy()


Using objects
~~~~~~~~~~~~~

Setting up model geometry
-------------------------

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START coordinate system
   :end-before: #DOC-END coordinate system

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START region
   :end-before: #DOC-END region

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START basis
   :end-before: #DOC-END basis

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START mesh parameters
   :end-before: #DOC-END mesh parameters

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START generated mesh
   :end-before: #DOC-END generated mesh

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START decomposition
   :end-before: #DOC-END decomposition

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START geometric field
   :end-before: #DOC-END geometric field

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START update geometric parameters
   :end-before: #DOC-END update geometric parameters

Setting up physics
------------------

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START equation set
   :end-before: #DOC-END equation set

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START dependent field
   :end-before: #DOC-END dependent field

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START initialise dependent field
   :end-before: #DOC-END initialise dependent field

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START equations
   :end-before: #DOC-END equations

Setting up the problem
----------------------

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START problem
   :end-before: #DOC-END problem

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START control loops
   :end-before: #DOC-END control loops

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START problem solver
   :end-before: #DOC-END problem solver

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START solver equations
   :end-before: #DOC-END solver equations

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START boundary condition nodes
   :end-before: #DOC-END boundary condition nodes

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START boundary conditions
   :end-before: #DOC-END boundary conditions

Solving the problem
-------------------

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START solve
   :end-before: #DOC-END solve

Exporting solutions
-------------------

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START fieldml export
   :end-before: #DOC-END fieldml export

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START exfile export
   :end-before: #DOC-END exfile export

Finalising OpenCMISS-Iron
-------------------------

.. literalinclude:: ../../src/python/laplace_equation.py
   :language: python
   :linenos:
   :start-after: #DOC-START finalise
   :end-before: #DOC-END finalise


