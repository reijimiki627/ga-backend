# ga-backend
## インストール
* Python(3.8)

## アプリ構築手順(初回のみ)
* Djangoインストール`python -m pip install Django`
* バージョン確認`python -m django --version`
* プロジェクトの作成`django-admin startproject django-app`
* アプリケーションの作成`python manage.py startapp restapi`

## REST APIアプリの構築(初回のみ)
* modelsの定義(/restapi/models.py)
* settings.pyにアプリケーションの追加
  * INSTALLED_APPSに`restapi`を追加
* データベースのマイグレート(おそらくmodelの更新の度実行)
  * `python manage.py makemigrations`
  * `python manage.py migrate`
  * 参考)migrate実行ログ
* admin.pyに以下のコードを追加
  * `admin.site.register(UserInfo)`
* 管理アカウントの作成`python manage.py createsuperuser`
* restapiframeworkのインストール`pip install djangorestframework`
* 以下のコンポーネントを定義する
  * Serializer(/restapi/serializer.py)
  * ViewSets(/restapi//views.py)
  * Router(/restapi/urls.py)

### migrate実行ログ
```
mikireiji@rmikis-MBP ga-backend % python manage.py makemigrations   
Migrations for 'restapi':
  restapi/migrations/0001_initial.py
    - Create model UserInfo
mikireiji@rmikis-MBP ga-backend % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, restapi, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying restapi.0001_initial... OK
  Applying sessions.0001_initial... OK
```

## サーバ起動
* /ga-backend にて `python manage.py runserver`
* `http://127.0.0.1:8000/`にアクセスで画面が表示される

## user管理
* `http://localhost:8000/admin`
