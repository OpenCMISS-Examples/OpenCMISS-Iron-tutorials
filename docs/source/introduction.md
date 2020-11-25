# Introduction

The OpenCMISS-Iron library has been created to enable highly advanced computational modelling of biological systems. It represents a re-engineering of over 30 years' of legacy codes for finite element based computational modelling of biological systems under the mast of the Physiome Project. Therefore, to fully appreciate and utilise the features of OpenCMISS-Iron, we recommend familiarising yourself with the fundamental concepts and data structures of OpenCMISS-Iron. For more information, please see the following paper: [OpenCMISS: a multi-physics & multi-scale computational infrastructure for the VPH/Physiome project](https://doi.org/10.1016/j.pbiomolbio.2011.06.015).

OpenCMISS-Iron has been developed as a library with object oriented programming in mind. This can be a little confusing for people who are used to working with commercial finite element modelling packages like ANSYS or COMSOL. The best analogy for how to think about using the OpenCMISS-Iron library is that it can be used like C++ libraries. 

## Supported Languages
The core library variables, functions and classes of OpenCMISS-Iron have been written using FORTRAN 90. This is to enable effective use of high performance computing resources. However, we have also implemented python and c bindings for the FORTRAN library, which makes it easier for users to incorporate OpenCMISS-Iron functionality into their codes. 
