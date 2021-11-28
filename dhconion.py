import os,time

time.sleep (2)
print ("instalando os recursos")
os.system ("apt install nginx -y && apt install tor -y")
time.sleep (4)
os.system ("cp -r nginx /usr/share")
time.sleep (2)
os.system ("cp -r tor /etc")
time.sleep (2)
os.system ("nginx")
os.system ("tor")
