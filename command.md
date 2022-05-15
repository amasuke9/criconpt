■環境構築
フォルダ作成
C:\dev\cricon

仮想環境
C:\dev\cricon>python -m venv myvenv

仮想環境の実行
myvenv\Scripts\activate

Djangoのインストール
python -m pip install --upgrade pip
requirements.txt　を作成
pip install -r requirements.txt

■プロジェクト作成
django-admin.exe startproject mysite .

settings.py の修正

■DBの作成
python manage.py migrate (manage.pyファイルのあるdjangogirlsディレクトリにいる必要があります) 

■Webサーバの起動
python manage.py runserver

    http://127.0.0.1:8000/

■アプリの作成
python manage.py startapp criconpt

mysite/settings.py　の修正（INSTALLED_APPS　に追加。Django にアプリ利用を設定）　
    'criconpt.apps.CriconptConfig',

■モデルの定義
まだ具体的にはこれから・・・ロジックを書く？テスト方法も理解必要。
画面作ってから作るようにする。★

■Gitの登録
git init
git config --global user.name "amasuke"
git config --global user.email amachan20145@gmail.com

.gitignore の作成

■Git プッシュ
git status
git add --all .
git commit -m "Criconpt app, first commit"

■Git hub でプロジェクト作成
https://github.com/amasuke9/criconpt.git

git remote add origin https://github.com/amasuke9/criconpt.git
git push -u origin master

PythonAnywhere　への登録は後で実施する。★

■URL の変更

ptform.html を作る。そのために設定を変更する。
変更場所
    新規作成
    C:\dev\cricon\criconpt\templates\criconpt\ptform.html
    変更
    C:\dev\cricon\criconpt\urls.py
    C:\dev\cricon\criconpt\views.py

PTフォームのページが表示できた。

■Git プッシュ
git status
git add --all .
git commit -m "PT page first commit"