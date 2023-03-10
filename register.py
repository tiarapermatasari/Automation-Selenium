import unittest
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from route import url
from data import register

class TestRegister(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_signup_valid_data(self):
        driver = self.browser
        driver.get(url.baseURL)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-female").click()
        driver.find_element(By.ID, "FirstName").send_keys(register.firstName)
        driver.find_element(By.ID, "LastName").send_keys(register.lastName)
        driver.find_element(By.ID, "Email").send_keys(register.email)
        driver.find_element(By.ID, "Password").send_keys(register.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(register.confirmPassword)
        driver.find_element(By.ID, "register-button").click()
        
        responSuccess = driver.find_element(By.CLASS_NAME, "result").text
        self.assertIn(register().successRegister, responSuccess)
        
        responAccount = driver.find_element(By.CLASS_NAME, "account").text
        self.assertEqual(responAccount, register().email)
        
    def test_signup_invalid_data(self):
        driver = self.browser
        driver.get(url.baseURL)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "register-button").click()
        
        ValidationFirstName = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertEqual(ValidationFirstName, register().validationFirstName)
        
    
    def tearDown(self):
        self.browser.close()
        
if __name__ == '__main__':
    unittest.main()