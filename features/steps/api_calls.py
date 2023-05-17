import behave.configuration
from behave import *
from features.environment import before_scenario
from behave.runner import Context, Runner
from selenium.webdriver.common.by import By
from time import sleep

@given('we are in the landing page')
def check_documentation(context):
    try:
        context.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/a').click()
        status_code = context.test_class.get_response_code(context)
        assert status_code == 200

    except AssertionError:

        response_code = context.browser.execute_script('return document.documentElement.outerHTML')
        raise AssertionError(f"Error: Unexpected response code. Expected 200, but got {response_code}.")


@when('we create password with "{number_chars}" and "{option}"')
def ask_for_password(context, number_chars, option):
    try:
        api_request = context.browser.get(f'http://wirelesschimp.pythonanywhere.com/generate-custom/{number_chars}?{option}=true')
        status_code = context.test_class.get_response_code(context)
        assert status_code == 200

    except AssertionError:
        response_code = context.test_class.get_response_code(context)
        raise AssertionError(f"Error: Unexpected response code. Expected 200, but got {response_code}.")

@then('we should get a custom password')
def check_pwd(context):
    try:
        password = context.browser.find_element(By.TAG_NAME, 'body').text
        assert password is not None
        print(password)
    except AssertionError:
        raise AssertionError(f"Error: Unexpected error, custom password wasn't fetched.")