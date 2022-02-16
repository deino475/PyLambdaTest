from pylambdatest.BaseLambdaTest import BaseLambdaTest

class CodePipelineLambdaTest(BaseLambdaTest):
	def __init__(self):
		event = {
			'CodePipeline.job' : {
				'id' : None,
				'accountId' : None,
				'data' : {
					'actionConfiguration' : {
						'configuration' : {
							'FunctionName' : None,
							'UserParameters' : None
						}
					},
					'inputArtifacts' : [],
					'outputArtifacts' : [],
					'artifactCredentials' : {}
				}
			}
		}
		super().__init__(self, event, {})