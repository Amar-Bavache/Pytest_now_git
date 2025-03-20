from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Search_EMP:
    Click_PIM_XPATH = (
        By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
    Text_Search_XPATH = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
    Button_search_XPATH = (By.XPATH, "//button[@type='submit']")
    Search_Result_CSS = (By.CSS_SELECTOR, "div[class='oxd-table-card'] div:nth-child(3) div:nth-child(1)")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_PIM_01(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_PIM_XPATH))
        self.driver.find_element(*Search_EMP.Click_PIM_XPATH).click()

    def enter_empid_09(self, empid):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Search_XPATH))
        self.driver.find_element(*Search_EMP.Text_Search_XPATH).send_keys(empid)

    def click_search_10(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Button_search_XPATH))
        self.driver.find_element(*Search_EMP.Button_search_XPATH).click()

    def Search_Result(self):
        try:
            firstandmiddlename = self.driver.find_element(*Search_EMP.Search_Result_CSS).text
            print(firstandmiddlename)
            return True
        except NoSuchElementException:
            return False