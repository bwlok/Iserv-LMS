from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = "username"
password = "password"


driver = webdriver.Firefox()

driver.get("https://iserv.osz-lise-meitner.eu/iserv/")
elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "form-username"))
)

userBtn = driver.find_element(By.ID, "form-username")
userInput = userBtn.find_element(By.TAG_NAME, "input")
passwordBtn = driver.find_element(By.ID, "form-password")
passwordInput = passwordBtn.find_element(By.TAG_NAME, "input")

userInput.send_keys(username)
passwordInput.send_keys(password)

button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()