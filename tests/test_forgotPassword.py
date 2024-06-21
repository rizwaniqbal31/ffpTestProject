from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk, simpledialog


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def test_openUrl2(driver):
    driver.get("https://app-ffp-stag.azurewebsites.net/")
    time.sleep(5)

def test_fotgotPassword(driver):
    wait = WebDriverWait(driver, 10)

    # Click Forgot Password
    clickForgotPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[3]/button")))
    clickForgotPassword.click()

    EnterEmail = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/div[3]/div/div/div[1]/form/div/input")))
    EnterEmail.send_keys("adminvfqffpmh0603050@yopmail.com")
    time.sleep(3)


    submitButton = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/div[3]/div/div/div[2]/button[2]")))
    submitButton.click()
    time.sleep(30)


    # Enter the OTP into the Dialog box
    otp = simpledialog.askstring("OTP", "Please enter the OTP:")


    # Enter the OTP into the input field
    EnterOTP = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/div[2]/div/form/div[1]/input")))
    EnterOTP.send_keys(otp)
    time.sleep(30)

    verifyButton = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/div[2]/div/form/button[1]")))
    verifyButton.click()


    EnterNewPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/div[3]/div/form/div[1]/div[1]/input")))
    EnterNewPassword.send_keys("Aa@12345@")
    time.sleep(3)

    ConfirmPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/div[3]/div/form/div[2]/div[1]/input")))
    ConfirmPassword.send_keys("Aa@12345644564@")
    time.sleep(3)

    # Check if passwords match
    if EnterNewPassword.get_attribute("value") != ConfirmPassword.get_attribute("value"):
        print("Error: Passwords don't match")
        # Optionally, you can clear the ConfirmPassword field and request the user to enter the password again
        ConfirmPassword.clear()
        ConfirmPassword.send_keys(Keys.CONTROL + "a")
        ConfirmPassword.send_keys(Keys.DELETE)
        # Then, request the user to enter the password again
        # You can use any method to prompt the user, like a tkinter dialog box or simple input()
    else:
        print("Passwords match")

    # Save New Password
    SavePassword = wait.until(EC.element_to_be_clickable((By.XPATH, "")))
    SavePassword.click()

    time.sleep(20)
    # driver.close()
    # driver.quit()