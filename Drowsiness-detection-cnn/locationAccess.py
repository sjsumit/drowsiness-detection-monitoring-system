import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def location_coordinates():
      options = Options()
      options.add_argument("--use-fake-ui-for-media-stream")
      timeout = 20
      driver = webdriver.Chrome(executable_path = './chromedriver.exe', chrome_options=options)
      driver.get("https://mycurrentlocation.net/")
      wait = WebDriverWait(driver, timeout)
      time.sleep(3)
      longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
      longitude = [x.text for x in longitude]
      longitude = str(longitude[0])
      latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
      latitude = [x.text for x in latitude]
      latitude = str(latitude[0])
      driver.quit()
      res = requests.get('https://www.ipinfo.io/')
      data = res.json()
      city = data['city']
      print("Latitude :%s"%latitude,"Longitude: %s"%longitude,"City: %s"%city)
      return latitude,longitude,city
