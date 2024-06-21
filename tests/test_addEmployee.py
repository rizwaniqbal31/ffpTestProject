from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def test_openUrl1(driver):
    driver.get("https://app-ffp-stag.azurewebsites.net/")

def test_loginSuccess1(driver):
    # Enter Email
    EmailInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[1]/input")
    EmailInputField.send_keys("adminvfqffpmh0603050@yopmail.com")

    # Enter Password
    PassInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/input")
    PassInputField.send_keys("Aa1234567@")

    # Eye Button
    driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/span/i").click()

    # Click Login
    EnterButton = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/button")
    EnterButton.send_keys(Keys.ENTER)

def test_addEmployee(driver):
    # Go to Admin
    wait = WebDriverWait(driver, 40)
    gotoAdmin = wait.until(EC.element_to_be_clickable((By.XPATH, "//html/body/app-root/div[2]/app-ffp/app-ffp-sidebar/div/div/ul/li[4]/a/span[1]")))
    gotoAdmin.click()

    # Go to Employee
    gotoEmployee = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/app-ffp-sidebar/div/div/ul/li[4]/ul/li[2]/a/span")))
    gotoEmployee.click()
    # driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-ffp/app-ffp-sidebar/div/div/ul/li[4]/ul/li[2]/a/span").click()

    #Add New Employee Button
    AddNewEmployee = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[2]/div/div/div[1]/div/a[2]")))
    AddNewEmployee.click()

    #Select Role
    selectRole = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[1]/div/div/div/div/p-dropdown/div/label")))
    selectRole.click()
    selectRoleType = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[1]/div/div/div/div/p-dropdown/div/div[4]/div/ul/li[4]/div/div")))
    selectRoleType.click()

    # Employee Image
    # image_path = "D:\@Metis\Icons\supervisor.png"
    # file_input = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[2]/div/div/div/input")))
    # file_input.send_keys(os.path.abspath(image_path))

    #Employee Name
    EmpName = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[1]/div/div/input")))
    EmpName.send_keys("Employee Labour One")

    #Employee QID
    EmployeeQID = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div/p-inputmask/input")))
    EmployeeQID.send_keys("24657681231")

    #DOB
    DOB = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[3]/div/p-calendar/span/input")))
    DOB.click()

    # Calculate today's date
    day = 12
    month = "May"
    year = 1996

    # Wait for the calendar to be visible and interact with it
    calendar = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ui-datepicker"))
    )

    # Select the current year
    year_select = calendar.find_element(By.CSS_SELECTOR, "select.ui-datepicker-year")
    for option in year_select.find_elements(By.TAG_NAME, "option"):
        if option.text == str(year):
            option.click()
            break

    # Select the current month
    month_select = calendar.find_element(By.CSS_SELECTOR, "select.ui-datepicker-month")
    for option in month_select.find_elements(By.TAG_NAME, "option"):
        if option.text == month:
            option.click()
            break

    # Select the current day
    day_elements = calendar.find_elements(By.CSS_SELECTOR, "a.ui-state-default")
    for day_element in day_elements:
        if day_element.text == str(day):
            day_element.click()
            break

    #Select Date
    # selectDOB = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[3]/div/p-calendar/span/div/table/tbody/tr[1]/td[2]/a")))
    # selectDOB.click()


    #Date of Joining
    DateofJoining = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[4]/div/p-calendar/span/input")))
    DateofJoining.click()

    # Calculate today's date
    today = datetime.datetime.now()
    day = today.day
    month = today.strftime("%B")
    year = today.year

    # Wait for the calendar to be visible and interact with it
    calendar = wait.until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[4]/div/p-calendar/span/div"))
    )

    # Select the current year
    year_select = calendar.find_element(By.CSS_SELECTOR, "select.ui-datepicker-year")
    for option in year_select.find_elements(By.TAG_NAME, "option"):
        if option.text == str(year):
            option.click()
            break

    # Select the current month
    month_select = calendar.find_element(By.CSS_SELECTOR, "select.ui-datepicker-month")
    for option in month_select.find_elements(By.TAG_NAME, "option"):
        if option.text == month:
            option.click()
            break

    # Select the current day
    day_elements = calendar.find_elements(By.CSS_SELECTOR, "a.ui-state-default")
    for day_element in day_elements:
        if day_element.text == str(day):
            day_element.click()
            break

    #Select Joining Date
    # selectJoining = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[4]/div/p-calendar/span/div/table/tbody/tr[1]/td[2]/a")))
    # selectJoining.click()

    #Select Contact
    selectContact = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[5]/div/div/p-inputmask/input")))
    selectContact.send_keys("32437437")

    #Select Gender
    selectGender = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[6]/div/p-dropdown/div/label")))
    selectGender.click()

    #Select Gender Type
    selectGenderType = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[6]/div/p-dropdown/div/div[4]/div/ul/li[1]")))
    selectGenderType.click()

    #Select Maritial Status
    SelectMaritialStatus = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[7]/div/p-dropdown/div/label")))
    SelectMaritialStatus.click()

    #Select Maritial Status Type
    SelectMaritialStatusType = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[7]/div/p-dropdown/div/div[4]/div/ul/li[2]/span")))
    SelectMaritialStatusType.click()

    #Enter Address
    EnterAddress = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[8]/div/div/input")))
    EnterAddress.send_keys("I-10, Islamabad")

    #Enter Salary
    EnterSalary = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[9]/div/div/input")))
    EnterSalary.send_keys("3000")


    #Assign Zone
    AssignZone = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[3]/div/div/div[1]/div/div/span/p-dropdown/div/label")))
    AssignZone.click()

    #Select Zone
    SelectZone = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[3]/div/div/div[1]/div/div/span/p-dropdown/div/div[4]/div[2]/ul/li[1]")))
    SelectZone.click()

    #Assign Device
    AssignDevice = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[3]/div/div/div[2]/div/p-dropdown/div/label")))
    AssignDevice.click()

    #Select Device
    SelectDevice = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/form/div[3]/div/div/div[2]/div/p-dropdown/div/div[4]/div[2]/ul/li/span")))
    SelectDevice.click()

    #Save Button
    ClickSave = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/ffp-employee-admin-form/div/div[1]/div/div/div[2]/div/span/button[2]")))
    ClickSave.click()

    time.sleep(20)
    # driver.close()
    # driver.quit()