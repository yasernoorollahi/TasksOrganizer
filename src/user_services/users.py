from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from models import User
from common.sqlite_setup import db,init_db


app =Flask(__name__)
api = Api(app)
init_db(app)



users={}

class UserResource(Resource):
    # def post(self):
    #     user_list= User.query.first()

    #     return jsonify(user_list)
        # user_id= request.json.get('id')
        # user_data = request.json.get('data')
        # users[user_id]= user_data
        # return jsonify({'id': user_id, 'data': user_data})

    def get(self):
        user = User.query.get_or_404(1)
        # return jsonify({'id': 's', 'username': })
        return {user.id }
    

api.add_resource(UserResource, '/users')

if __name__ == '__main__':
    app.run(debug=True, port=50002)