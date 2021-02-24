まず.bashrcに以下をいれた(プロキシの設定)

```js
export http_proxy="http://wwwout.nims.go.jp:8888"
export https_proxy=$http_proxy
```

~/.gitconfigを作って下記を入力

```js
[http]
     proxy = http://wwwout.nims.go.jp:8888
     sslVerify = false
[https]
     proxy = http://wwwout.nims.go.jp:8888
```

上の設定をしないとプロキシのせいでgit cloneができなかった

そしてpyenvを入れて

```js
 git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

.bash_profileに下記を追加

```js
export PATH
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export TMPDIR=/home/nashio/tmp
eval "$(pyenv init -)"
pyenv rehash
```

**ほんとはvirtualpyenv入れた方がいいのかも**

そのあと，pyenvでpython3.9.0入れようとすると

```js
Installing Python-3.9.0...
ERROR: The Python ssl extension was not compiled. Missing the OpenSSL lib?

Please consult to the Wiki page to fix the problem.
https://github.com/pyenv/pyenv/wiki/Common-build-problems


BUILD FAILED (CentOS 6.6 using python-build 1.2.22-19-g569992f)

Inspect or clean up the working tree at /home/satoshi/tmp/python-build.20210121100445.106967
Results logged to /home/satoshi/tmp/python-build.20210121100445.106967.log

Last 10 log lines:
	fi
Looking in links: /home/satoshi/tmp/tmpnnvhsr4v
Processing /home/satoshi/tmp/tmpnnvhsr4v/setuptools-49.2.1-py3-none-any.whl
Processing /home/satoshi/tmp/tmpnnvhsr4v/pip-20.2.3-py2.py3-none-any.whl
Installing collected packages: setuptools, pip
  WARNING: The script easy_install-3.9 is installed in '/home/satoshi/.pyenv/versions/3.9.0/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts pip3 and pip3.9 are installed in '/home/satoshi/.pyenv/versions/3.9.0/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-20.2.3 setuptools-49.2.1
```

こんなエラーが出てインストールできなかった．頑張れば解決できるかもしれないけど(https://qiita.com/sato_9/items/04d219618856eaaeb341)，とりあえず

```js
pyenv install anaconda3-2019.10
```

を入れておいた

ASEを入れて　https://wiki.fysik.dtu.dk/ase/install.html

```js
pip install --upgrade --user ase
```

numpy, scipy and matplotlibを最新版にした

```js
[satoshi@whisky ~]$  pip install --upgrade --user numpy scipy matplotlib
....
Successfully installed matplotlib-3.3.3 numpy-1.19.5 scipy-1.6.0
```