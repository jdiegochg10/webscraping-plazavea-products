from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import xlsxwriter

class PlazaVea():


  def __init__(self):
    self.driver = webdriver.Chrome(executable_path="D:/Aplicaciones/automation-browser/drivers/chromedriver.exe")  

  def entry(self):
    matriz = [ [ 0 for i in range(7) ] for j in range(10) ] 
    rowm = 0
    colm = 0

    codigoMenu = '01000101'
    codigoProducto = '0001'    
    

    base_url = 'https://www.plazavea.com.pe/gancho-organizador-para-reposacabezas-de-asiento-91678/p'
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    self.driver.get(base_url)       

    #active descripcion
    productDescription = self.driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[4]/div[5]/div[1]/div[1]').click()
    #active tecni    
    especificationTechical = self.driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[4]/div[5]/div[1]/div[5]').click()
    

    # print(matriz)
    # print(np.array(matriz))

    for i, row in enumerate(self.driver.find_elements(By.TAG_NAME, 'tr')):       
      for j, cellth in enumerate(row.find_elements(By.TAG_NAME, 'th')):  
        print(str(cellth.text))
        matriz[i][0] = codigoMenu
        matriz[i][1] = codigoProducto
        matriz[i][2] = i  
        matriz[i][3] = cellth.text
        matriz[i][5] = 0
        matriz[i][6] = 1
        # print("j" + str(j))    
        # print(cellth.text)
      for j, celltd in enumerate(row.find_elements(By.TAG_NAME, 'td')):
        matriz[i][4] = celltd.text
        # matriz.append(celltd.text)
        # print(celltd.text)    
    self.driver.quit()
    # print(np.array(matriz))
    
    wb = xlsxwriter.Workbook('ProductoPlavaVea.xlsx') 

    # add_sheet is used to create sheet. 
    ws = wb.add_worksheet('PRODUCTO')


    for codigoMenu, codigoProducto, i, cellth, celltd, j, z in (matriz):
      ws.write(rowm, colm, codigoMenu)
      ws.write(rowm, colm + 1, codigoProducto)
      ws.write(rowm, colm + 2, i)
      ws.write(rowm, colm + 3, cellth)
      ws.write(rowm, colm + 4, celltd)
      ws.write(rowm, colm + 5, j)
      ws.write(rowm, colm + 6, z)
      rowm += 1

    wb.close()
  
bot = PlazaVea()
bot.entry()
