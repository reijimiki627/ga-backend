from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # テーブル名
    __tablename__ = 'user'

    print("check.")
    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'password': self.password,
            'create_date':  self.create_date
        }