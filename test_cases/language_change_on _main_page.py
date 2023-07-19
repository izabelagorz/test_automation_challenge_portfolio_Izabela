import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service as ChromeService


class TestLanguageChangeOnMainPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.chromeservice = ChromeService(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.chromeservice)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_language_of_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sing_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        user_login.click_on_change_language_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()