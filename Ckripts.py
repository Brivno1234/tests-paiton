import os
import time

import csv
import datetime


# сохранить в вайлик резульнаты пинга

hosts= ["8.8.8.8", "1.1.1.1", "192.168.1.1"]
now = datetime.datetime.now()
print(now)
#Time.status
#05.06.20.25 ok
#05.06.20.25,Fail

with open("ping_log.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Time","Status"])



while True:
    print("Kättesadavuse kontroll")
    now = datetime.datetime.now()
    result = ""
    for elem in hosts:
        response =os.system(f"ping -n 1 {elem} > null")
        if response == 0:
            resalt = "ok"
            print(elem, "kätesadavalt")
        else:
            resalt = "fail"
            print(elem ," ei ole kättesadavalt")
            
        with open("ping_log.csv","a") as file:
            writer = csv.writer(file)
            writer.writerow([ now,result ])            
            
            
            
        print("-"*30)
        time.sleep(0)
        