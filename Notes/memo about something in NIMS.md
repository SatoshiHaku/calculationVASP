VESTAの使いかた
BANDの書き方 KPOINTS

## ssh

入る時

```js
ssh satoshi@whisky
```

何か送るとき(localで入力)

```js
scp test.txt satoshi@whisky:/home/satoshi
```

curren dirに持ってくる時(localで入力)

```js
scp satoshi@whisky:/home/satoshi/test.txt ./
```

実行

```js
qsub run.sh
```

## VESTAの保存

Fractional coordinates(比率で定義)でexport(POSCARに)してから，座標を変えると全体がそれにともなって変化する
![IMAGE](resources/4D100F852F35FA240932C13B88F1F0D8.jpg =400x582)

Cartesian coordinate(デカルト座標)でexportしてから，座標を変えると，境界だけが変化する→これで表面状態とか作る
![IMAGE](resources/CEE31852E679A1CD4461F8B0AD96F440.jpg =400x586)





サーバーのVASPを使う時はhoge.shに

```js
python hoge.py
```

とか書いて

```js
qsub hoge.sh
```

すると，実行してくれる





