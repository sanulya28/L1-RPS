# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question). lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                 return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Display instructions
def instruction():
    print('''

**** Instructions ****

To begin, decide on a score goal (e.g.: The first one to get a 
score of 50 wins).

For each round of the game, you win points by rolling dice.
The winner of the round is the one who gets 13 (or slightly less).

If you win the round, then your score will increase by the
number of points that you earned. If your first roll of two 
dice is a double (e.g. both dice show a three), then your score
will be DOUBLE the number of points.

If you lose the round, then you don't get any points.

If you and the computer tie (i.e. you both get a score of 11,
then you will have 11 points added to your score.

Your goal is to try to get to the target score before the 
computer. 

Good luck

    ''')

# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than/ equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)
          
# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📃✂️ Rock / Paper / Scissors Game 💎📃✂️")
print()

# ask user if they want to see  the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n⊚⊚⊚ Round {rounds_played + 1} (Infinite Mode) ⊚⊚⊚"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)
    print()

# get user choice
    user_choice = string_checker("choose: ", rps_list)
    print("you chose", user_choice)

# If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1




# Game loop ends here

# Game History / Statistics area