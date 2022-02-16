from pylambdatest.BaseLambdaTest import BaseLambdaTest

class CloudFormationLambdaTest(BaseLambdaTest):
	def __init__(self):
		event = {
			'RequestType' : None,
			'ServiceToken' : None,
			'ResponseURL' : None,
			'StackId' : None,
			'RequestId' : None,
			'LogicalResourceId' : None,
			'ResourceType' : None,
			'ResourceProperties' : {}
		}
		super().__init__(self, event, {})