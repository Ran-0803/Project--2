import pytest


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Datas import data
from Locators import locator


class Test_resetcode:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.WebData().url)  # this code is used to get the url from the data
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # this code is used to for explicit wait
        yield
        self.driver.quit()
    def fillText(self, locator, textvalue):
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        element.clear()
        element.send_keys(textvalue)

    def clickButton(self, locator):
        self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()

    def test_fillForm(self,boot):

            # This code is used to find the path and fill the username
            self.fillText(locator.WebLocator().usernameLocator, data.WebData().username)
            # This code is used to click Forgot your Password
            self.clickButton(locator.WebLocator().fypLocator)
            # This code is used to enter the username
            self.fillText(locator.WebLocator().UserNameLocator, data.WebData().username)
            # This code is used to click the reset password button
            try:
                self.clickButton(locator.WebLocator().resetPasswordLocator)
            except NoSuchElementException as e:
                print(e)
            # This code is used to check whether the link is sent for reset
                if self.driver.current_url == data.WebData().resetCodeURL:
                    print("Reset Password link sent Successfully")
                else:
                    print("error")
