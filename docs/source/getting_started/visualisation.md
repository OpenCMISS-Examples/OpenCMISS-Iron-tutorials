# Visualising simulation results

There are a number of approaches for visualising simulation results from OpenCMISS-Iron.

## Cmgui
OpenCMISS-Iron support export of meshes and fields in `.exelem` and `.exnode` files for visualisation in the Cmgui 3D visualisation software package. This isdemonstrated in the *Basics* tutorial. 

### Installing Cmgui
This software can be downloaded from the [Physiome Project website](http://physiomeproject.org/software/opencmiss/cmgui/download).

### Cmgui documentation
 
Documentation for cmgui can be found from the following sources:

- [Main documentation](https://abi-software-book.readthedocs.io/en/latest/Cmgui/)
- [Cmgui commands](http://cmiss.bioeng.auckland.ac.nz/development/help/cmgui/gfx/index.html) 
- [Cmgui examples](http://cmiss.bioeng.auckland.ac.nz/development/examples/a/index_thumbs.html)
- [Legacy documentation](https://www.cmiss.org/cmgui)

``` Note:: For OpenCMISS-Iron Docker installations, install cmgui on your host machine. The meshes exported from running python scripts/Jupyter notebooks in the OpenCMISS-Iron Docker containers will be accessible from the host machine for visualisation. See the *Docker installation Section* of the documentation for more information about how to access folders mounted within Docker container from the host machine.
```   

## Pythreejs
The OpenCMISS-Iron tutorials provide basic support for visualising simulation results in html using [Pythreejs](https://pythreejs.readthedocs.io/en/stable/). These html visualisations can be embedded in Jupyter notebooks, or generate standalone html files when run through a python interpreter. This is demonstrated in the *Basics* tutorial.

## VTK
The OpenCMISS-Iron tutorials provide basic scripts for creating VTK objects from OpenCMISS-Iron meshes. These VTK files can then be visualised in almost all visualisation software (e.g. [paraview](https://www.paraview.org/)) The python [meshio](https://github.com/nschloe/meshio) module can then be used to convert these to a number of different mesh formats. `meshio 4.3.5` is already installed within the OpenCMISS-Iron Docker containers, and supports the following mesh output formats:
- Abaqus,
- ANSYS msh,
- AVS-UCD,
- CGNS,
- DOLFIN XML,
- Exodus,
- FLAC3D,
- H5M,
- Kratos/MDPA,
- Medit,
- MED/Salome,
- Nastran (bulk data),
- Neuroglancer precomputed format,
- Gmsh (format versions 2.2, 4.0, and 4.1),
- OBJ,
- OFF,
- PERMAS,
- PLY,
- STL,
- Tecplot .dat,
- TetGen .node/.ele,
- SVG (2D only, output only),
- SU2,
- UGRID,
- VTK,
- VTU,
- WKT (TIN),
- XDMF.

``` Note:: Exporting higher order elements, e.g. cubic Hermite elements,  in these formats using the meshio python module is not supported. If you want to visualise higher order elements, please use Cmgui. 
```   

``` Note:: The meshio python module: 1) only supports specific element interpolations that can be described in VTK format, and 2) has to conform to the capabilities of these file formats. Therefore, it may not be possible to export your mesh in a paricular format. For more information, consult the [meshio source code](https://github.com/nschloe/meshio/tree/master/meshio). You can browse the soruce code for the format of interest to determine what element interporlations are supported. 
```   


