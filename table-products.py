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

    #Constant
    
    ruc = '20532584681'
    rucCorpSell = 'NULL'
    nameCor = 'PLAZA VEA'    

    #variables
    matrizProduct = [ [ '' for i in range(5) ] for j in range(140) ] 
    matrizEspTec = [ [ '' for i in range(7) ] for j in range(100) ] 
    matrizOtherDesc = [ [ '' for i in range(4) ] for j in range(140) ] 
    matrizProductEmp = [ [ '' for i in range(15) ] for j in range(140) ] 

    rowGlobalProduct = 1
    rowGlobalEspTec = 1
    rowGlobalOtherDesc = 1
    rowGlobalProductCom = 1


    rowExcelPro = 0
    colExcelPro = 0
    rowm = 0
    colm = 0
    rowExcelOtherDes = 0
    colExcelOtherDesc = 0
    rowExcelProductEmp = 0
    colExcelProductEmp = 0

    codigoMenu = '01000101'


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

    time.sleep(20)

    #get urls of all products 
    allProducts = self.driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/div/section[2]/div[2]/div[2]/div[2]/div[2]/div')
    for iprod, allProduct in enumerate(allProducts.find_elements(By.CLASS_NAME, 'Showcase__name')):
      if (iprod < 4):
        urlProducto = allProduct.get_attribute("href")        
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])          
        self.driver.get(urlProducto)  
        time.sleep(10)
        #start scraping product               
                
        #getMark
        getMark = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[1]/div[1]/span[1]/div/a')
        #getProduct
        getProduct = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[1]/div[1]/h6/div')        
        #getPriceRegulate
        if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[3]/div[2]').get_attribute('class') == 'ProductCard__price ProductCard__price--regular':
          getPriceRegulate = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[3]/div[2]')
          getPriceRegulate = getPriceRegulate.text
          getPriceRegulateFlag = 1
          getPercentDiscount = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[3]/div[3]/div[2]/span')
          getPercentDiscount = getPercentDiscount.text
        else: 
          getPriceRegulate = 0.00
          getPriceRegulateFlag = 0
          getPercentDiscount = 0.00
        #getPriceOnline
        getPriceOnline = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[3]/div[3]/div[1]')
        getPriceOnline = getPriceOnline.text
        getPriceOnlineFlag = 1
        #product

        if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[8]/span[1]').get_attribute('class') == 'ProductCard__marketplace__logo-text':
          getCorpSell = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[8]/span[1]').text
          getCorpSellFlag = 1          
        elif self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[8]/span[1]').get_attribute('class') == 'ProductCard__marketplace__logo':
          getCorpSell = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[1]/div[4]/div[2]/div[8]/span[1]').value_of_css_property('background-image')
          getCorpSellFlag = 1
        else:
          getCorpSell = ''
          getCorpSellFlag = 0

        matrizProduct[rowGlobalProduct][0] = codigoMenu 
        matrizProduct[rowGlobalProduct][1] = rowGlobalProduct 
        matrizProduct[rowGlobalProduct][2] = getProduct.text 
        matrizProduct[rowGlobalProduct][3] = getMark.text 
        matrizProduct[rowGlobalProduct][4] = 1 
        rowGlobalProduct += 1   

        #product comparny
        
        matrizProductEmp[rowGlobalProductCom][0] = codigoMenu 
        matrizProductEmp[rowGlobalProductCom][1] = rowGlobalProductCom
        matrizProductEmp[rowGlobalProductCom][2] = getProduct.text
        matrizProductEmp[rowGlobalProductCom][3] = getMark.text 
        matrizProductEmp[rowGlobalProductCom][4] = getPriceRegulate
        matrizProductEmp[rowGlobalProductCom][5] = getPriceRegulateFlag
        matrizProductEmp[rowGlobalProductCom][6] = getPriceOnline
        matrizProductEmp[rowGlobalProductCom][7] = getPriceOnlineFlag
        matrizProductEmp[rowGlobalProductCom][8] = getPercentDiscount
        matrizProductEmp[rowGlobalProductCom][9] = ruc
        matrizProductEmp[rowGlobalProductCom][10] = nameCor
        matrizProductEmp[rowGlobalProductCom][11] = rucCorpSell
        matrizProductEmp[rowGlobalProductCom][12] = getCorpSell
        matrizProductEmp[rowGlobalProductCom][13] = getCorpSellFlag
        matrizProductEmp[rowGlobalProductCom][14] = 1
        rowGlobalProductCom += 1

        
        #scraping description 
        if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[1]').get_attribute('class') == 'selector':                               
          self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[1]').click()
          #getDescription
          getDescription = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[2]/div')

          matrizOtherDesc[rowGlobalOtherDesc][0] = codigoMenu
          matrizOtherDesc[rowGlobalOtherDesc][1] = rowGlobalOtherDesc
          matrizOtherDesc[rowGlobalOtherDesc][2] = getDescription.text
          matrizOtherDesc[rowGlobalOtherDesc][3] = './'
          rowGlobalOtherDesc += 1   

        #scraping characterisc
        if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[3]').get_attribute('class') == 'selector':          
          self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[3]').click() 

        #technical specifications 
        if self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[5]').get_attribute('class') == 'selector':

          self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[5]/div[1]/div[5]').click()      
          #array               
          for i, row in enumerate(self.driver.find_elements(By.TAG_NAME, 'tr')):       
            for j, cellth in enumerate(row.find_elements(By.TAG_NAME, 'th')):                
              matrizEspTec[rowGlobalEspTec][0] = codigoMenu
              matrizEspTec[rowGlobalEspTec][1] = iprod + 1
              matrizEspTec[rowGlobalEspTec][2] = i + 1
              matrizEspTec[rowGlobalEspTec][3] = cellth.text
              matrizEspTec[rowGlobalEspTec][5] = 0
              matrizEspTec[rowGlobalEspTec][6] = 1
              # print("j" + str(j))    
              # print(cellth.text)
            for j, celltd in enumerate(row.find_elements(By.TAG_NAME, 'td')):
              matrizEspTec[rowGlobalEspTec][4] = celltd.text
            #global row
            rowGlobalEspTec += 1
        #end scraping product

        time.sleep(10)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    self.driver.quit()


    #push data to excel
    wb = xlsxwriter.Workbook('ProductoPlavaVea.xlsx') 
    # add_sheet is used to create sheet. 
    wsProduct = wb.add_worksheet('PRODUCTO') 
    for codigoMenu, rowGlobalProduct, getProduct, getMark, estado  in (matrizProduct):
      wsProduct.write(rowExcelPro, colExcelPro, codigoMenu)
      wsProduct.write(rowExcelPro, colExcelPro + 1, rowGlobalProduct)
      wsProduct.write(rowExcelPro, colExcelPro + 2, getProduct)
      wsProduct.write(rowExcelPro, colExcelPro + 3, getMark)
      wsProduct.write(rowExcelPro, colExcelPro + 4, estado)
      rowExcelPro += 1
    
    wsOtherDesc = wb.add_worksheet('OTRADESC') 
    for codigoMenu, rowGlobalOtherDesc, getDescription, car in (matrizOtherDesc):
      wsOtherDesc.write(rowExcelOtherDes, colExcelPro, codigoMenu)
      wsOtherDesc.write(rowExcelOtherDes, colExcelPro + 1, rowGlobalOtherDesc)
      wsOtherDesc.write(rowExcelOtherDes, colExcelPro + 2, getDescription)
      wsOtherDesc.write(rowExcelOtherDes, colExcelPro + 3, car)      
      rowExcelOtherDes += 1
        
    wsEspTec = wb.add_worksheet('ESP_TECNICAS')

    for codigoMenu, codigoProducto, i, cellth, celltd, j, z in (matrizEspTec):
      wsEspTec.write(rowm, colm, codigoMenu)
      wsEspTec.write(rowm, colm + 1, codigoProducto)
      wsEspTec.write(rowm, colm + 2, i)
      wsEspTec.write(rowm, colm + 3, cellth)
      wsEspTec.write(rowm, colm + 4, celltd)
      wsEspTec.write(rowm, colm + 5, j)
      wsEspTec.write(rowm, colm + 6, z)
      rowm += 1

    wsCorEmp = wb.add_worksheet('PRODUCTO-EMPRESA')

    for codigoMenu, rowGlobalProductCom, getProduct, getMark, getPriceRegulate, getPriceRegulateFlag, getPrecioOnline, getPriceOnlineFlag, getPercentDiscount, ruc, nameCor, rucCorpSell, getCorpSell, getCorpSellFlag, estado in (matrizProductEmp):
      wsCorEmp.write(rowExcelProductEmp, colm, codigoMenu)
      wsCorEmp.write(rowExcelProductEmp, colm + 1, rowGlobalProductCom)
      wsCorEmp.write(rowExcelProductEmp, colm + 2, getProduct)
      wsCorEmp.write(rowExcelProductEmp, colm + 3, getMark)
      wsCorEmp.write(rowExcelProductEmp, colm + 4, getPriceRegulate)
      wsCorEmp.write(rowExcelProductEmp, colm + 5, getPriceRegulateFlag)
      wsCorEmp.write(rowExcelProductEmp, colm + 6, getPrecioOnline)
      wsCorEmp.write(rowExcelProductEmp, colm + 7, getPriceOnlineFlag)
      wsCorEmp.write(rowExcelProductEmp, colm + 8, getPercentDiscount)
      wsCorEmp.write(rowExcelProductEmp, colm + 9, ruc)
      wsCorEmp.write(rowExcelProductEmp, colm + 10, nameCor)
      wsCorEmp.write(rowExcelProductEmp, colm + 11, rucCorpSell)
      wsCorEmp.write(rowExcelProductEmp, colm + 12, getCorpSell)
      wsCorEmp.write(rowExcelProductEmp, colm + 13, getCorpSellFlag)
      wsCorEmp.write(rowExcelProductEmp, colm + 14, estado)
      rowExcelProductEmp += 1


    wb.close()
PlazaVea = PlazaVea()
PlazaVea.entry()