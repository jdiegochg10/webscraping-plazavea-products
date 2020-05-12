from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PlazaVea():
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path="D:/Aplicaciones/automation-browser/drivers/chromedriver.exe")  

  def entry(self):
    base_url = 'https://www.plazavea.com.pe/bazar/automotor/accesorios-para-auto/'
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    self.driver.get(base_url)   

    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = self.driver.execute_script("return document.body.scrollHeight")

    while True:
    # Scroll down to bottom
      self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
      new_height = self.driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

    time.sleep(50)

    #get urls of all products 

    allProducts = self.driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/div/section[2]/div[2]/div[2]/div[2]/div[2]/div')
    for i, allProduct in enumerate(allProducts.find_elements(By.CLASS_NAME, 'Showcase__name')):
      if (i == 1):
        # self.driver.find_elements(By.LINK_TEXT)
        # allProduct.click()
        # print("Numero " + str(i) + " : " + allProduct.get_attribute("href"))        
        links = self.driver.find_elements(By.LINK_TEXT(allProduct.get_attribute("href")))
        links.click()
        #  print("Numero " + str(i) + " : " + allProducts.get_attribute("href"))
      # allProducts.get_attribute("href")[1]

    # self.driver.quit()

PlazaVea = PlazaVea()
PlazaVea.entry()