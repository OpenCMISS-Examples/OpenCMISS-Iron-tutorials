# FAQ

## Finding iron classes, methods, and class attributes

The [OpenCMISS-iron python API documentation](http://staging.opencmiss.org/documentation/apidoc/iron/latest/python/index.html) outlines the methods and attributes of iron objects.

### OpenCMISS-Iron classes 
There are two types of iron classes:
 - CMFEType - these are the classes that are used to instantiate iron objects. Attributes for these classes need to be set through the class's methods and not by directly setting attribute values.
 - Enum -  these are classes that only contain attributes, that can be directly used in CMFEType class methods. 

A list of these classes can be found by navigating to the [class Hierachy page](http://opencmiss.org/documentation/apidoc/iron/latest/python/hierarchy.html) in the python API documentation. 

Note that Enum type classes do not need to be instantiated. The attributes of these classes can be directly used, for example, as inputs to methods in CMFEType classes. For example, in the code excerpt below, the `LINEAR_LAGRANGE` attribute of the `BasisInterpolationSpecifications` Enum class is used directly as input to a method in the `iron.Basis()` CMFEType class.

```python
# import OpenCMISS-Iron with the iron namespace.
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
## Enum Class attributes

A list of attributes in each Enum class can be found by navigating to the [class Hierachy page](http://opencmiss.org/documentation/apidoc/iron/latest/python/hierarchy.html) in the python API documentation, clicking the Enum drop down list, and selecting the Enum Class of interest.