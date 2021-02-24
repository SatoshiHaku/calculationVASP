import pyprocar

#plot band structure M-G-K-M
pyprocar.bandsplot('PROCAR',outcar='OUTCAR',kticks=[0,39,79,119,159],knames=['M','G','K','M'],elimit=[-2,2],mode='plain',color='blue',code='vasp')

#plot 2d band structure
for e in [0,-0.3,-0.6,-1,-1.2]:
    pyprocar.fermi2D('2dband2/PROCAR', outcar='2dband2/OUTCAR', st=True, energy=e, noarrow=True, spin=1, code='vasp')
