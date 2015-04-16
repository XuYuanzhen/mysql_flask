# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify, json
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:passwords@localhost/web12306'




class session(db.Model):
  __tablename__ = 'web12306'
  user_id = db.Column(db.String(100), primary_key = True)
  user_email = db.Column(db.String(100))
  user_pass = db.Column(db.String(100))
  user_nic = db.Column(db.String(100))
  user_phone = db.Column(db.String(100))
  user_name = db.Column(db.String(100))





@app.route('/scan/<user_id>', methods=['GET'])
def scan(user_id):
     result = session.query.filter_by(user_id=user_id).first()
     if result is None:
            json_result={'user_id':None}
            return json.dumps(json_result,ensure_ascii=False)
     else:
            json_result = {'user_id': result.user_id, 'user_email': result.user_email, 'user_pass': result.user_pass, 'user_nic': result.user_nic, 'user_phone': result.user_phone, 'user_name': result.user_name}
            return json.dumps(json_result,ensure_ascii=False)


@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 8080, debug=True)
