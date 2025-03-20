from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Add_Emp:
    Click_PIM_XPATH = (
        By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
    Button_Add_XPATH = (By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@placeholder='First Name']")
    Text_LastName_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Text_MiddleName_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Button_Save_XPATH = (By.XPATH, "//button[@type='submit']")
    Success_Message_XPATH = (
        By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50, poll_frequency=0.3)

    def click_PIM_01(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_PIM_XPATH))
        self.driver.find_element(*Add_Emp.Click_PIM_XPATH).click()

    def click_add_02(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Button_Add_XPATH))
        self.driver.find_element(*Add_Emp.Button_Add_XPATH).click()

    def enter_firstname_03(self, firstname):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_FirstName_XPATH))
        self.driver.find_element(*Add_Emp.Text_FirstName_XPATH).send_keys(firstname)

    def enter_middlename_04(self, middlename):
        self.driver.find_element(*Add_Emp.Text_MiddleName_XPATH).send_keys(middlename)

    def enter_lastname_05(self, lastname):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_LastName_XPATH))
        self.driver.find_element(*Add_Emp.Text_LastName_XPATH).send_keys(lastname)

    def Click_Save_06(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Button_Save_XPATH))
        self.driver.find_element(*Add_Emp.Button_Save_XPATH).click()

    def success_message_07(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Success_Message_XPATH))
            success_message = self.driver.find_element(*Add_Emp.Success_Message_XPATH).text
            print(success_message)
            return True
        except:
            return False

    def print_Sec_message_08(self):
        self.driver.find_element(*Add_Emp.Success_Message_XPATH).text

