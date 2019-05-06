import time
from datetime import datetime as dt 

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
#localhost's IP 
redirect="127.0.0.1"
#The websites you want to block
website_list=["www.google.com", "google.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() <dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours")
        with open (hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n") #write hostnames to localhost IP address

    else:
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #remove hostnames from host file
        print("fun hours")

#repeat the while loop every 60 seconds
time.sleep(60)


