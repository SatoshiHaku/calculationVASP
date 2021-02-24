まずSOを入れずにscf計算を行って，そのあとにSOを入れてもう一度scf計算する
INCARは以下の感じで行けた
NBANDSはスピン縮退が解けるので，2倍にする

<font color='pink'>NSW=1</font>でもいいかも

```js
SYSTEM = Pt

GGA_COMPAT = .FALSE.
LSCALAPACK=.FALSE.

ISTART = 0
ICHARGE = 2
GGA = PE

ENCUT = 400

ALGO = Normal
ISIF = 2
IBRION = 2 !optimiza structure
POTIM = 0.015 !changed from 0.1
NSW = 200
EDIFFG = -0.01 !eV/A

NBANDS = 384
MAGMON = 0.0 1.0 0.0
ISPIN = 2
LSORBIT = .TRUE.
LMAXMIX = 4      ! for d-elements increase LMAXMIX to 4, f-elements: LMAXMIX = 6
SAXIS =  0 0 1   ! direction of the magn
```

