from selenium import webdriver
from behave import *
from time import sleep
import requests
class TestMethods:

    @fixture
    def selenium_browser_firefox(self, context):
        # Configuración del perfil del navegador Firefox para obtener el código de respuesta
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('webdriver.log.file', '../../log_file.log')  # Ruta al archivo de registro de Selenium
        context.browser = webdriver.Firefox(firefox_profile=firefox_profile)
        yield context.browser
        context.browser.quit()

    @fixture
    def coolpass_log(self, context):
        context.browser.get("http://wirelesschimp.pythonanywhere.com/")
        sleep(2)
        print('CoolPass opened!')
    @fixture
    def get_response_code(self, context):
        current_web = context.browser.current_url
        check_request = requests.get(current_web)
        status_code = check_request.status_code
        return status_code

