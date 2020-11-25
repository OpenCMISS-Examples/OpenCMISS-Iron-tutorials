# Introduction

OpenCMISS-Iron (Open Continuum Mechanics, Imaging, Signal processing and System identification) is a mathematical modelling environment that enables the application of finite element analysis techniques to a variety of complex bioengineering problems. It represents a re-engineering of over 30 years' of legacy codes for finite element based computational modelling of biological systems under the mast of the Physiome Project. 

## Refactored from the ground up
The project represents a complete rewrite and overhaul of the existing CMISS computational modelling tool to take advantage of modern programming languages, data structures, and today’s range of available high performance hardware.

## Optimised simulation performance
This significant re-engineering effort represents a complete upgrade in functionality and modelling capability, particularly in terms of increased ability to optimise simulation performance on high performance, and in particular distributed, architectures.

## History
The original CMISS programme was started by Peter Hunter in 1980 in the Department of Theoretical and Applied Mechanics (TAM) at The University of Auckland and had major early contributions from Poul Nielsen and Andrew McCulloch.

The development of OpenCMISS, begun in 2005 with funding from the Wellcome Trust, has been led by Chris Bradley in Auckland and Oxford.

Since 2008 this work has evolved into a major collaborative project between the groups based in Melbourne, Stuttgart, and Auckland with input from partners in King’s College London, Barcelona, Oslo, Oxford, and Sheffield, funded by both European and national level research funding agencies.

## Supported Languages
OpenCMISS-Iron has been developed as a library with object oriented programming in mind. This can be a little confusing for people who are used to working with commercial finite element modelling packages like ANSYS or COMSOL. The best analogy for how to think about using the OpenCMISS-Iron library is that it can be used like C++ libraries. 

The core library variables, functions and classes of OpenCMISS-Iron have been written using FORTRAN 90. This is to enable effective use of high performance computing resources. However, we have also implemented python and c bindings for the FORTRAN library, which makes it easier for users to incorporate OpenCMISS-Iron functionality into their codes. 

## Design
To fully appreciate and utilise the features of OpenCMISS-Iron, we recommend familiarising yourself with the fundamental concepts and data structures of OpenCMISS-Iron. For more information, please see the following paper: [OpenCMISS: a multi-physics & multi-scale computational infrastructure for the VPH/Physiome project](https://doi.org/10.1016/j.pbiomolbio.2011.06.015).

## Contributors
Jared Collette, Nathan Andrew Isles, Gene Soudlenkov, Alan Garny, Jenny Helyanwe
Wang, Mario Enzo Habenbacher, Sander Arens, Shane Blackett, Bojan Blazevic, Peter Bier, Andy Bowery, Chris Bradley, Randall Britten, Vincent Budelmann, David Bullivant, Phani Chichapatnam, Richard Christie, Andrew Cookson, Andrew Crozier, Thiranja Prasad Babarenda Gamage, Arne Gjuvsland, Thomas Heidlauf, Andreas Hessenthaler, Alice Hung, Peter Hunter, Jagir Hussan, Chloe Irwin Whitney, Jessica Jor, Sebastian Krittian, David Ladd, Sander Land, Jack Lee, Caton Little, Xaio Bo Lu, Kumar Mithraratne, Christian Michler, Jennine Mitchell, Mylena Mordhorst, Martyn Nash, David Nickerson, Steven Niederer, Poul Nielsen, Øyvind Nordbø, David Nordsletten, Stig Omholt, Ali Pashaei, Vijayaraghavan Rajagopal, Adam Reeve, Oliver Röhrle, Ishani Roy, Ole W. Saastad, Soroush Safaei, Mark Sagar, Farzaneh Shalbaf, Vickie Shim, Matt Sinclair, Nic Smith, Hugh Sorby, Martin Steghofer, Merryn Tawhai, Mark Trew, Jon Olav Vik, Vicky Wang, Zinhou Wang, Daniel Wirtz, Alan Wu, Tim Wu, Robert Jiahe Xi, Nancy (Xiani) Yan, Hashem Yousefi, Ting Yu, Heye Zhang, Ju Zhang, Tiong Lim.
