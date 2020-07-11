#Bisection Algorithm

print("Please think of a number between 0 and 100!")
high = 100
low = 0
while True:
    guess = int((high + low)/2)
    print("Is your secret number " + str(guess) + "?")
    accuracy = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if accuracy == "h":
        high = guess
    elif accuracy == "l":
        low = guess
    elif accuracy == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
