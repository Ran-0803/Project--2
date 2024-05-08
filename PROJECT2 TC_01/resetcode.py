from Datas import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ResetCode:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Explicit wait
        self.wait = WebDriverWait(self.driver, 10)

    def boot(self):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        # Explicit Wait
        self.wait.until(ec.url_to_be(data.WebData().url))

    def quit(self):
        self.driver.quit()

    def fillText(self, locator, textvalue):
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        element.clear()
        element.send_keys(textvalue)

    def clickButton(self, locator):
        self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()

    def fillForm(self):
        try:
            self.boot()
            # This code is used to find the path and fill the username
            self.fillText(locator.WebLocator().usernameLocator, data.WebData().username)
            # This code is used to click Forgot your Password
            self.clickButton(locator.WebLocator().fypLocator)
            # This code is used to enter the username
            self.fillText(locator.WebLocator().UserNameLocator, data.WebData().username)
            # This code is used to click the reset password button
            self.clickButton(locator.WebLocator().resetPasswordLocator)
            # This code is used to check whether the link is sent for reset
            if self.driver.current_url == data.WebData().resetCodeURL:
                print("Reset Password link sent Successfully")
            else:
                print("error")
        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()


obj = ResetCode()
obj.fillForm()
