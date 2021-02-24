## cat
### filaAの閲覧

```js
cat fileA
```

### 入力(>)と追加(>>)

```js
cat fileA > fileB
cat fileA >> fileB
```

### 連結

```js
cat fileA fileB > fileC
```

#### オプション
#### 行番号をつけて表示

```js
cat -n fileA
```

#### 空白行を入れずに番号をつけて表示

```js
cat -b fileA
```

## サーバーになげる.shについて

```js
#!/bin/sh

#$ -S /bin/sh
#$ -cwd
#$ -V
#$ -q all.q
#$ -pe impi24 96

mpiexec.hydra -n $NSLOTS /home/appl/VASP/vasp.5.4.1/bin/vasp_std
```

6行目で全てのノードで使ってないところを使う
7行目で96コア使う

並列処理はMPIを利用している．

```js
mpiexec.hydra -n $NSLOTS
```

の部分が並列処理をするためのところ．
→#NSLOTSで#$ -pe impi24 24のコア数を読んでる．

