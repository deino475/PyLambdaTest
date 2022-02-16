from pylambdatest.BaseLambdaTest import BaseLambdaTest

class AlexaLambdaTest(BaseLambdaTest):
    def __init__(self):
        event = {
            'header' : {
                'payloadVersion' : None,
                'namespace' : None,
                'name' : None
            },
            'payload' : {
                'switchControlAction' : None,
                'appliance' : {
                    'applianceId' : None,
                    'additionalApplianceDetails' : {}
                },
                "accessToken" : None
            }
        }
        context = {}
        super().__init__(event, context)

