print("What is your birth_year?") 
# Asking for your birth_year
myBirth_year = int(input("Please enter the year you were born:"))
Current_year = int(input("Kindly provide the current year that you are in:"))
myAge = Current_year- myBirth_year
if myAge == 19 :
    print("Hurry, you are " + str(myAge) + " years old")
else:
    print("Boo! you are not") 
