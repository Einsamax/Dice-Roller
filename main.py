from time import sleep
import random

#Introduce user to the program
if __name__ == "__main__":
    print ("*" * 32)
    print("Welcome to the Dice Roller!".center(32))
    print ("*" * 32)
    print()

    sleep(1)

rolling=True
while rolling:
    #prompt user to chose their dice type
    print("*" * 32)
    print("Which type of dice would you like to roll?")
    sleep(1)
    print("You may select from D2, D3, D4, D6, D8, D10, D12, D20, and D100!")
    sleep(1)
    print("You may also type 'exit' to leave the program.")
    dicetype = str(input()) #User enters the type of dice they wish to roll
    dicetotal=0 #Sets and resets the dicetotal to 0
    diceroll=0 #sets and resets the diceroll to 0
    if dicetype == "D2" : #Player chose D2
        sleep(1)
        print("How many D2 would you like to roll?")
        numdice = input() #User enters how many dice to roll
        print("Rolling", int(numdice), "D2!") #Prompt confirms user input
        sleep(1)
        for numdice in range (1,int(numdice) + 1): #Repeats the loop for the number of rolls enetered
            diceroll = (random.randint(1,2)) #Rolls the dice based on D2 roll
            dicetotal = dicetotal + diceroll #Adds the dice roll to the total value of entered dice rolls
            print("You rolled a", diceroll, "!" ) #Prints the diceroll for each loop
            sleep(1)
        print("Your total is", dicetotal, "!") #Once all rolls are complete the sum of all rolls is printed
        sleep(1)
    elif dicetype == "D3" : # Player chose D3
        sleep(1)
        print("How many D3 would you like to roll?")
        numdice = input()  # User enters how many dice to roll
        print("Rolling", int(numdice), "D3!")  # Prompt confirms user input
        sleep(1)
        for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
            diceroll = (random.randint(1, 3))  # Rolls the dice based on D3 roll
            dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
            print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
            sleep(1)
        print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
        sleep(1)
    elif dicetype == "D4" : # Player chose D4
        sleep(1)
        print("How many D4 would you like to roll?")
        numdice = input()  # User enters how many dice to roll
        print("Rolling", int(numdice), "D4!")  # Prompt confirms user input
        sleep(1)
        for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
            diceroll = (random.randint(1, 4))  # Rolls the dice based on D4 roll
            dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
            print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
            sleep(1)
        print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
        sleep(1)
    elif dicetype == "D6":  # Player chose D6
        sleep(1)
        print("How many D6 would you like to roll?")
        numdice = input()  # User enters how many dice to roll
        print("Rolling", int(numdice), "D6!")  # Prompt confirms user input
        sleep(1)
        for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
            diceroll = (random.randint(1, 6))  # Rolls the dice based on D6 roll
            dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
            print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
            sleep(1)
        print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
        sleep(1)
    elif dicetype == "D8" : # Player chose D8
        sleep(1)
        print("How many D8 would you like to roll?")
        numdice = input()  # User enters how many dice to roll
        print("Rolling", int(numdice), "D8!")  # Prompt confirms user input
        sleep(1)
        for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
            diceroll = (random.randint(1, 8))  # Rolls the dice based on D8 roll
            dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
            print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
            sleep(1)
        print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
        sleep(1)
    elif dicetype == "D10":  # Player chose D10
        sleep(1)
        print("How many D10 would you like to roll?")
        numdice = input()  # User enters how many dice to roll
        print("Rolling", int(numdice), "D10!")  # Prompt confirms user input
        sleep(1)
        for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
            diceroll = (random.randint(1, 10))  # Rolls the dice based on D10 roll
            dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
            print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
            sleep(1)
        print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
        sleep(1)
    elif dicetype == "D12":  # Player chose D12
        sleep(1)
        print("How many D12 would you like to roll?")
        numdice = input()  # User enters how many dice to roll
        print("Rolling", int(numdice), "D12!")  # Prompt confirms user input
        sleep(1)
        for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
            diceroll = (random.randint(1, 12))  # Rolls the dice based on D12 roll
            dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
            print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
            sleep(1)
        print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
        sleep(1)
    elif dicetype == "D20":  # Player chose D20
            sleep(1)
            print("How many D20 would you like to roll?")
            numdice = input()  # User enters how many dice to roll
            print("Rolling", int(numdice), "D20!")  # Prompt confirms user input
            sleep(1)
            for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
                diceroll = (random.randint(1, 20))  # Rolls the dice based on D20 roll
                dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
                print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
                sleep(1)
            print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
            sleep(1)
    elif dicetype == "D100":  # Player chose D100
            sleep(1)
            print("How many D100 would you like to roll?")
            numdice = input()  # User enters how many dice to roll
            print("Rolling", int(numdice), "D100!")  # Prompt confirms user input
            sleep(1)
            for numdice in range(1, int(numdice) + 1):  # Repeats the loop for the number of rolls entered
                diceroll = (random.randint(1, 100))  # Rolls the dice based on D12 roll
                dicetotal = dicetotal + diceroll  # Adds the dice roll to the total value of entered dice rolls
                print("You rolled a", diceroll, "!")  # Prints the diceroll for each loop
                sleep(1)
            print("Your total is", dicetotal, "!")  # Once all rolls are complete the sum of all rolls is printed
            sleep(1)
    elif dicetype == "exit": #Player wishes to close the program
        sleep(1)
        print("Thank you for rolling your luck!")
        sleep(2)
        rolling = False #exits the while loop

    else:
        print("Uh oh! It looks like you entered an invalid dice type!")
        sleep(1)






