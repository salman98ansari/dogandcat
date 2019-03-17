import os
os.chdir('C:\\Users\\Salman\\Desktop\\Images\\FEMALE') #path to folder
i=1
for file in os.listdir():
      src=file
      dst="female"+str(i)+".jpg"  #it will append male+i in renamed ,change i resspectively
      os.rename(src,dst)
      i+=1


#file will be renamed in same directory 
