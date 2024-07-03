from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class CommonFunction:
    @staticmethod
    def Click(element):
        element.click()

    @staticmethod
    def SendKeys(element, text):
        element.send_keys(text)

    @staticmethod
    def IsDisplayed(element):
        return element.is_displayed()

    @staticmethod
    def IsSelected(element):
        return element.is_selected()

    @staticmethod
    def Submit(element):
        element.submit()

    @staticmethod
    def Back(driver):
        driver.back()

    @staticmethod
    def ScrollDownBottom(driver, body):
        # Simulate "Page Down" key press to scroll down the page
        body.send_keys(Keys.PAGE_DOWN)

    @staticmethod
    def Close(driver):
        driver.close()

    @staticmethod
    def Quit(driver):
        driver.quit()
