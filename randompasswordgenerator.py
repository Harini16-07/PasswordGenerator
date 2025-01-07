import random
import string
user=int(input("Enter the length of the password"))
print("Choose the opertion to be performed:")
print("1.Characters") 
print("2.Digits")
print("3.Special Characters")
print("4.Exit")

arr=""
while True:
    choice=int(input())
    if(choice==1):
        arr=arr+string.ascii_letters
        print("Character added to the password")
    elif(choice==2):
        arr=arr+string.digits
        print("Digits added to the password")

    elif(choice==3):
        arr=arr+string.punctuation
        print("Speacial Character added to the password")

    elif(choice==4):
        
        break
    else:
        print("Please,provide a valid input")
password=[]
for i in range(user):

  ranchoice=random.choice(arr)
  password.append(ranchoice)


print("Password:"+"".join(password))
       
