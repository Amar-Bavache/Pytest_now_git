import time

from PageObjects.LoginPO import Orange_HRM
from Utilities.logger import LogGenerator
from Utilities.readConfig import Readconfig
from PageObjects.AddEmpPO import Add_Emp
from Utilities import Xutils


class Test_HRM_AddEMP_DDT_004:
    username = Readconfig.Getusername()
    password = Readconfig.Getpassword()
    log = LogGenerator.loggen()
    Xl1path = "D:\\Credence\\Python\\ProjectOrangeHRM\\testcases\\testdata\\FML.xlsx"

    def test_addemp_05(self, setup):
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
        self.row = Xutils.RowCount(self.Xl1path, "Sheet1")
        for r in range(2, self.row + 1):
            self.firstname = Xutils.ReadData(self.Xl1path, "Sheet1", r, 2)
            self.middlename = Xutils.ReadData(self.Xl1path, "Sheet1", r, 3)
            self.lastname = Xutils.ReadData(self.Xl1path, "Sheet1", r, 4)
            time.sleep(5)
            self.log.info("Clicking on PIM from list")
            self.ae.click_PIM_01()
            self.log.info("clicking on add button")
            self.ae.click_add_02()
            self.log.info("entering firstname: " + self.firstname + " middlename: " + self.middlename + " lastname: " + self.lastname + " in text box")
            self.ae.enter_firstname_03(self.firstname)
            self.ae.enter_middlename_04(self.middlename)
            self.ae.enter_lastname_05(self.lastname)
            self.log.info("clicking on save button")
            self.ae.Click_Save_06()
            print(self.ae.print_Sec_message_08())
            self.log.info("checking for emp add success")
            if self.ae.success_message_07() == True:
                self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot\\EMP_ADD_Suc_pass.png")
                assert True
            else:
                self.driver.save_screenshot("D:\\Credence\\Python\\ProjectOrangeHRM\\ScreenShot\\EMP_ADD_Suc_fail.png")
                assert False
        self.log.info("Test case DDT is completed")





