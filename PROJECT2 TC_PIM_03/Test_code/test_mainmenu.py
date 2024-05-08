import pytest

from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestHeader:
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

    def getTextBYXpath(self, locator):
        return self.driver.find_elements(by=By.XPATH, value=locator)

    def test_mainMenu(self,boot):
        try:
            # THis code is used to find and fill the username
            self.fillText(locator.WebLocator().usernameLocator, data.WebData().username)
            # This code is used to find and fill the password
            self.fillText(locator.WebLocator().passwordLocator, data.WebData().password)
            # This code is used to find the path and click the login button
            self.clickButton(locator.WebLocator().loginLocator)
            # This code is used to click the Admin
            self.clickButton(locator.WebLocator().adminLocator)

            a = self.getTextBYXpath(locator.WebLocator().optionsLocator)

            for j in a:
                print(j.text)
            print("mainMenu on Admin Page are displayed")
        except NoSuchElementException as e:
            print(e)