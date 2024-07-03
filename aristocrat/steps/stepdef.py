import time
import pytest
import ast
import json
from Functions import CommonFunction
from PropertyFile import PropertiesUtils
from selenium import webdriver
import ast
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
with open(
    "steps\config.json", "r"
) as config:
    data = json.load(config)
#
pro = PropertiesUtils(data["property_path"])
# driver methods
common = CommonFunction()

@given('The user navigates to the website')
def navigate_to_website(context):
    driver.get(data["url"])


@when('user Enters username and password')
def enter_credentials(context):
    time.sleep(2)
    user_field=driver.find_element(*pro.get_locator("username"))
    common.SendKeys(user_field,data["username"])
    pass_field=driver.find_element(*pro.get_locator("password"))
    common.SendKeys(pass_field,data["password"])


@when('user click on log in button')
def click_login_button(context):
    login_btn=driver.find_element(*pro.get_locator("login_button"))
    common.Click(login_btn)
    time.sleep(2)

# Then Steps
@then('User will be logged in')
def verify_login(context):
    title=driver.find_element(*pro.get_locator("title_card"))
    common.IsDisplayed(title)

#TC002

@given('The user navigates to the website from the URL')
def navigate_to_website(context):
    driver.back()
    time.sleep(2)

@when('user Enters locked out username and password')
def enter_locked_out_credentials(context):
    user_field=driver.find_element(*pro.get_locator("username"))
    common.SendKeys(user_field,data["locked_username"])
    pass_field=driver.find_element(*pro.get_locator("password"))
    common.SendKeys(pass_field,data["password"])

    

@when('user click on the log in button')
def click_login_button(context):
    login_btn=driver.find_element(*pro.get_locator("login_button"))
    common.Click(login_btn)
    time.sleep(2)

@then('User will be prompted with error')
def verify_error_message(context):
    title=driver.find_element(*pro.get_locator("error_prompt"))
    common.IsDisplayed(title)

#TC003

@given('I am on the inventory page')
def go_to_inventory_page(context):
    user_field=driver.find_element(*pro.get_locator("username"))
    user_field.clear()
    common.SendKeys(user_field,data["username"])

    login_btn=driver.find_element(*pro.get_locator("login_button"))
    common.Click(login_btn)
    time.sleep(2)


@when('user sorts products from low price to high price')
def sort_products_low_to_high(context):
    sort=driver.find_element(*pro.get_locator("lohi_sort"))
    common.Click(sort)
    time.sleep(1)

@when('user adds lowest priced product')
def add_lowest_priced_product(context):
    add_cart=driver.find_element(*pro.get_locator("add_to_cart"))
    common.Click(add_cart)
    time.sleep(1)


@when('user clicks on cart')
def click_cart(context):
    cart_btn=driver.find_element(*pro.get_locator("cart_button"))
    common.Click(cart_btn)
    time.sleep(1)

@when('user clicks on checkout')
def click_checkout(context):
    checkout_button = driver.find_element(*pro.get_locator("checkout"))
    common.Click(checkout_button)
    time.sleep(0.5)

@when('user enters first name John')
def enter_first_name(context):
    first_name=driver.find_element(*pro.get_locator("first_name"))
    common.SendKeys(first_name,data["firstName"])
    
@when('user enters last name Doe')
def enter_last_name(context):
    last_name=driver.find_element(*pro.get_locator("last_name"))
    common.SendKeys(last_name,data["lastName"])
    
@when('user enters zip code 123')
def enter_zip_code(context):
    postal_code=driver.find_element(*pro.get_locator("postal_code"))
    common.SendKeys(postal_code,data["postalCode"])
    time.sleep(0.5)
    
@when('user clicks Continue button')
def click_continue(context):
    continue_button = driver.find_element(*pro.get_locator("continue"))
    common.Click(continue_button)

@then('I verify in Checkout overview page if the total amount for the added item is $8.63')
def verify_total_amount(context):
    total_amount = driver.find_element(*pro.get_locator("amount"))
    common.IsDisplayed(total_amount)

@when('user clicks Finish button')
def click_finish(context):
    finish_button = driver.find_element(*pro.get_locator("finish"))
    common.Click(finish_button)
    time.sleep(1)

@then('Thank You header is shown in Checkout Complete page')
def verify_checkout_complete(context):
    thank_you_header = driver.find_element(*pro.get_locator("thank_you"))
    if(common.IsDisplayed(thank_you_header)):
        print("verified")
    else:
        print ("something went wrong")