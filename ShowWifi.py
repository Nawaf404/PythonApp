import datetime
import socket
import subprocess

print('''
         --------------------------
        -       Hello World        -
        |__________________________|''')

print('''
    |--------------------------------------------|
    |   Here Will Show All of Wife you Used it   |
    |                                            |
    |______________-2020/4/10-___________________|

''')

today = datetime.datetime.now()
print("""\n\n 
   __         __             ______        ___            ___            __          _____            ________________ 
  |  |       |  |           / ___ \        \  \          /   \          / /         /  ___ \          |  |____________|
  |   \      |  |          / /   \ \        \  \        /  /\ \        / /         /  /   \ \         |  |
  |   \ \    |  |         / /_____\ \        \  \      /  /  \ \      / /         /  /_____\ \        |  |___________
  |  | \ \   |  |        /  _______  \        \  \    /  /    \ \    / /         /  ________  \       |  |___________|
  |  |  \ \  |  |       /  /       \  \        \  \  /  /      \ \  / /         /  /        \  \      |  |
  |  |   \ \ |  |      /  /         \  \        \  \/ /         \ \/ /         /  /          \  \     |  |  
  |__|    \__|_|      /__/           \__\        \___/           \__/         /__/            \__\    |__| 
                                     
                                      
                                            -- V e r s i o n   1.0  -- 
              \_____/
              ( * * )                       | Welcome To Nawaf Tools |
          _  |-------|  _
         | | |       | | |
         | | |       | | |                  [+] Created By Nawaf [+]
         |_| |_______| |_|                  
               _    _                        || G i T H U B |
              |  | | |                 
              |_|  |_|                 [+] https://github.com/Nawaf404 [+]
                                
""")
now = datetime.datetime.now()
NameDay = now.strftime("%A")
DateT = datetime.datetime.now().day
DateM = datetime.datetime.now().month
DateMonthName = datetime.datetime.now()
Monthname = DateMonthName.strftime("%B")
YearDate = datetime.datetime.now().year
slash = " / "
whitespaces = " "
Date = NameDay + whitespaces + str(DateT) + whitespaces +  Monthname + whitespaces + slash + whitespaces +str(DateM)+ whitespaces + slash +whitespaces+ str(YearDate)
print("Date Today :\n\n {} ".format(Date))

today = datetime.datetime.now().today()
print("\n\n Current date Today : \n\n" , today)


print('''\n\n                                 Welcome          \n\n''')
print("                              Tools | Nawaf |   \n")
print("""                            |---------------------|
                            |                     |
                            |  WE WATCHING YOU    |
                            |                     | 
                            |       \_____/       |
                            |       ( *  * )      |
                            |        \_==_/       |
                            |_____________________|""")
admin = socket.gethostname()
IPadmin = socket.gethostbyname(admin)
print("\n\nYour Computer Name is : " , admin , "\n\nYour iP Address : " , IPadmin)
print("\n========================================")
print("\n\n")
input('')


print("--- Will Show All Wifi --- ")
print('\n\n Just Wait a moment ..')



results = subprocess.check_output(['netsh','wlan','show','network'])
results = results.decode("ascii")
results = results.replace("\r","")
ls  = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls) :
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)
input('')