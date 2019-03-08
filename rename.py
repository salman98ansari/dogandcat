import os
os.chdir('C:\\Users\\Salman\\Desktop\\salman1\\valid\\male')
i=1
for file in os.listdir():
      src=file
      dst="male"+str(i)+".jpg"
      os.rename(src,dst)
      i+=1
