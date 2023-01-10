from datetime import datetime
from flask import Blueprint, request, abort, jsonify

from models import db, User, Weapon, Game, Match, Team, MatchDetail, UsefulInfo

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

@api.route('/wepon/list', methods=['GET'])
def get_weapon_list():
    q_game_id = request.args.get('game_id', default=-1, type=int)
    if q_game_id == -1:
        weapons = Weapon.query.all()
    else:
        weapons = Weapon.query.filter_by(game_id=q_game_id)

    return jsonify({'weapons': [weapon.to_dict() for weapon in weapons]})

@api.route('/game/list', methods=['GET'])
def get_game_list():
    games = Game.query.all()

    return jsonify({'games': [game.to_dict() for game in games]})

@api.route('/match/list', methods=['GET'])
def get_match_list():

    ## TODO 認証システムを導入
    p_user_id =  request.args.get('user_id', default=-1, type=int)
    if p_user_id == -1:
        datas = db.session.query(Match, Game).filter(Match.game_id == Game.id).all()
    else:
        datas = db.session.query(Match, Game).filter(Match.game_id == Game.id).filter_by(user_id=p_user_id).all()
    
    return jsonify({'matches': [{
            "match_id": data.Match.id,
            "game_title": data.Game.title,
            "user_id": data.Match.user_id,
            "match_mode": data.Match.match_mode,
            "match_date": format(data.Match.match_date, "%Y-%m-%d %H:%M:%S"),
            "result": data.Match.result
        } for data in datas]})

@api.route('/useful_info/list', methods=['GET'])
def get_useful_list():
    datas = db.session.query(UsefulInfo, User, Game).filter(UsefulInfo.user_id == User.id, UsefulInfo.game_id == Game.id).all()
    return jsonify({'useful_info': [{
        'useful_info_id': data.UsefulInfo.id,
        'user_name': data.User.user_id,
        'game_title': data.Game.title,
        'title': data.UsefulInfo.title,
        'create_date': data.UsefulInfo.create_date,
        'update_date': data.UsefulInfo.update_date,
    } for data in datas]}), 200

@api.route('/useful_info/detail', methods=['GET'])
def get_useful_detail():
    p_id = request.args.get('id', default=-1, type=int)
    datas = db.session.query(UsefulInfo, User, Game).filter(UsefulInfo.user_id == User.id, UsefulInfo.game_id == Game.id).filter_by(id=p_id)
    return jsonify({'useful_info': [{
        'useful_info_id': data.UsefulInfo.id,
        'user_name': data.User.user_id,
        'game_id': data.Game.id,
        'game_title': data.Game.title,
        'title': data.UsefulInfo.title,
        'contents': data.UsefulInfo.contents,
        'create_date': data.UsefulInfo.create_date,
        'update_date': data.UsefulInfo.update_date,
    } for data in datas]}), 200

@api.route('/useful_info', methods=['POST'])
def post_useful_info():
    payload = request.json
    p_user_id = payload.get('user_id')
    p_game_id = payload.get('game_id')
    p_title = payload.get('title')
    p_contents = payload.get('contents')

    useful_info = UsefulInfo(p_user_id, p_game_id, p_title, p_contents, datetime.now(), datetime.now())
    db.session.add(useful_info)
    db.session.commit()

    return jsonify(), 200

@api.route('/useful_info', methods=['PUT'])
def update_useful_info():
    payload = request.json
    p_id = payload.get('id')
    # p_user_id = 1
    # p_game_id = payload.get('game_id')
    p_title = payload.get('title')
    p_contents = payload.get('contents')

    useful_info = db.session.query(UsefulInfo).filter_by(id=p_id).first()

    print(useful_info.title)

    useful_info.title = p_title
    useful_info.contents = p_contents
    useful_info.update_date = datetime.now()

    print(useful_info.title)

    db.session.commit()

    return jsonify(), 200

@api.route('/match', methods=['POST'])
def post_match():
    payload = request.json
    p_game_id = payload.get('game_id')
    p_user_id = payload.get('user_id')
    p_match_date = payload.get('match_date')
    p_charactor_id = payload.get('charactor_id')
    p_member_count = payload.get('member_count')
    p_team_members = payload.get('team_members')
    p_weapon_id1 = payload.get('weapon_1')
    p_weapon_id2 = payload.get('weapon_2')
    p_kill_count = payload.get('kill_count')
    p_assist_count = payload.get('assist_count')
    p_damage = payload.get('damage')
    p_rank = payload.get('rank')
    p_rank_point = payload.get('rankpoint')
    p_memo = payload.get('memo')

    print(payload)
    # match テーブル登録
    match = Match(p_game_id, p_user_id, p_match_date, datetime.now())
    db.session.add(match)
    db.session.commit()
    print(match.id)

    # teamテーブル登録
    for team_member in p_team_members:
        team = Team(match.id, team_member['name'], team_member['charactor_id'], team_member['weapon_main_id'], team_member['weapon_sub_id'], datetime.now())
        db.session.add(team)
        db.session.commit()

    # match detail テーブル登録
    match_detal = MatchDetail(match.id, p_charactor_id, p_member_count, p_weapon_id1, p_weapon_id2, p_kill_count, p_assist_count, p_damage, p_rank, p_rank_point, p_memo, datetime.now())
    db.session.add(match_detal)
    db.session.commit()

    return jsonify(), 200
