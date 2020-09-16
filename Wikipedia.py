import wikipedia
import os
import socket
import psutil
# import antigravity

import colorama
print(colorama.Fore.LIGHTCYAN_EX+"Welcome IN WIKIPEDIA Program ..!")

name = socket.gethostname()
ip = socket.gethostbyname(name)
battery = psutil.sensors_battery()
percent = str(battery.percent)
close = colorama.Style.RESET_ALL
print(close)
print("Welcome", colorama.Fore.RED + name)
print(close)

print("iP Address", colorama.Fore.LIGHTBLUE_EX + ip)
print(close)

print("Battery", colorama.Fore.GREEN + percent)
print(close)

def check(inputUser):
    import re
    pattern = "^[a-zA-Z]*$"
    if re.match(pattern, inputUser):
        pass
    else:
        print(colorama.Fore.RED+colorama.Back.BLACK+"Sorry must type correct type input")
        print(close)

lang = input("First type the Language what you want {shortcuts} : ")
check(lang)
try:
    ask = input(colorama.Back.CYAN+colorama.Fore.BLACK+"Enter word to search in WIKIPEDIA : ")
    check(ask), print(close)

    print("There's some title choose one :\n")
    for i in wikipedia.search(ask):
        print("- ", i)

    print("if there's no what you choose, type your word")
    choose = input(" : ")
    check(choose)
    page = wikipedia.page(choose)

    print("\n--------------------------------------------\n")
    print(wikipedia.summary(choose, sentences=3))
    print("\n----------------------------------------\nIt's Intro for the search")
    print("The Url : ", page.url)
except wikipedia.exceptions.PageError:
    print("Sorry the search dosen't match , try Another")
    exit()
except wikipedia.exceptions.DisambiguationError:
    print("Sorry the word isn't enough or correct, choose one from titles")
    exit()

page = wikipedia.page(choose)
AskSave = input("if you want to save the search type Y if not type n : ")
if AskSave == "Y":
    import datetime
    date = datetime.date.today()
    t = datetime.datetime.now()
    time = t.strftime("Day : %A and Time %H:%M:%S")
    nameFile = str(choose+"-1.txt")
    file = open(nameFile, 'w')

    file.write(str(date))
    file.write("\n")
    file.write(str(time))
    file.write("\n")
    file.write("------\nTitle : ")
    file.write(str(page.title))
    file.write("\n")
    file.write(str(page.url))
    file.write("\n-----------------------\n")
    file.write(str(wikipedia.summary(choose)))
    file.write("\n")
    file.close()
elif AskSave == "n":
    pass
else:
    print("sorry i don't understand 0")

askLong = input("Mmmm.. Hey User\neverything is good but do you want long article ? Y or n : ")
if askLong == "Y":
    print("Ok .. it's working now just wait")
    nameFileLong = str(choose+"2.txt")
    fileLong = open(nameFileLong, "w")
    fileLong.write("Title : ")
    fileLong.write(page.original_title)
    fileLong.write("\nPage ID : "), fileLong.write(page.pageid)
    fileLong.write("\nContent :\n")
    fileLong.write(page.summary)
    fileLong.write("\n------------------\n")
    fileLong.write(str(page.categories))
    fileLong.write("\n--------------------\nLinks :\n")

    fileLong.write(str(page.references))
    fileLong.write("And Last , URL  :\n"), fileLong.write(page.url)
    fileLong.close()

elif askLong == "n":
    print("Ok << thanks >> ")
else:
    print("sorry i don't understand")

askQR = input("Do you want to make QR Code ? Y n : ")
if askQR == "Y":
    import pyqrcode
    import png
    from pyqrcode import QRCode
    s = page.url
    url = pyqrcode.create(s)
    nameOfQR = str(choose+".svg")
    nameOfQRpng = str(choose+".png")
    url.svg(nameOfQR, scale=8)
    url.png(nameOfQRpng, scale=6)
    print("Done !")
    print("search it in your folder")
    print(f"its name : {nameOfQRpng} ")
    print("Thanks !")
elif askQR == "n":
    print("Ok .. will out now ")
    exit()
else:
    print("sorry i don't understand")
input("press anything to exit ... ")
# .. 1 - QR Code
# .. 2 - Save The Information in File
# .. 3 - Display only 5 lines as Intro
# .. 4 - take the url for qr, and show all of info
# .. 5 - import antigravity