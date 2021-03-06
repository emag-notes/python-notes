===============================================================================
ゲストブックアプリ
===============================================================================

目的
===============================================================================

Web ブラウザでコメントを投稿する Web アプリケーションの練習。

ツールのバージョン
===============================================================================

:Python: 2.7.12
:pip: 8.1.2
:virtualenv: 15.0.3

インストールと起動方法
===============================================================================

リポジトリからコードを取得し、その下に virtualenv 環境を用意します::

  $ git clone https://github.com/emag-notes/python-notes
  $ cd python-professional-programming/ch03
  $ virtualenv .venv
  $ source .venv/bin/activate
  (.venv)$ pip install .
  (.venv)$ guestbook
    * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)

開発手順
===============================================================================

開発用インストール
-------------------------------------------------------------------------------

1. チェックアウトする
2. 以下の手順でインストールする::


  (.venv)$ pip install -e .


依存ライブラリ変更時
-------------------------------------------------------------------------------

1. ``setup.py`` の ``install_requires`` を更新する
2. 以下の手順で環境を更新する::


  (.venv)$ virtualenv --clear .venv
  (.venv)$ pip install -e .
  (.venv)$ pip freeze > requirements.txt

3. setup.py と requirements.txt をリポジトリにコミットする
