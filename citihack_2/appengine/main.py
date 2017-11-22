import logging, math, random

from flask import Flask, make_response
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

f = open('sqrt.py', 'r')

boilerplate = f.read()

def sqrt_reference(x):
	return math.sqrt(x)

parser = reqparse.RequestParser()
parser.add_argument('testable')

class TestSolution(object):
	"""docstring for TestSolution"""
	def __init__(self, example, testable):
		super(TestSolution, self).__init__()
		self.testable_function = testable.encode('ascii','ignore')
		self.example_function = example
		exec 'self.testable_function = ' + self.testable_function

	def test(self):
		for n in [random.randrange(0,50) for x in range(10)]:
			# print(type(self.testable_function))
			# print(type(self.example_function))
			if self.testable_function(n) != self.example_function(n):
				return False



class Index(Resource):
    def get(self):
        return {'hello': 'world'}


class TestList(Resource):
    def get(self):
        return {'Square Root': '/1', 'Sorting Algorithm':'/2','Shuffle algorithm':'/2'}

class Submit(Resource):
	def post(self,test_no):
		args = parser.parse_args()
		# print(args['testable'])

		solution = TestSolution(example=sqrt_reference ,testable=args['testable'])

		if solution.test() == False:
			return False

		return True

class SquareRoot(Resource):
	def get(self):
		return {'name':'Square Root Test',
		'description':'This test is designed to test the candidate\'s ability to implement the algorithm for a square root.',
		'boilerplate':boilerplate}
		

api.add_resource(Index, '/')
api.add_resource(TestList, '/tests/')
api.add_resource(SquareRoot, '/tests/1')
api.add_resource(Submit, '/submit/<test_no>')
		
@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


print('it runs')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
