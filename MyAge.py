import datetime ## import library datetime

year = int(input("Please Enter the year : "))
month = int(input("Please Enter the month : "))
day = int(input("Please Enter your day : "))
## Get Year, Month, Day from User

today = datetime.datetime.now() ## DATE Today
DOB = datetime.datetime(year, month, day)
age = today - DOB ## Minus today from DOB

print("You have live for : ", age)
final_age = age.days / 365 ## Div from age days to year(365 day)
print(f'Your Age Is : {final_age}\nExactly : ',int(final_age))
