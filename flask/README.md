## DBのセットアップ（初回のみ）
* mysqlインストール：`brew install mysql@5.7`
* パスの設定：`echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.zshrc`
* ソースの追加：`source ~/.zshrc`
* パスワード設定
  * mysql起動：`brew services start mysql@5.7`
  * パスワード設定：`mysql_secure_installation`
  * パスワード：`password`

## mysql
* terminalログイン：`mysql --user=root --password`
* guiインストール：`Sequel Pro`(なんでも良い)
* テーブルの追加
  * `/flask/sql`配下のSQLを実行する

## アプリケーション起動
* pip install：`pip install -r requirements.txt`
* 起動：`python run.py`

