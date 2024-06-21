from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def test_openUrl4(driver):
    driver.get("https://app-ffp-stag.azurewebsites.net/")

def test_loginSuccess4(driver):
    # Enter Email
    EmailInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[1]/input")
    EmailInputField.send_keys("adminvfqffpmh0603050@yopmail.com")

    # Enter Password
    PassInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/input")
    PassInputField.send_keys("Aa123456@")

    # Eye Button
    driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/span/i").click()

    # Click Login
    EnterButton = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/button")
    EnterButton.send_keys(Keys.ENTER)

def test_updatePassword(driver):
    # Go to Profile
    wait = WebDriverWait(driver, 10)
    gotoProfile = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/app-header/nav/div[2]/div[1]/ul[2]/li[4]/a/span/img")))
    gotoProfile.click()

    # Click Profile
    wait = WebDriverWait(driver, 10)
    clickProfile = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/app-header/nav/div[2]/div[1]/ul[2]/li[4]/ul/li[1]/a")))
    clickProfile.click()

    #Update Password
    UpdatePassword = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/app-user-profile/div/div/div[2]/form/fieldset/div[2]/div[3]/div/div/span/a/span/i[2]")))
    UpdatePassword.click()

    #Enter Old Password
    EnterOldPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/app-user-profile/div/div/div[2]/div/div/div/div[2]/form/div/div/input")))
    EnterOldPassword.send_keys("Aa123456@")

    #Enter Old Password Again
    EnterOldPasswordAgain = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/app-user-profile/div/div/div[2]/div/div/div/div[2]/form/fieldset/div[1]/div/input")))
    EnterOldPasswordAgain.send_keys("Aa1234567@")

    #Enter New Password
    EnterNewPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/app-user-profile/div/div/div[2]/div/div/div/div[2]/form/fieldset/div[2]/div/input")))
    EnterNewPassword.send_keys("Aa1234567@")

    #Click Save
    SavePassword = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-ffp/div/app-user-profile/div/div/div[2]/div/div/div/div[3]/button[2]")))
    SavePassword.click()


    time.sleep(20)
    # driver.close()
    # driver.quit()