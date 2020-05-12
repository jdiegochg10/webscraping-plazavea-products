from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException 


class PlazaVea():
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path="D:/Aplicaciones/automation-browser/drivers/chromedriver.exe")  

  def entry(self):
    base_url = 'https://www.plazavea.com.pe/piso-para-auto-top-gam-negro/p'
    self.driver.maximize_window()    
    self.driver.implicitly_wait(10)
    self.driver.get(base_url)   

    # time.sleep(10)

    print(self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[1]').get_attribute('class'))
    print(self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[3]').get_attribute('class'))
    print(self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[5]').get_attribute('class'))



    if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[1]').get_attribute('class') == 'selector':      
      print("true")     
    else:
      print("false")
    if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[3]').get_attribute('class') == 'selector':
      print("true")     
    else:
      print("false")
    if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[5]').get_attribute('class') == 'selector':
      print("true")     
    else:
      print("false")


    #scraping characterisc
    # if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[3]').find_elements(By.CLASS_NAME, 'Selector'):
    #   print("true")
    # #technical specifications 
    # if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[5]').find_elements(By.CLASS_NAME, 'Selector'): 
    #   print("true")
    #   self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[5]').click()      
    #   #array               
        
    
    self.driver.quit()
PlazaVea = PlazaVea()
PlazaVea.entry()