import time

from PageObjects.LoginPO import Orange_HRM
from Utilities.logger import LogGenerator
from Utilities.readConfig import Readconfig
from PageObjects.SearchEMPPO import Search_EMP


class Test_SearchEmp:
    username = Readconfig.Getusername()
    password = Readconfig.Getpassword()
    log = LogGenerator.loggen()

    def test_searchemp_01(self, setup):
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
        time.sleep(5)
        self.se = Search_EMP(self.driver)
        self.log.info("clicking on PIM")
        self.se.click_PIM_01()
        self.log.info("entering empid in text box")
        self.se.enter_empid_09("0099")
        self.log.info("clicking on search button")
        self.se.click_search_10()
        if self.se.Search_Result() == True:
            self.log.info("Printed Firstname and middle last")
            self.log.info("Testcase test_addEmp_003 is passed")
            time.sleep(3)
            self.driver.save_full_page_screenshot(".\\ScreenShots\\test_addEmp_003.png")
            assert True
        else:
            self.log.info("Testcase test_addEmp_003 is failed")
            assert False
        self.log.info("Testcase test_addEmp_003 is completed")

