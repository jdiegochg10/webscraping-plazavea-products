import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen, Request

class PlazaVea():
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path="D:/Aplicaciones/automation-browser/drivers/chromedriver.exe")  
  
  def entry(self):
    base_url = 'https://www.plazavea.com.pe/gancho-organizador-para-reposacabezas-de-asiento-91678/p'
    self.driver.maximize_window()    
    self.driver.implicitly_wait(10)
    self.driver.get(base_url)

    imageObjects = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[3]/div[1]/div[2]/ul/div[1]/div')
    
    for imageObject in imageObjects.find_elements(By.TAG_NAME, 'a'):
      urlImageNormal = imageObject.get_attribute('rel')
      urlImageZoom = imageObject.get_attribute('zoom')
      print(urlImageNormal)
      print(urlImageZoom)

    # src = img.get_attribute('src')
    # download the image
    urllib.request.urlretrieve(urlImageNormal, "./img/Normal.webp")
    urllib.request.urlretrieve(urlImageZoom, "./img/zoom.webp")

    self.driver.quit()
PlazaVea = PlazaVea()
PlazaVea.entry()

