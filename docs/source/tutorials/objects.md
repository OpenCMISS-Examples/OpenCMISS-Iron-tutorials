# Interacting with OpenCMISS-Iron objects

This tutorial describes the architecture of the OpenCMISS-Iron library and how to interact with the library using its API's

If you are a beginner, skip to the OpenCMISS-Iron basics tutorial to see 
OpenCMISS-Iron in action, then return here to find out more about how you can 
call the OpenCMISS-Iron library to setup your own problems. 

## OpenCMISS-Iron classes 
There are two types of OpenCMISS-Iron classes:
 - CMFEType - these are the classes that are used to instantiate OpenCMISS-Iron objects. Attributes for these classes need to be set through the class's methods and not by directly setting attribute values.
 - Enum -  these are classes that only contain attributes, that can be directly used in CMFEType class methods. 

A list of these classes can be found by navigating to the [class Hierachy page](http://opencmiss.org/documentation/apidoc/iron/latest/python/hierarchy.html) in the python API documentation. 

Note that Enum type classes do not need to be instantiated. The attributes of these classes can be directly used, for example, as inputs to methods in CMFEType classes. For example, in the code excerpt below, the `LINEAR_LAGRANGE` attribute of the `BasisInterpolationSpecifications` Enum class is used directly as input to a method in the `iron.Basis()` CMFEType class.

```python
# import OpenCMISS-Iron with the OpenCMISS-Iron namespace.
from opencmiss.iron import iron 
...
# Create basis object by instantiating iron.Basis() class.
basis = iron.Basis() 
...
# Call the basis object's InterpolationXiSet method, whose input is an 
# attribute of the iron.BasisInterpolationSpecifications class.
basis.InterpolationXiSet([iron.BasisInterpolationSpecifications.LINEAR_LAGRANGE])
...

```

The python help() function can be used to determine Enum attributes that are required for each CMFEType class method.

### CMFEType Class methods

A list of methods for CMFEType iron class can be found by navigating to the [class list functions page](http://opencmiss.org/documentation/apidoc/iron/latest/python/namespaceiron.html#func-members) in the python API documentation. 
```python
help(basis.InterpolationXiSet)
# or
help(iron.Basis.InterpolationXiSet)

```
### Enum Class attributes

A list of attributes in each Enum class can be found by navigating to the [class Hierachy page](http://opencmiss.org/documentation/apidoc/iron/latest/python/hierarchy.html) in the python API documentation, clicking the Enum drop down list, and selecting the Enum Class of interest.

## Using OpenCMISS-Iron objects

### Creating objects

Every OpenCMISS-Iron object can be created using the following steps that are illustrated for creating a coordinate system object:


1. Create an instance of the class of interest from the iron module, ie `instance = iron.Class_name()`.

    `coordinate_system = iron.CoordinateSystem()`


2. Set default attributes of the object using the `CreateStart` method. This requires the user to provide an identifier that is unique for each object. This identifier is typically termed a user number.

    `coordinate_system_user_number = 1`

    `coordinate_system.CreateStart(coordinate_system_user_number)`


3. Customise the attributes of the object by calling class methods.

    `coordinate_system.DimensionSet(2)`


4. Finalise the object. An object cannot be used until it is finalised.

    `coordinate_system.CreateFinish()`


### Listing available Iron object methods

Every OpenCMISS-Iron object have more attributes and methods than are covered in this tutorial, giving the user customisation options. To quickly view the available methods, run the cell below on the particular instantiation of a class of interest. Further documentation on the classes, methods, and attributes can be found in the following [link](http://opencmiss.org/documentation/apidoc/iron/latest/python/annotated.html). For example, all the methods and attributes for the iron.CoordinateSystem() class are found [here](http://opencmiss.org/documentation/apidoc/iron/latest/python/classiron_1_1_coordinate_system.html). A direct way to obtain the documentation for a class is to use the python help() command, which will return the documentation of a particular class.

```python
import pprint
pprint.pprint(dir(iron.CoordinateSystem()))
help(iron.CoordinateSystem())
```

### Destroying objects

Once finalised, the parameters of the object cannot typically be modified. In order to modify the object, either another object needs to be defined with a different user number, or the object needs to be destroyed as shown below:

`coordinate_system.Destroy()`

