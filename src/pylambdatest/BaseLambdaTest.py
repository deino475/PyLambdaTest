import os
import warnings

class BaseLambdaTest:
    def __init__(self, event = {}, context = None):
        self.event = event
        self.context = context
        self.environment = {}

    def test(self, func):

        self.context.start()
        response = func(self.event, self.context)
        self.context.end()

    def set_environment_var(self, key, value):
        self.environment[str(key)] = str(value)