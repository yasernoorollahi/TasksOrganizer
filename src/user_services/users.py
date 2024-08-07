from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app =Flask(__name__)
api = Api(app)


users={}

class UserResource(Resource):
    def post(self):
        return{'data':'user data'}
        # user_id= request.json.get('id')
        # user_data = request.json.get('data')
        # users[user_id]= user_data
        # return jsonify({'id': user_id, 'data': user_data})
    

api.add_resource(UserResource, '/users')

if __name__ == '__main__':
    app.run(debug=True, port=50001)