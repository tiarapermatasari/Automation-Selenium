import unittest
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from unittest.suite import TestSuite
from selenium.webdriver.support.ui import Select
from route import url
from data import *

class TestCheckout(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
      
    def test_checkout(self):
        driver = self.browser
        driver.get(url().baseURL)
        driver.maximize_window
        
        #checkout
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[4]/div/div[1]/a/img').click()
        driver.find_element(By.ID, "add-to-cart-button-72").click()
        driver.find_element(By.CLASS_NAME, "cart-label").click()
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[3]/input[1]').click()
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys(register.firstName)
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys(register.lastName)
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys(register.email)
        driver.find_element(By.XPATH, "//select[@id='BillingNewAddress_CountryId']/option[text()='Canada']").click()
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys(address.city)
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys(address.address1)
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys(address.postalCode)
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys(address.phoneNumber)
        driver.find_element(By.XPATH, '//*[@id="billing-buttons-container"]/input').click()
        driver.find_element(By.XPATH, '//*[@id="shipping-buttons-container"]/input').click()
        driver.find_element(By.XPATH, '//*[@id="shipping-method-buttons-container"]/input').click()
        driver.find_element(By.XPATH, '//*[@id="payment-method-buttons-container"]/input').click()
        driver.find_element(By.XPATH, '//*[@id="payment-info-buttons-container"]/input').click()
        driver.find_element(By.XPATH, '//*[@id="confirm-order-buttons-container"]/input').click()
        
        #assert
        responseSuccess = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/div[1]/strong').text
        self.assertEqual(responseSuccess, address.successOrder)
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        