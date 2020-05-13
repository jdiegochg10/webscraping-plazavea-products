from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class PlazaVea():
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path="D:/Aplicaciones/automation-browser/drivers/chromedriver.exe")      

  def entry(self):
    path = './img/'
    base_url = 'https://www.plazavea.com.pe'
    self.driver.maximize_window()    
    self.driver.implicitly_wait(10)
    self.driver.get(base_url)
    #click electro
    menus = self.driver.find_elements_by_xpath('/html/body/div[3]/header/div[1]/div/div')
    #Menu
    for menu in menus:
      if menu.get_attribute('class') == 'Header__dropdown  Header__offer ':
        titleMenu = menu.find_element(By.CLASS_NAME,'Header__dropdown__text').text       
        #supermarket
        if titleMenu == 'Supermercado':
          pathM = path + titleMenu        
          #create directory
          os.makedirs(pathM)
          menu.find_element(By.CLASS_NAME,'Header__dropdown__text').click()   
          time.sleep(20)  
          raizSubMenu = self.driver.find_elements_by_xpath('/html/body/div[3]/header/section/div[3]/div[2]/div/ul/div/li')
          for i, subMenu in enumerate(raizSubMenu):
            #title submenu            
            titleSubMenu = subMenu.find_element(By.TAG_NAME, 'a').text            
            os.makedirs(path + titleMenu + '/' + titleSubMenu)            
        #electro
        elif titleMenu == 'Electro':
          pathE = path + titleMenu 
          #create directory
          os.makedirs(pathE)       
        # try:
        #   os.makedirs(path)
        # except OSError:
        #   print("Creation of the directory %s failed" % path)
        # else:
        #   print("Successfully created the directoy %s" % path)

      else:
        print('No es menu')

    def createPath(self, path):
      try:
        os.makedirs(path)
      except OSError:
        print("Creation of the directory %s failed" % path)
      else:
        print("Successfully created the directoy %s" % path)
    #filter 

    # print(header.tex)

    # menu = self.driver. 
    

    # for head in header:

    #   if header.get_attribute('class') == 'Header__dropdown  Header__offer':
    #     print (true)


    # self.driver.quit()
PlazaVea = PlazaVea()
PlazaVea.entry()

