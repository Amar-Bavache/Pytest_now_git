from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Orange_HRM:
    Text_Username_XPATH = (By.CSS_SELECTOR, "input[placeholder='Username']")
    Text_Password_NAME = (By.NAME, "password")
    Button_Login_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_Profile_XPATH = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    Click_Logout_XPATH = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    Find_LOGO_XPATH = (By.XPATH, "/html/body/div/div[1]/div/div[2]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def Enter_username(self, name):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_NAME))
        self.driver.find_element(*Orange_HRM.Text_Username_XPATH).send_keys(name)

    def Enter_Password(self, password):
        self.driver.find_element(*Orange_HRM.Text_Password_NAME).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Orange_HRM.Button_Login_XPATH).click()

    def Click_Profile(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Profile_XPATH))
        self.driver.find_element(*Orange_HRM.Click_Profile_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*Orange_HRM.Click_Logout_XPATH).click()

    def Login_Status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Profile_XPATH))
            self.driver.find_element(*Orange_HRM.Click_Profile_XPATH)
            return True
        except:
            return False

    def Screen_shoot(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Find_LOGO_XPATH))
            self.driver.find_element(*Orange_HRM.Find_LOGO_XPATH)
            return True
        except:
            return False