import logging

import allure
from allure_commons.types import AttachmentType

from PageObjects.LoginPO import Orange_HRM
from Utilities.logger import LogGenerator
from Utilities.readConfig import Readconfig


class Test_OrangeHRM_001:
    username = Readconfig.Getusername()
    password = Readconfig.Getpassword()
    log = LogGenerator.loggen()

# for page title
    def test_page_tital_01(self, setup):
        self.log.info("Opening the browser")
        self.log.info("Opening the URL")
        self.driver = setup
        self.log.info("Checking for the page title")
        if self.driver.title == "OrangeHRM":
            self.log.info("taking the screen shoot")
            self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot"
                                        "\\test_page_tital_01_test_page_tital_01_pass.png")
            self.log.info("opened page is matched as per requirement")
            assert True
        else:
            self.log.info("taking the screen shoot")
            self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot"
                                        "\\test_page_tital_01_test_page_tital_01_fail.png")
            self.log.info("opened page is not matched as per requirement")
            assert False

    # @allure.Severity(allure.severity_level.CRITICAL)
    def test_login_02(self, setup):
        self.log.info("Opening the web browser")
        self.log.info("navigating and opening the given URL")
        self.driver = setup
        self.lp = Orange_HRM(self.driver)
        self.log.info("Entering the username")
        self.lp.Enter_username(self.username)
        self.log.info("Entering the password")
        self.lp.Enter_Password(self.password)
        self.log.info("clicking on login button")
        self.lp.Click_Login()
        self.log.info("Checking for the login status")
        if self.lp.Login_Status() == True:
            self.log.info("Login credential is correct and logged in")
            self.log.info("taking the screen shoot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_02_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot"
                                        "\\test_page_tital_01_test_login_02_pass.png")
            self.lp.Click_Profile()
            self.log.info("clicking on logout")
            self.lp.Click_Logout()
            assert True

        else:
            self.log.info("given credential's are wrong")
            self.log.info("taking the screen shoot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_02_fail", attachment_type=AttachmentType.JPG)
            self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot"
                                        "\\test_page_tital_01_test_login_02_fail.png")
            assert False

