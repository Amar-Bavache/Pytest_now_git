import time

from PageObjects.LoginPO import Orange_HRM
from Utilities.logger import LogGenerator
from Utilities.readConfig import Readconfig
from PageObjects.AddEmpPO import Add_Emp


class Test_HRM_AddEMP_002:
    username = Readconfig.Getusername()
    password = Readconfig.Getpassword()
    log = LogGenerator.loggen()

    def test_placeorder_01(self, setup):
        self.driver = setup
        self.log.info("Opening the web browser")
        self.log.info("navigating and opening the given URL")
        self.lp = Orange_HRM(self.driver)
        self.log.info("Entering the username")
        self.lp.Enter_username(self.username)
        self.log.info("Entering the password")
        self.lp.Enter_Password(self.password)
        self.log.info("clicking on login button")
        self.lp.Click_Login()
        self.ae = Add_Emp(self.driver)
        time.sleep(5)
        self.log.info("Clicking on PIM from list")
        self.ae.click_PIM_01()
        self.log.info("clicking on add button")
        self.ae.click_add_02()
        self.log.info("entering first middle last name in text box")
        self.ae.enter_firstname_03("Ramesshh")
        self.ae.enter_middlename_04("D")
        self.ae.enter_lastname_05("Baaakale")
        self.log.info("clicking on save button")
        self.ae.Click_Save_06()
        self.log.info("checking for emp add success")
        if self.ae.success_message_07() == True:
            self.log.info(self.ae.print_Sec_message_08())
            self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot\\EMP_ADD_Suc_pass.png")
            assert True
        else:
            self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot\\EMP_ADD_Suc_fail.png")
            assert False

