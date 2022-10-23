from flask import Flask, render_template, jsonify
from models import db
from flask_cors import CORS

from api import api

# Flask本体
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000/*"}})

# ファイルから設定を読み込む
app.config.from_pyfile('conf.cfg')

# DB初期化
db.init_app(app)

# Blueprint登録
app.register_blueprint(api)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': {
        'code': 'Not found',
        'message': 'Page not found.'
    }}), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)