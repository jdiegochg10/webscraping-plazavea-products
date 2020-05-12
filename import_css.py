from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import webbrowser
import xlsxwriter
from selenium.common.exceptions import NoSuchElementException 


class PlazaVea():
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path="D:/Aplicaciones/automation-browser/drivers/chromedriver.exe")  
  
  def entry(self):


    base_url = 'https://www.plazavea.com.pe/gancho-organizador-para-reposacabezas-de-asiento-91678/p'
    self.driver.maximize_window()    
    self.driver.implicitly_wait(10)
    self.driver.get(base_url)   

    getImage = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[8]/span[1]')
    # getAttribute = getImage.value_of_css_property('background-image')
    getText = getImage.text
    print(getText)
    
PlazaVea = PlazaVea()
PlazaVea.entry()