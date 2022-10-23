from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # テーブル名
    __tablename__ = 'user'

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

class Weapon(db.Model):
    # テーブル名
    __tablename__ = 'weapon'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=True)
    type = db.Column(db.String(10), nullable=True)

    def __init__(self, game_id, name, type):
        self.game_id = game_id
        self.name = name
        self.type = type

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'name': self.name,
            'type':  self.type
        }

class Game(db.Model):
    # テーブル名
    __tablename__ = 'game'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=True)
    create_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, game_id, title, type):
        self.game_id = game_id
        self.title = title
        self.type = type

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'type':  self.type
        }

class Charactor(db.Model):
    # テーブル名
    __tablename__ = 'charactor'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    name = db.Column(db.String(20), nullable=True)
    type = db.Column(db.String(10), nullable=True)

    def __init__(self, game_id, name, type):
        self.game_id = game_id
        self.name = name
        self.type = type

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'name': self.name,
            'type':  self.type
        }

class Match(db.Model):
    # テーブル名
    __tablename__ = 'match'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_mode = db.Column(db.String(20), nullable=True)
    match_date = db.Column(db.DateTime, nullable=False)
    result = db.Column(db.String(20), nullable=True)
    create_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, game_id, user_id, match_mode, match_date, result, create_date):
        self.game_id = game_id
        self.user_id = user_id
        self.match_mode = match_mode
        self.match_date = match_date
        self.result = result
        self.create_date = create_date

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'user_id': self.user_id,
            'match_mode': self.match_mode,
            'match_date':  self.match_date,
            'result': self.result,
            'create_date':  self.create_date
        }

class Team(db.Model):
    # テーブル名
    __tablename__ = 'team'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    charactor_id = db.Column(db.Integer, db.ForeignKey('charactor.id'), nullable=True)
    weapon_main_id = db.Column(db.Integer, db.ForeignKey('weapon.id'), nullable=True)
    weapon_sub_id = db.Column(db.Integer, db.ForeignKey('weapon.id'), nullable=True)
    create_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, match_id, user_name, charactor_id, weapon_main_id, weapon_sub_id, create_date):
        self.match_id = match_id
        self.user_name = user_name
        self.charactor_id = charactor_id
        self.weapon_main_id = weapon_main_id
        self.weapon_sub_id = weapon_sub_id
        self.create_date = create_date

    def to_dict(self):
        return {
            'id': self.id,
            'match_id': self.match_id,
            'user_name': self.user_name,
            'charactor_id':  self.charactor_id,
            'weapon_main_id':  self.weapon_main_id,
            'weapon_sub_id':  self.weapon_sub_id,
            'create_date':  self.create_date
        }

class MatchDetail(db.Model):
    # テーブル名
    __tablename__ = 'match_detail'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    charactor_id = db.Column(db.Integer, db.ForeignKey('charactor.id'), nullable=True)
    num_of_team_member = db.Column(db.Integer, nullable=True)
    weapon_main_id = db.Column(db.Integer, db.ForeignKey('weapon.id'), nullable=True)
    weapon_sub_id = db.Column(db.Integer, db.ForeignKey('weapon.id'), nullable=True)
    num_of_kill = db.Column(db.Integer, nullable=True)
    num_of_assist = db.Column(db.Integer, nullable=True)
    damage = db.Column(db.Integer, nullable=True)
    rank = db.Column(db.String(20), nullable=True)
    rank_point = db.Column(db.Integer, nullable=True)
    memo = db.Column(db.String(20), nullable=True)
    create_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, match_id, charactor_id, num_of_team_member, weapon_main_id, weapon_sub_id, num_of_kill, num_of_assist, damage, rank, rank_point, memo, create_date):
        self.match_id = match_id
        self.charactor_id = charactor_id
        self.num_of_team_member = num_of_team_member
        self.weapon_main_id = weapon_main_id
        self.weapon_sub_id = weapon_sub_id
        self.num_of_kill = num_of_kill
        self.num_of_assist = num_of_assist
        self.damage = damage
        self.rank = rank
        self.rank_point = rank_point
        self.memo = memo
        self.create_date = create_date

    def to_dict(self):
        return {
            'id': self.id,
            'match_id': self.match_id,
            'charactor_id':  self.charactor_id,
            'num_of_team_member': self.num_of_team_member,
            'weapon_main_id':  self.weapon_main_id,
            'weapon_sub_id':  self.weapon_sub_id,
            'num_of_kill':  self.num_of_kill,
            'num_of_assist':  self.num_of_assist,
            'damage':  self.damage,
            'rank':  self.rank,
            'rank_point':  self.rank_point,
            'memo':  self.memo,
            'create_date':  self.create_date
        }

class UsefulInfo(db.Model):
    # テーブル名
    __tablename__ = 'useful_info'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    contents = db.Column(db.String(500), nullable=True)
    create_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, game_id, title, contents, create_date, update_date):
        self.user_id = user_id
        self.game_id = game_id
        self.title = title
        self.contents = contents
        self.create_date = create_date
        self.update_date = update_date

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'game_id': self.game_id,
            'title': self.title,
            'contents':  self.contents,
            'create_date':  self.create_date,
            'update_date':  self.update_date
        }
