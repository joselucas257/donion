import os,time
os.system ("unzip tor.zip && unzip nginx.zip")
time.sleep (2)
print ("instalando os recursos")
os.system ("apt install nginx -y && apt install tor -y")
time.sleep (4)
os.system ("cp -r nginx /usr/share")
time.sleep (2)
os.system ("cp -r tor /etc")
os.system ("killall -9 nginx")
os.system ("killall -9 tor")
time.sleep (2)
os.system ("nginx")
os.system ("tor")

