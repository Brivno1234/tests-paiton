# import os
# import time
# 
# import csv
# import datetime
# 
# 
# # сохранить в вайлик резульнаты пинга
# 
# hosts= ["8.8.8.8", "1.1.1.1", "192.168.1.1"]
# now = datetime.datetime.now()
# print(now)
# #Time.status
# #05.06.20.25 ok
# #05.06.20.25,Fail
# 
# with open("ping_log.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Time","Status"])
# 
# 
# 
# while True:
#     print("Kättesadavuse kontroll")
#     now = datetime.datetime.now()
#     result = ""
#     for elem in hosts:
#         response =os.system(f"ping -n 1 {elem} > null")
#         if response == 0:
#             resalt = "ok"
#             print(elem, "kätesadavalt")
#         else:
#             resalt = "fail"
#             print(elem ," ei ole kättesadavalt")
#             
#         with open("ping_log.csv","a") as file:
#             writer = csv.writer(file)
#             writer.writerow([ now,result ])            
#             
#             
#             
#         print("-"*30)
#         time.sleep(0)
# #võimalus  vadata kõik protsesid arvutis#
#salvestada need failise tasklist [Time , processname,Memory Usage]

import csv
import datetime
import subprocess

# Создаем CSV-файл и записываем заголовки
with open("ping_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Process Name", "Memory Usage"])

# Получаем список процессов в формате CSV
output = subprocess.check_output("tasklist /FO CSV", shell=True, text=True)
lines = output.splitlines()

# Пропускаем заголовок
for line in lines[1:]:
    # Убираем кавычки и разбиваем строку
    parts = list(csv.reader([line]))[0]
    now = datetime.datetime.now()
    process_name = parts[0]
    memory_usage = parts[-1]

    # Записываем данные в CSV
    with open("ping_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, process_name, memory_usage])

    # Выводим информацию в консоль
    print("Time:", now, "Name:", process_name, "Memory:", memory_usage)


