import winsound
frequency = 2500 ## Set Frequency To 2500 Hertz
duration = 1000 # Set Duration To 1000 ms == 1 second
Ask = input("Are You Ready To Hear The Sound ?  : ")
winsound.Beep(frequency,duration)
def sos():
    for s in range(0,3):
        winsound.Beep(2000, 100)
        for n in range(0,3):
            winsound.Beep(2000, 400)
            for j in range(0,3):
                winsound.Beep(2000, 100)
sos()