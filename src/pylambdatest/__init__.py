from pylambdatest.BaseContext import BaseContext as BaseContext
from pylambdatest.BaseLambdaTest import BaseLambdaTest as BaseLambdaTest
from pylambdatest.AlexaLambdaTest import AlexaLambdaTest as AlexaLambdaTest
from pylambdatest.APIGatewayLambdaTest import APIGatewayLambdaTest as APIGatewayLambdaTest
from pylambdatest.CloudFormationLambdaTest import CloudFormationLambdaTest as CloudFormationLambdaTest


def create_test(event_type = 'default', event_data = {}):
	test_dictionary = {
		'default' : BaseLambdaTest,
		'alexa' : AlexaLambdaTest,
		'apigateway' : APIGatewayLambdaTest,
		'cloudformation' : CloudFormationLambdaTest
	}

	event_object = test_dictionary[event_type]()
