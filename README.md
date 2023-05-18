# Precompiled PETSc 3.9.4 VS2017 Windows 64 bit libraries

## Source code 

The source code was developed by the PETSc project based at Argonne National Laboratory. See https://www.mcs.anl.gov/petsc for details. The repository does not include the source code, it only includes the libraries, header and config files.

## Compiler 

These libraries were compiled with Microsoft Visual Studio 2017 Community under cygwin.

## Include files 

For release builds you should have these directories in your include path  
	- ...\include\  
	- ...\win64_release\include\  

For debug builds you should have these directories in your include path  
	- ...\include\  
	- ...\win64_debug\include\  

## Library files 

For release builds you should have this directory in your library path  
	- ...\win64_release\lib\  

For debug builds you should have this directory in your library path  
	- ...\win64_debug\lib\  

Then link with these libraries  
	- libf2clapack.lib (the non-optimised LAPACK library)  
	- libf2cblas.lib (the non-optimised BLAS library)  
	- libpetsc.lib (the PETSc library)  

## MPI flavour  
	The libraries were compiled using the Microsoft_HPC_Pack_2012 MPI library.  Therefore you need to install Microsoft_HPC_Pack_2012 and link to ...\Microsoft_HPC_Pack_2012\Lib\amd64\msmpi.lib.

## Cygwin build script

For anyone who cares, here is the cygwin build script.

```bash  

#!/bin/bash

#Visual Studio
#Run from the vs2017 command prompt and set up the command line compile environment
	#C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat x86_amd64
#Run cygwin from that CMD window
	#C:\cygwin64>Cygwin-mintty.bat

#In windows (VC2017) must link with the Multi-Thread static runtime library /MT option
#see Configuration Properties | C/C++ | Code Generation | Runtime Libraries | Multi-thread (/MT)

export PETSC_DIR=/cygdrive/z/code/third_party/petsc-3.9.4

./configure PETSC_ARCH=win64_vs2017_release \
  --with-cc='win32fe cl' \
  --with-cxx='win32fe cl' \
  --with-clanguage=C++ \
  --with-fc=0 \
  --download-f2cblaslapack=1 \
  --with-mpi-include=/cygdrive/c/Microsoft_HPC_Pack_2012/Inc \
  --with-mpi-lib=/cygdrive/c/Microsoft_HPC_Pack_2012/Lib/amd64/msmpi.lib \
  --with-mpiexec=/cygdrive/c/Microsoft_HPC_Pack_2012/Bin/mpiexec.exe \
  --with-64-bit-indices=0 \
  --with-single-library=1 \
  --with-endian=little \
  --with-debugging=0 \
  --with-x=0 \
  --with-windows-graphics=0

make PETSC_DIR=/cygdrive/z/code/third_party/petsc-3.9.4 PETSC_ARCH=win64_vs2017_release all




```

