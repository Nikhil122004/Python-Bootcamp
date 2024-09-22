import random
secret_number= random.randint(1, 50)

#assigning the total attempts=5
attempts = 5

print("Guess the secret number between 1 and 50. You have 5 attempts!")

while attempts > 0: 
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < 1 or user_guess > 50:
            print("Please enter a number between 1 and 50.")
            continue
        
        if user_guess < secret_number:
            print("Your input is very low. Try again.")
        elif user_guess > secret_number:
            print("Your input is very high. Try again.")
        else:
            print("Congratulations! You won!")
            break

        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    


if attempts == 0:
    print(f"Sorry, you've used all your attempts. You lose. The secret number was {secret_number}.")
   
