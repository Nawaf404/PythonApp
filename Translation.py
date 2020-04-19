import datetime
import googletrans
from googletrans import Translator
import datetime

print("Datetime Now : " , datetime.datetime.now())

result = Translator()
print("\nWill Translate from English To Arabic\n\n")
Ask = input("Enter English Word : ") 
print("just give me a moment")
TransEnglish = result.translate(Ask,src='en',dest='ar')
print("The Laungages of The Word :", TransEnglish.src)
print("Word will translate to :",TransEnglish.dest)
print("The Orginal Word is :", TransEnglish.origin)
print("Translation :" , TransEnglish.text)
print("\n\n----- WIll Translate Now from Arabic to English ----\n ")
Ask2 = input("Enter Arabic Word : ")

TransArabic = result.translate(Ask2,src='ar',dest='en')
print("The Laungages of The Word :", TransArabic.src)
print("Word will translate to :",TransArabic.dest)
print("The Orginal Word is :", TransArabic.origin)
print("Translation :" , TransArabic.text)


## if time.night() :
##  start.programming !    



input("\n\n----- Thanks for using ------")
