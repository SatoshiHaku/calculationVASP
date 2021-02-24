## 構造最適化
### INCAR

```js
SYSTEM = PFDTinPtslab

ISTART = 0
ICHARGE = 2
GGA = PE

ENCUT = 400

ISIF = 2
IBRION = 2 !optimiza structure
POTIM = 0.1
NSW = 200
EDIFFG = -0.01 !eV/A
```

### KPONTS(slabだからz方向のK点は1にしてる．バルクの時は全部同じ数の方がいい)

```js
KPOINTS created by Atomic Simulation Environment
0
Monkhorst-Pack
2 2 1
0 0 0 
```

## DOS計算
### INCAR

```js

ISTART = 1
ICHARGE = 11
GGA = PE

ENCUT = 400
ISMEAR = -1

ISPIN = 2

IBRION = -1 !optimiza structure
NSW = 0
```

### KPOINTS

```js
KPOINTS created by Atomic Simulation Environment
0
Monkhorst-Pack
4 4 1
0 0 0 
```

## バンド計算
### INCAR

```js
SYSTEM = PFDTinPtslab

ISTART = 0
ICHARGE = 2
GGA = PE

ENCUT = 400

IBRION = -1
ISPIN = 2
ISMEAR = -1  !Fermi smearing or -5 is better
SIGMA = 0.1 !Smearing width eV default value = 0.2eV
NSW = 0

LORBIT = 11
```

```js
ISTART = 1
ICHARGE = 11
GGA = PE

ENCUT = 400

IBRION = -1
ISPIN = 2
ISMEAR = -1  !Fermi smearing or -5 is better
SIGMA = 0.1 !Smearing width eV default value = 0.2eV
NSW = 0

LORBIT = 11
```

```js
ISTART = 1
ICHARGE = 11
GGA = PE

ENCUT = 400

IBRION = -1
ISPIN = 2
LSORBIT = .TRUE.
LMAXMIX = 4      ! for d-elements increase LMAXMIX to 4, f-elements: LMAXMIX = 6
SAXIS =  1 1 1   ! direction of the magn

ISMEAR = -1  !Fermi smearing or -5 is better
SIGMA = 0.1 !Smearing width eV default value = 0.2eV
NSW = 0

LORBIT = 11
```

### KPOINTS

```js
Band G-X-W-L-G
20
Line-mode
reciprocal
 0 0 0 !gamma
 0.5 0.5 0 !X

 0.5 0.5 0 !X
 0.5 0.75 0.25 !W

 0.5 0.75 0.25 !W
 0.5 0.5 0.5 !L

 0.5 0.5 0.5 !L
 0 0 0 !gamma
```

```js
 CuslabBand M-G-K-M
60
Line-mode
reciprocal
 0.5 0.5 0.0 M
 0.0 0.0 0.0 gamma

 0.0 0.0 0.0 gamma
 0.375 0.375 0.375 K

 0.375 0.375 0.375 K
 0.5 0.5 0 M
```

wget https://chromedriver.storage.googleapis.com//chromedriver_mac64.zip