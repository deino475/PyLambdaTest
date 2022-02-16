from pylambdatest.BaseLambdaTest import BaseLambdaTest

class APIGatewayLambdaTest(BaseLambdaTest):
	def __init__(self, resource):
		event = {
			'resource' : resource,
			'path' : None,
			'httpMethod' : None,
			'requestContext' : None,
			'headers' : None,
			'multiValueHeaders' : None,
			'queryStringParameters' : None,
			'multiValueQueryStringParameters' : None,
			'pathParameters' : None,
			'stageVariables' : None,
			'body' : None,
			'isBase64Encoded' : False
		}
		context = {}
		super().__init__(event, context)
