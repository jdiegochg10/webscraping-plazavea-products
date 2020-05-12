from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PlazaVea():
  

  def __init__(self):
    self.driver = webdriver.Chrome(executable_path="D:/Aplicaciones/automation-browser/drivers/chromedriver.exe")  

  def entry(self):
    lista = []
    base_url = 'https://www.plazavea.com.pe'
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    self.driver.get(base_url)
    buttonElectro = self.driver.find_element_by_xpath('//*[@id="event-nonfood"]').click()
    buttonBazar = self.driver.find_element_by_xpath('/html/body/div[3]/header/section/div[3]/div[4]/div/ul/div/li[3]').click()
    buttonAccesorioAuto = self.driver.find_element_by_xpath('//a[contains(text(),"Accesorios para auto")]').click()  
        
    WebDriverWait(self.driver, 100).until(
        EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[3]/main[1]/div[1]/div[4]/div[1]/section[2]/div[2]/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[3]/div[5]/a[1]"))
    )
  
    productBazar = self.driver.find_element_by_xpath("/html[1]/body[1]/div[3]/main[1]/div[1]/div[4]/div[1]/section[2]/div[2]/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[3]/div[5]/a[1]").click()


    #   sleep(3) 
    # except:
      # pass
  
    #active descripcion
    productDescription = self.driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[4]/div[5]/div[1]/div[1]').click()
    #active tecni    
    especificationTechical = self.driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[4]/div[5]/div[1]/div[5]').click()

    elementDescriptionProduct = self.driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[4]/div[5]/div[1]/div[2]/div[1]')
    
    elementProduct = self.driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[4]/div[4]/div[1]/div[1]/h6[1]/div[1]')
    product = elementProduct.text
    elementMark = self.driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[4]/div[4]/div[1]/div[1]/span[1]/div[1]/a[1]')
    mark = elementMark.text

    [] lista = self.driver.find_elements(By.XPATH('//*[@id="caracteristicas"]/table/tbody/tr[1]/th'))


    self.driver.close()

    print(product)
    print(mark)
    print(len(lista))

  # def EspecificationTechnical(self):



bot = PlazaVea()
bot.entry()


# print(descriptionProduct)
# print(rowData)



#scraping




# descriptionProduct = elementDescriptionProduct.text

# #count rows table - technical especifications

# rowData = []
# rowHeader = []

# headLine = driver.find_element_by_tag_name('tr')
# headers = headLine.find_elements_by_tag_name('th')

# for header in headers:
#   headerText = header.text.encode('utf8')
#   rowHeader.append(headerText)
# rowData.append(",".join(rowHeader))



# array = []

# for 

# th 
# td 


