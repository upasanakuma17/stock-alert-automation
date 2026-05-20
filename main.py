from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yagmail
import os
import time

# WEBSITE URL
url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"

# OPEN CHROME BROWSER
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# OPEN WEBSITE
driver.get(url)

# WAIT FOR WEBSITE TO LOAD
time.sleep(5)

# FIND PERCENTAGE ELEMENT
percentage = driver.find_element(
    By.CLASS_NAME,
    "stock-trend"
)

# EXTRACT TEXT
percentage_text = percentage.text

print("Current Percentage:", percentage_text)

# REMOVE %
percentage_number = percentage_text.replace("%", "")

# CONVERT TO FLOAT
percentage_number = float(percentage_number)

print("Converted Number:", percentage_number)

# CHECK CONDITION
if percentage_number < -0.10:

    print("Sending Email Alert...")

    sender = "yourgmail@gmail.com"
    receiver = "yourgmail@gmail.com"

    yag = yagmail.SMTP(
        user=sender,
        password=os.getenv("PASSWORD")
    )

    subject = "Stock Alert"

    contents = f"""
    Warning!

    Stock dropped below -0.10%

    Current value: {percentage_number}%
    """

    yag.send(
        to=receiver,
        subject=subject,
        contents=contents
    )

    print("Email Sent!")

else:
    print("Stock value is normal.")

# CLOSE BROWSER
driver.quit()