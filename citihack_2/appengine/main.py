# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

from flask import Flask, make_response
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

test1 = ''



# @app.route('/')
# def hello():
#     return 'Hello World!'


# @app.errorhandler(500)
# def server_error(e):
#     # Log the error and stacktrace.
#     logging.exception('An error occurred during a request.')
#     return 'An internal error occurred.', 500
# # [END app]

boilerplate = ''


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class TestList(Resource):
    def get(self):
        return {'Square Root': '/1', 'Sorting Algorithm':'/2','Shuffle algorithm':'/2'}

class Submit(Resource):
	def post(self):
		return {'test':'test'}

class SquareRoot(Resource):
	def get(self):
		return {'name':'Square Root Test',
		'description':'This test is designed to test the candidate\'s ability to implement the algorithm for a square root.',
		'boilerplate':boilerplate}
		

api.add_resource(HelloWorld, '/')
api.add_resource(TestList, '/tests/')
api.add_resource(SquareRoot, '/tests/1')
api.add_resource(Submit, '/submit/<test_no>')

# @app.errorhandler(404)
# def page_not_found(e):
#     """Return a custom 404 error."""
#     return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


print('it runs')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
