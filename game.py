#keep track of money/score when at 1000 you win!

#game logic
#get user input
#keep track of tools in tool box
#keep track of tools to buy/once bought, no longer an option
money = 0

print("Welcome to the lawnmower app. Make $1000 and hire starving students to win!")


class tool:
    def __init__ (self, name, cost, pay, own):
        self.name = name
        self.cost = cost
        self.pay = pay
        self.own = own
    def stats(self):
        print(f"Using {self.name} will cost {self.cost} to purchase and return {self.pay}. You currently have {money}")
        if self.own == True:
            print(f"You currently have {self.name}")
        else:
            print(f"You do not own {self.name}")

teeth = tool("teeth", 0, 1, True)
scissors = tool("rusty scissors", 5, 5, False)
pushLawn = tool("push lawnmower", 25, 50, False)
electricLawn = tool ("electric lawnmower", 250, 100, False)
hireTeam = tool("starving students", 500, 250, False)

tools = [
    teeth,
    scissors,
    pushLawn,
    electricLawn,
    hireTeam
]

# print(hireTeam.own)


# def salary(pay):
#     return (money + pay)


# print("Landscaper user can use teeth to cut grass")


# def buyTools():

# def cutGrass():

# Run game
def userChoice(choice):
    if choice == 'buy':
        print("What would you like to buy?")
    elif choice == 'cut':
        print("What would you like to cut with?")
    else:
        print("Not an option, try again.")

while money <= 100 and hireTeam.own == False: 
    user_input = input("Would you like to buy new tools or cut grass? (Type 'buy/cut' to choose or 'quit' to leave the app) ")
    if user_input == 'quit':
        print('You have quit the app')
        break
    else:
        userChoice(user_input)