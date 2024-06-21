from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_openUrl3(driver):
    driver.get("https://app-ffp-stag.azurewebsites.net/")
    time.sleep(5)

# driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[1]/input").send_keys("adminvfqffpmh0603050@yopmail.com")
def test_loginSuccess3(driver):
    EmailInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[1]/input")
    EmailInputField.send_keys("adminvfqffpmh0603050@yopmail.com")

    PassInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/input")
    PassInputField.send_keys("Aa1234567@")

    driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/span/i").click()

    # driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/button").click()

    EnterButton = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/button")
    EnterButton.send_keys(Keys.ENTER)

    time.sleep(20)
    driver.close()
    driver.quit()