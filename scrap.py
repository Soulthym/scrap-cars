from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
##
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--fullscreen")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.cars.com/research/search/?lrgPriceId=8,9,11&rn=0&rpp=99&catId=444")
time.sleep(4)
##
IDs = []
for i in range(86):
    details = driver.find_element_by_xpath(f"/html/body/div[1]/section[2]/div[1]/div[2]/div[{i+1}]/div[1]/a[1]")
    IDs.append(details.get_attribute("href").strip().strip("/").split("/")[-1])
    print(IDs[-1])
