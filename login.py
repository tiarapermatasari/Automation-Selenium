import unittest
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from route import url
from data import *


class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login_valid_data(self):
        driver = self.browser
        driver.maximize_window
        driver.get(url.baseURL)
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys(login.validEmail)
        driver.find_element(By.ID, "Password").send_keys(login.validPassword)
        driver.find_element(By.CLASS_NAME, "button-1").click()
        Alert(driver).dismiss()
        
        successLogin = driver.find_element(By.CLASS_NAME, "account").text
        driver.implicitly_wait(10)
        self.assertEqual(successLogin, login().validEmail)
    
    
    def test_login_invalid_data(self):
        driver = self.browser
        driver.maximize_window
        driver.get(url.baseURL)
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys(login.invalidEmail)
        driver.find_element(By.ID, "Password").send_keys(login.invalidPassword)
        driver.find_element(By.CLASS_NAME, "button-1").click()
        
        ValidationLoginUnsuccess = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertEqual(ValidationLoginUnsuccess, login().errorMessage)
        
    
if __name__ == '__main__':
    unittest.main()
        
        