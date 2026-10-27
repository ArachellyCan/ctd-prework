from types import get_original_bases
# #Section 1: Variables and types

#Variables defined
first_name ="Jorge"
age_now= 28
height_altura = 5.8
my_brother = True
month = "October"
zodiac= "Libra"

#using the Funcion type to find Data Type
print(first_name,type(first_name))
print(age_now,type(age_now))
print (height_altura, type(height_altura))
print(my_brother,type(my_brother))

print()
print()
print()

#Section 2: User Input (funtion) and Math using previous Variables

#What is a variable? It is a name that stores a value
#types of Variables
#sting (str) text
#intger(int) whole numbers
#Float (float) Decimals
#Boolean (bool)
#Declared variables True or Fals




first_name = input ("name ")
first_name = str(first_name)

year_born = input ("Birth year   ")
year_born =int (year_born)

#print(first_name + str(year_born))

age_now = input("How old are you?  ")
#age_now = int (age_now)

age_now = 2029 -year_born

print(f"Hello, {first_name} ,you are aproximatekt {next_year} years old  ")



#Section 3: Conversion and f-strings

number_1 = input("Enter the first decimal number  ")
number_1 = float(number_1)

number_2 = input("Enter the second decimal number  ")
number_2 = float(number_2)

print(f"The result of the multiplication is, {number_1 * number_2}  ")

# #Section 4: Formatted Receipt
print()
print()
print()
print("=========Food========")
print("Uber Eats  -  Takeout")
print("# Number")
print("=====================")
print("Server: Default  0   ")
print("UE -- Customer Name  ")
print("Order Number         ")
print()
print()
print()
#Section 5 Profile Card
first_name = "JJorge"
Hometown = "Mexico, City"
Hobby = "Learning about Mexican Civilizations"
Fun_Fact = "Astrology"
Occasion = "Birthday"
Zodiac = "Libra"
month="October"




first_name = input("PROFILE name  ")
#first_name = str("first_name")

Hometown = input("What is your home town ?   ")
#Hometown = str(Hometown)

Hobby = input("What is your Hobby   ")
#Hobby = str(Hobby)

Fun_Fact = input("fun fact  ")
#Fun_Fact = str(Fun_Fact)# other wise you are changing the value of the variable
#Therefore not printing the correct Values

Year = input("Year you were born   ")
Year = int(Year) #int is just use to convert a str to an int to do the math
Present_Year = 2026-Year
print ("Your age is:", Present_Year)
print()
print()
print()



print()
print(f"=======Greeting Card Generator=======")
print()
print(f"      PROFILE  {first_name}         ")
print()
print(f"      Hometown: {Hometown}       ")
print()
print(f"      Hobby: {Hobby}          ")
print()
print(f"      Fun fact: {Fun_Fact} about your self   ")
print()
print(f"      Age:  {Present_Year}   ")
