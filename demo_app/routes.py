from flask_restful import Api, Resource, reqparse

from demo_app import flask_app
from demo_app.models import Band

flask_api = Api(flask_app)

bands_collection = {}


class BandsResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'name',
            type=str,
            required=True,
            location='json'
        )

        parsed_args = parser.parse_args()
        band_name = parsed_args['name']

        bands_collection[band_name] = Band(band_name)

        return {'message': 'Band %s created' % band_name}, 201


class BandResource(Resource):
    def get(self, band_name):
        try:
            band = bands_collection[band_name]
            return band.to_dict()
        except KeyError:
            return {'error': 'Band name %s not found' % band_name}, 404


class BandMembersResource(Resource):
    def post(self, band_name):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'name',
            type=str,
            required=True,
            location='json'
        )

        parser.add_argument(
            'role',
            type=str,
            required=True,
            location='json'
        )

        parsed_args = parser.parse_args()
        member_name = parsed_args['name']
        member_role = parsed_args['role']

        try:
            band = bands_collection[band_name]
        except KeyError:
            return {'error': 'Band name %s not found' % band_name}, 404

        try:
            band.add_member(member_name, member_role)
        except AttributeError:
            return {'error': 'Invalid role name'}, 400

        return {
                   'message': 'Band Member %s (%s) created' % (member_name, member_role)
               }, 201


class BandMemberResource(Resource):
    def get(self, band_name, role_name):
        try:
            band = bands_collection[band_name]
        except KeyError:
            return {'error': 'Band name %s not found' % band_name}, 404

        try:
            members = band.get_members_by_role(role_name)
        except AttributeError:
            return {'error': 'Invalid role name'}, 400

        return {
            'band_name': band_name,
            'members': members
        }


flask_api.add_resource(BandsResource, '/bands')
flask_api.add_resource(BandResource, '/bands/<string:band_name>')
flask_api.add_resource(BandMembersResource, '/bands/<string:band_name>/members')
flask_api.add_resource(BandMemberResource, '/bands/<string:band_name>/members/<string:role_name>')
