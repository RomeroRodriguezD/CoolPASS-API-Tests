from behave import *
from support.fixtures import TestMethods

# Set up before tests

def before_scenario(context, scenario):
    context.test_class = TestMethods()
    use_fixture(context.test_class.selenium_browser_firefox, context)
    use_fixture(context.test_class.coolpass_log, context)
