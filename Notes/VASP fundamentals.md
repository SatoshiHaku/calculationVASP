## 入力ファイル
- INCAR 計算の種類，条件
- POSCAR 単位胞、原子の種類、原子の座標
- POTCAR　擬ポンテシャルについて
- KPOINTS　K点を分割する方法と数

### INCAR
  ex) DOS or 構造最適化
  https://www.vasp.at/wiki/index.php/Category:INCAR
  ここにtagの情報がある
  
### POSCAR
ここから欲しい材料のデータをとる．もしくはここから変えるcifファイル https://materialsproject.org/
  VESTAでVASP用のPOSCARファイルを出力可能　http://www.jp-minerals.org/vesta/en/

### POTCAR
  擬ポンテシャルについて
  どの擬ポテンシャルを使ったかわかるように，以下のようなシェルスクリプトを書いておくといいかも~(ぞれぞれの原子名のディレクトリの下に擬ポテンシャルを入れといて，そこからPOTCARを作った方が後からこのシェルスクリプトからどれを使ったかわかる．)
  VASPのサイトからダウンロード可能

```js
#!/bin/sh
DIR=~/projects/vasp/pp/pbe
cat ${DIR}/O/POTCAR\
    ${DIR}/Sr_sv/POTCAR\
    ${DIR}/Ti/POTCAR \
    > POTCAR
```

### KPOINTS
  K点を分割する方法と数
  分割サイズがa, b, cで同じように(例えばb=2a=4cなら、k=4, 2, 1)
  [KPOINTSの扱い方](quiver:///notes/705CD43D-374A-4F25-A55F-9DFD043A33B0)
  
  
## 出力ファイル

- OSZCAR (SCFサイクルでのエネルギーと力)
- CHGCAR (電子密度、 CHGCAR.vaspにrenameすればvestaで開くことができる)
- XDATCAR (構造最適化の場合に出力された原子座標、POSCARと同じフォーマット)
- DOSCAR (DOSのデータ)
- CONTCAR (POSCARと同じフォーマット。構造最適化等で生成される最終ステップの構造)
- WAVECAR (リスタート用の波動関数、バイナリファイル)
  
  

# INCARの例
## SCF　( + spin + structure optimize)コメントアウトされていない部分

```js
#ALGO = Fast 
#ALGOタグは、電子最小化アルゴリズムを指定するオプション
#PREC = Accurate
#PREC specifies the "precision"-mode

#For optimal performance we recommend that you set
#NPAR = 4 - approx SQRT( number of cores)
#NPAR determines the number of bands that are treated in parallel.

#(number of cores/NPAR must be integer)    
NPAR = 2

#spin 2, nonspin 1
ISPIN = 2
# ISPIN specifies spin polarization.


####SCF
ISMEAR = -5
#ISMEAR determines how the partial occupancies f_nk are set for each orbital.

```

![IMAGE](resources/E111CDB293573AECFCA81FA81D7E2EF6.jpg =1030x134)

```js
SIGMA = 0.2
#SIGMA specifies the width of the smearing in eV.

# IBRION, 1= RMM-DIIS quasi-Newton, 2=conjugate-gradient=CG
#SCF OPTIMIZATION
IBRION = 1
#-1: no update., 0: molecular dynamics.,1: ionic relaxation (RMM-DIIS).,2: ionic relaxation (conjugate gradient algorithm).....

ISIF = 3
```

![IMAGE](resources/78DCD72FB5D3727BA57E5B5058D573AE.jpg =452x328)

```js
NSW = 40
#NSW sets the maximum number of ionic steps.

####DOS
#ISMEAR = -5
#NSW = 0
#IBRION = -1

#ICHARG = 11
#ICHARG determines how VASP constructs the initial charge density.(0|1|2|4)
#自己矛盾しない計算を行うことができる．ＩＣＨＡＲＧの値に１０を加えることは、例えばＩＣＨＡＲＧ＝１１またはＩＣＨＡＲＧ＝１２（あまり便利ではない値だけど１０も可能）、電子最小化の間ずっと、電荷密度が一定に維持されることを意味する。
#LORBIT = 11
#LORBIT, together with an appropriate RWIGS, determines whether the PROCAR or PROOUT files are written.
#(RWIGS specifies the Wigner-Seitz radius for each atom type.w)
```

![IMAGE](resources/63393A8CA5EB40CE56D2C5A22A99F6F0.jpg =847x332)

ウィグナー‐ザイツ半径RWSは原子体積Vを用いて
\begin{eqnarray}
\frac{4}{3}RWS^3=\frac{V}{N}
\end{eqnarray}
の関係にある。Nは電子数．ここで，原子体積は単体元素の原子1モルが占める体積をいい，その単体の原子量を密度で除した値をもつ。

```js
##DOS range eV, same energy step as WIEN2k DOS
#EMIN = -10.0
#EMAX = 17.0
#To specify the lower boundary of the energy range for the evaluation of the DOS

#NEDOS = 1001
#specifies number of gridpoints on which the DOS is evaluated

####band dispersion
#ICHARG=11
#ISMEAR = 0
#LORBIT=11
```

