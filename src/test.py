from pylambdatest import create_test
import time
import os

def post_route(event, context):
    time.sleep(2)
    print(os.getenv('APPLICATION'))
    return {
        'statusCode' : 200,
        'body' : 'This is a success'
    }


new_test = create_test('apigateway')
new_test.set_environment_var('APPLICATION','re')
print(type(new_test))

response = new_test.test(post_route)
print(new_test.context.execution_time())
print(response)