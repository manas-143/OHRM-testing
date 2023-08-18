from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

links = {
    "username" : "//input[@name='username']",
    "password" : "//input[@name='password']",
    "submit"   : '//button[@type="submit"]',
    "pim_button" : "//li[@class='oxd-main-menu-item-wrapper'][2]",
    "add_button" : "//button/i[@class='oxd-icon bi-plus oxd-button-icon']",
    "first_name" : "//input[@name='firstName']",
    "middle_name" : "//input[@name='middleName']",
    "last_name" : "//input[@name='lastName']",
    "emp_id"    : "//*[@class='oxd-input oxd-input--active oxd-input--error']",
    "active_button" : "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']",
    "new_user_name" : "(//*[text()='Username']/following::input)[1]",
    "new_password" : "(//*[text()='Password']/following::input)[1]",
    "confirm_password": "(//*[text()='Confirm Password']/following::input)[1]",
    "save_button" : "//*[@type='submit']",
    "employee_div" : "//div[@class='oxd-table-body']",
    "check_box"    : "//div[@class='oxd-table-card-cell-checkbox']",
    "delete_btn"   :  "//button[text()=' Delete Selected ']",
    "confirm_delete" : "//button[text()=' Yes, Delete ']"


}
records_to_be_delete = 10

@given("the user is on the OrangeHRM website")
def opening_source_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when("the user logs in and adds new employees")
def logged_in_and_add_new_employee(context):
    context.driver.find_element(By.XPATH,links["username"]).send_keys("Admin")
    context.driver.find_element(By.XPATH,links["password"]).send_keys("admin123")
    context.driver.find_element(By.XPATH,links["submit"]).click()
    context.driver.find_element(By.XPATH,links["pim_button"]).click()
    context.driver.find_element(By.XPATH,links["add_button"]).click()
    context.driver.find_element(By.XPATH,links["first_name"]).send_keys("manas")
    context.driver.find_element(By.XPATH,links["middle_name"]).send_keys("kumar")
    context.driver.find_element(By.XPATH,links["last_name"]).send_keys("dash")
    context.driver.find_element(By.XPATH,links["active_button"]).click()
    context.driver.find_element(By.XPATH,links["new_user_name"]).send_keys("manas14")
    context.driver.find_element(By.XPATH,links["new_password"]).send_keys("12@manas")
    context.driver.find_element(By.XPATH,links["confirm_password"]).send_keys("12@manas")
    context.driver.find_element(By.XPATH,links["save_button"]).click()

@when("the user deletes selected employee records")
def select_and_delete_multiple_employee(context):
    context.driver.find_element(By.XPATH, links["pim_button"]).click()
    parent_div = context.driver.find_element(By.XPATH,links["employee_div"])
    child_div = parent_div.find_elements(By.XPATH,links["check_box"])

    for user in range(records_to_be_delete):
        try:
            child_div[user].click()
            time.sleep(3)
        except:
            pass

    context.driver.find_element(By.XPATH,links["delete_btn"]).click()
    context.driver.find_element(By.XPATH, links["confirm_delete"]).click()

@then("the selected records should be deleted")
def closing_the_browser(context):
    context.driver.quit()
