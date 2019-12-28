#! /bin/python3
from progressbar import progressbar
import os
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
for i in progressbar(range(86)):
    details = driver.find_element_by_xpath(f"/html/body/div[1]/section[2]/div[1]/div[2]/div[{i+1}]/div[1]/a[1]")
    IDs.append(details.get_attribute("href").strip().strip("/").split("/")[-1])
##
for root, dirs, files in os.walk("results/", topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
    os.rmdir("results")
os.mkdir("results")

for ID in progressbar(IDs):
    comparator_url = f"https://www.cars.com/research/compare/?vehicles={ID}"
    print(f"{ID=}")
    driver.get(comparator_url)
    time.sleep(1)
    driver.find_element_by_id("customize-compare-button").click()
    time.sleep(2)
    driver.find_elements_by_class_name("toggle-all")[-1].click()
    driver.find_element_by_id("done-button").click()
    time.sleep(2)
    body = driver.find_element_by_xpath("//body").get_attribute('outerHTML')
    with open(f"results/{ID}.html","w+") as f:
        f.write(body)
driver.close()

## XPATHs for specs
    #data = {
    #    'overview'                 : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/div[4]/section/"),
    #    'pricing'                  : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[1]/"),
    #    'fuel_economy'             : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[2]/"),
    #    'convenience'              : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[2]/"),
    #    'specs'                    : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[4]/"),
    #    'entertainment'            : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[5]/"),
    #    'warranty'                 : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[6]/"),
    #    'seats'                    : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[7]/"),
    #    'cargo'                    : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[8]/"),
    #    'climate'                  : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[9]/"),
    #    'safety'                   : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[10]/"),
    #    'security'                 : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[11]/"),
    #    'exterior'                 : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[12]/"),
    #    'instrumentation'          : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[13]/"),
    #    'mechanical'               : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[14]/"),
    #    'IIHS_Crash_Test_Ratings'  : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[15]/"),
    #    'NHTSA_Crash_Test_Ratings' : driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/article/div/div[2]/div[1]/cars-research-compare-datapoints/div/div[16]/")
    #}

