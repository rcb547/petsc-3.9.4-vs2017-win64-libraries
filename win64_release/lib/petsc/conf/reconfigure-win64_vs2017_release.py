#!/usr/bin/python
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure
  configure_options = [
    '--download-f2cblaslapack=1',
    '--useThreads=0',
    '--with-64-bit-indices=0',
    '--with-cc=win32fe cl',
    '--with-clanguage=C++',
    '--with-cxx=win32fe cl',
    '--with-debugging=0',
    '--with-endian=little',
    '--with-fc=0',
    '--with-mpi-include=/cygdrive/c/Microsoft_HPC_Pack_2012/Inc',
    '--with-mpi-lib=/cygdrive/c/Microsoft_HPC_Pack_2012/Lib/amd64/msmpi.lib',
    '--with-mpiexec=/cygdrive/c/Microsoft_HPC_Pack_2012/Bin/mpiexec.exe',
    '--with-single-library=1',
    '--with-windows-graphics=0',
    '--with-x=0',
    'PETSC_ARCH=win64_vs2017_release',
  ]
  configure.petsc_configure(configure_options)
