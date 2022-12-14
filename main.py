from random import*

#greet user
print("Welcome to guess my number! I will pick a number a random numbe and you will try and guess it, good luck!")

#generate random number
random_number = randint(1,6)

#ask user for number
guess = int(input("enter your guess:"))

#check if answer is correct
if random_number == guess:
  print("correct the number was " + str(random_number))
else:
  print("incorrect the number was  " + str(random_number))