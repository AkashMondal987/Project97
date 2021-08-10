import random
print ("Number Guessing Game")
number = random.randint(1,10)
chance = 0
print ("Guess A Number Between 1 To 10")
while chance < 5:
    guess = int (imput("Enter Your Guess: "))
    if guess == number: 
        print ("Congratulatios You Won")
        break
    elif guess < number:
        print ("Guess A Higher Number", guess)
    else:
        print ("Guess A Lower Number", guess)
    chance += 1
if not chance < 5:
    print ("You Lose")