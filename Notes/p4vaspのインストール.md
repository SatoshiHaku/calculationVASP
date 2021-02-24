## Ubuntu (Linux)
ディレクトリ作って

```js
cd P4vasp/
```

そこにp4vasp-0.3.30をダウンロードして解凍(tar)

install/にあるinstall_ubuntu_dependencies.shを実行

```js
sh install_ubuntu_dependencies.sh
```

一個上の階層でインストール

```js
sudo make install
```

これだけだとなぜかp4vaspが入らなかった．意味不
以下のように無理やり入れた

```js
sudo apt-get update
sudo apt-get install p4vasp
```

ちなみに実行は

```js
p4v
```

## mac OS
関連ファイルが入らなかった
推奨されているmacportsとか，pipとかbrewでも入れてみたけど，PyGtkが入らず，よくわからないので，parallel desktopにUbuntu入れて上記のように構築した