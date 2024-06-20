from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # This argument maximizes the window

driver = webdriver.Chrome(options=chrome_options)

driver.get("git")

# driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[1]/input").send_keys("adminvfqffpmh0603050@yopmail.com")

EmailInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[1]/input")
EmailInputField.send_keys("adminvfqffpmh0603050@yopmail.com")

PassInputField = driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/input")
PassInputField.send_keys("Aa123456@")

driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/div[2]/div/span/i").click()

# driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/button").click()

EnterButton = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-login/div/div[2]/div/app-login-from/div/div[2]/div/form/button")
EnterButton.send_keys(Keys.ENTER)


time.sleep(20)
driver.close()
driver.quit()