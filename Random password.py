#Random password generator
import random
print("welcome to random password generator")
randomchar="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
number_of_password=int(input("Number of password you want:"))
length_of_password=int(input("Enter the length of the password:"))
print("Here the password:")
print("***********************")
for i in range(number_of_password):
    password=" "
    for char in range(length_of_password):
        password=password+random.choice(randomchar)
    print(password)

print("**********************")
        

