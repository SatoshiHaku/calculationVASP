インストールしたanacondaの環境に設定する

```js
source activate my_pymatgen
```

vaspの結果はvasprun.xmlに全て入ってる
例えばバンド構造はget_band_structureで持ってこれる

```js
>>> from pymatgen.io.vasp import Vasprun, BSVasprun
>>> from pymatgen.electronic_structure.plotter import BSPlotter
>>>
>>> v = BSVasprun("vasprun.xml")
>>> bs = v.get_band_structure(kpoints_filename="KPOINTS",line_mode=True)
>>> plt = BSPlotter(bs)
>>> plt.get_plot(vbm_cbm_marker=True,ylim=(-3,3))
```

例えば，badnstrに入れたら

```js
>>> BSV = BSVasprun("vasprun.xml")
>>> bandstr = BSV.get_band_structure(kpoints_filename="KPOINTS",line_mode=True)
```

分かりやすくいろんな値を取り出せる

```js
>>> bandstr.is_spin_polarized
True
>>> bandstr.efermi
10.63581843
>>> bandstr.nb_bands
96
```

バンド構造見たかったら

```js
>>>plt = BSPlotter(bandstr)
>>>plt.get_plot(vbm_cbm_marker=True,ylim=(-3,3))
>>>plt.show()
```

![IMAGE](resources/2DF51F581EA71EEDC15DA2A1FD7EBF92.jpg =600x766)
![IMAGE](resources/124830B3BA77037803FEEF1B40F34E79.jpg =600x778)


![IMAGE](resources/6AF607139BE73DC47D99AB743C0BCCB6.jpg =600x791)
![IMAGE](resources/F1BA24F7BE439326B50AD3C8D1FA98AF.jpg =600x779)