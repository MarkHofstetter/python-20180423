from flask_restful import Resource, Api
import DB

api = Api(app)
class FlaskrApi(Resource):
    def get(self):
        db = Model.DB()
        energy = db.sq(Model.Energy).all()
        list_entries = [list(row) for row in energy]
        return list_entries

api.add_resource(FlaskrApi, '/api')
