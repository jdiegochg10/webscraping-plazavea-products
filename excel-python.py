import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('PRODUCTO') 
  
sheet1.write(0, 0, 'CodigoMenu') 
sheet1.write(0, 1, 'NombreProducto') 
sheet1.write(0, 2, 'DescripcionMarca') 
sheet1.write(0, 3, 'Estado') 
  
wb.save('ProductoPlavaVea.xls') 


