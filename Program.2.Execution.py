#Binh Mai
#CS101
#Program 2

#Prompt user if they want to play against another player of a computer
#   If incorrect value, computer should prompt for correct value
#Prompt user for the number of sticks they want to play with
#   If user inputs incorrect value, let user knows their value was incorrect
#If against a computer, user goes first. 
#If against another player, users decide amongst themselves
#
#Start game!
#
#If the user is playing against a computer, the computer will be randomized
#Prompt user for the number of sticks they want
#If they pick an invalid prompt, they will be prompted for a correct value
#Subtract the number of sticks they choose from the total amount of sticks
#Display the number of sticks they picked up as well as the number of sticks left
#The AI will then play and pick a number of sticks to use
#Display the number of sticks the AI picked up as well as how many are left
#Repeatuntil there are three sticks left
#Afterwards the amount of choices are limited based on how many sticks are left
#Whomever picks up the last stick is the loser
#The winner of the game will be congratulated and given a message
#
#If the user if playing against another person,
#The first player will be prompted for the number of sticks they want to pick up
#Subtract that number from the total amount of sticks left and display what's left
#The second player will then be prompted for the number of sticks they want to pick up
#Subtract that number from the total amount of sticks left and display what's left
#Repeat the first player's and second player's turns until there are 3 sticks left
#Once there are 3 sticks left, the choices are limited based on the remaining number
#   of sticks
#Whomever picks up the last stick will be the loser
#The winner is whoever doesn't pull up the last stick and will be congratulated
#   with a message
#
#For both games, the program should ask the user if they want to play again
#If should have a list of allowable affirmative and negative input that will be
#   allowed for the user to input.
#If the user inputs an unacceptable command they will be given a list of acceptable
#   commands and told to input the right ones

#Make a value of still_playing that will determine the whole game. So long as this
#value remains true, all of the loops will run. However, if the user decides to no
#longer play, it will stop. I am also initializing all variables in this beginning step. 

still_playing = True;
total_sticks = 0
import random #importing module for the computer 
rules_for_two_players = """

        Let's review the rules for two players!
        Decide amongst yourselves who will go first
        Player 1 will decide to take a number of sticks from the pile
        Pick carefully as you can only pick 1, 2 or 3 sticks at a time!
        Then switch to Player 2
        Continue switching back and forth.
        Whoever picks the last stick is the loser!
        Good luck and enjoy the following game! 
        """
rules_against_the_computer = """

        To play against the computer
        You'll go first
        You will select a number of sticks to take away from the pile
        Pick carefully as you can only pick 1, 2, or 3 sticks at a time
        The computer will pick a random number of sticks
        You'll take turns with the computer
        Whoever picks up the last stick is the loser!
        Good luck and enjoy the following game!
        """


while still_playing:

#Use code to determine from the user input who they will be playing against. Prompt
#user if they input an incorrect value
        
        while True:
                game = (input("Would you like to play a game of sticks? \
Type in 1 to play against another player and 2 to play against a computer!"))
                if game == "1":
                        print ("Let's decide how many sticks you want to play with")
                        break
                elif game == "2":
                        print ("Great! Decide how many sticks you want to play with against the \
computer.")
                        break
                else:
                        print ("I'm sorry, but I can only take 1 or 2. Please choose\
1 to play against another player or 2 to play against the computer")
                        continue

#If playing against another player
#Prompt user for the number of sticks they want to play with

        while game == "1":
                total_sticks = int(input("How many sticks would you like to play with? Pick a number \
between 10 and 50:"))
                if total_sticks >= 10 and total_sticks <= 50:
                        print ("Great! Let's go over the rules really fast") #Used to check code
                        print (rules_for_two_players) #Just for reference for user
                        break
                if total_sticks < 10 or total_sticks > 50:
                        print ("I'm sorry but I can only accept values from 10 to 50. Please choose\
a value from 10 to 50:")
                        continue

#Starting the game now.
#FIRST FIND A WAY TO GET FROM THE PREVIOUS LOOP TO THIS LOOP
                #THEN FIGURE OUT HOW TO SUBTRACT STUFF AND LOOP. 

                while total_sticks >= 10 and total_sticks <= 50:
                        p_one_sticks = int(input("How many sticks will Player One take?"))
                        if 1 <= p_one_sticks < 4:
                                total_sticks -= p_one_sticks
                                print ("Player One took {} sticks. There are {} sticks left!")

#If playing against the computer
#First the player has to determine the total amount of sticks they want to play with

        while game == "2":
                total_sticks = int(input("How many sticks would you like to play with? Pick a number\
between 10 and 50:"))
                if total_sticks >=10 and total_sticks <=50:
                        print("Great! Let's just go over the rules really fast") #Used to check code
                        print (rules_against_the_computer) #Just for reference for user
                        break
                if total_sticks < 10 or total_sticks > 50:
                        print ("I'm sorry but I can only accept values from 10 to 50. Please choose\
a value from 10 to 50:")
                        continue

                
#Now that we know the number of sticks the two players want to use, let's start the game!
#STOPPING POINT 9/18/2014

