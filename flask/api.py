from flask import Blueprint, request, abort, jsonify

from models import db, User

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/login', methods=['POST'])
def list_user():
    print(request)
    payload = request.json
    userId = payload.get('user_id')
    passwd = payload.get('password')
    print("userId:" + userId + ", password:" + passwd)

    user = User.query.filter_by(user_id=userId, password=passwd).first()
    # user = User.query.all()
    print("user")
    # jsonレスポンス返却
    # jsonifyにdict型オブジェクトを設定するとjsonデータのレスポンスが生成される
    if not user:
        abort(401, {'code': 'UnAuthrized', 'message': 'ログインIDまたはパスワードが正しくありません。'})

    return jsonify(user.to_dict), 200
