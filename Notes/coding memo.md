import pyprocar
pyprocar.bandsplot('PROCAR',outcar='OUTCAR',elimit=[-10,10],mode='parametric',cmap='jet',kticks=[0,19,39,59,79],knames=['G','X','W','L','G'],orbitals=[0,1,2,3])

import pyprocar
pyprocar.bandsplot('PROCAR',outcar='OUTCAR',elimit=[-10,10],mode='parametric',cmap='jet',kticks=[0,39,79,119,159],knames=['$M$','$\Gamma$','$K$','$M$'],orbitals=[0,1,2,3])