# tests/test_login.py

import os
import random
import time
import tempfile
from dotenv import load_dotenv
import mysql.connector

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables
load_dotenv()

# Headless Chrome options
options = Options()
options.add_argument("--headless=new")  # Use new headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

# Launch Chrome with webdriver-manager
driver = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(driver, 10)

    test_username = f"selenium_user_{random.randint(1000, 9999)}"
    test_password = "test123"

    # 1. Go to /register and fill the form
    driver.get("http://localhost:5000/register")
    driver.find_element(By.NAME, "username").send_keys(test_username)
    driver.find_element(By.NAME, "password").send_keys(test_password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 2. Go to /login and log in
    driver.get("http://localhost:5000/login")
    driver.find_element(By.NAME, "username").send_keys(test_username)
    driver.find_element(By.NAME, "password").send_keys(test_password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 3. Wait for welcome message
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    welcome_text = driver.find_element(By.TAG_NAME, "h1").text

    assert test_username in welcome_text, "❌ Login failed or welcome page not displayed."

    # 4. Verify user exists in DB
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (test_username,))
    result = cursor.fetchone()
    conn.close()

    assert result is not None, "❌ User not found in DB!"
    print("Selenium test passed: User registered, logged in, and found in DB.")

except Exception as e:
    print(f"❌ Selenium test failed: {e}")

finally:
    driver.quit()
