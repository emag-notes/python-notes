# coding: utf-8
import shelve
from datetime import datetime

from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

DATA_FILE = 'guestbook.dat'


def save_data(name, comment, created_at):
    """投稿データを保存します
    """
    # shelve モジュールでデータベースファイルを開きます
    database = shelve.open(DATA_FILE)
    # データベースに greeting_list がなければ、新しくリストを作ります
    if 'greeting_list' \
       '' not in database:
        greeting_list = []
    else:
        # データベースからデータを取得します
        greeting_list = database['greeting_list']
    # リストの先頭に投稿データを追加します
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'created_at': created_at
    })
    # データベースを更新します
    database['greeting_list'] = greeting_list
    # データベースファイルを閉じます
    database.close()


def load_data():
    """投稿されたデータを返します
    """
    # shelve モジュールでデータベースファイルを開きます
    database = shelve.open(DATA_FILE)
    # greeting_list を返します。データがなければカラのリストを返します
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list


@application.route('/')
def index():
    """トップページ
    テンプレートを使用してページを表示します
    """
    # 投稿データを読み込みます
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)


@application.route('/post', methods=['POST'])
def post():
    """投稿用URL
    """
    # 投稿されたデータを取得します
    name = request.form.get('name')
    comment = request.form.get('comment')
    created_at = datetime.now()
    # データを保存します
    save_data(name, comment, created_at)
    # 保存後はトップページにリダイレクトします
    return redirect('/')


@application.template_filter('nl2br')
def nl2br_filter(s):
    """改行文字を br タグに置き換えるテンプレートフィルタ
    """
    return escape(s).replace('\n', Markup('<br/>'))


@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    """datetime オブジェクトを見やすい表示にするテンプレートフィルタ
    """
    return dt.strftime('%Y/%m/%d %H:%M:%S')


def main():
    application.run('127.0.0.1', 8000)

if __name__ == '__main__':
    # IP アドレス 127.0.0.1 の 8000 番ポートでアプリケーションを実行します
    application.run('127.0.0.1', 8000, debug=True)
