money = 0

print("\nWelcome to the lawnmower app. Make $1000 and hire starving students to win!")


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

teeth = tool("teeth", 0, 100, True)
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

def cutGrass():
    global money
    print("These are your options:(Type your selection)")
    for element in tools:
        if element.own == True:
            print(element.name)
            
    userCutGrass = input()
    for element in tools:
        if userCutGrass == element.name and element.own == True:
            money += element.pay
            print(f"You cut with {element.name} and got paid {element.pay}. You now have {money} in total.")
        # elif :
        #     print("Not a selection. Try again.")

def buyTools():
    global money
    global userBuyTool 
    print("\nThis is what you can buy: (Type your selection)")
    for element in tools:
        if element.own == False:
            print(f"{element.name}")
            
    userBuyTool = input()
    for element in tools:
        if  userBuyTool == element.name and element.own == False and money >= element.cost:
            money -= element.cost
            element.own = True
            print(f"\nYou bought {element.name} for {element.cost}. You now have {money} in total.")
            return
    print("\nNot enough money!")


# Run game
def userChoice(choice):
    if choice == 'buy':
        print("What would you like to buy?")
        buyTools()
    elif choice == 'cut':
        print("What would you like to cut with?")
        cutGrass()
    else:
        print("Not an option, try again.")

while money <= 1000 or hireTeam.own == False: 
    user_input = input("Would you like to buy new tools or cut grass? (Type 'buy/cut' to choose or 'quit' to leave the app) ")
    if user_input == 'quit':
        print('You have quit the app')
        break
    else:
        userChoice(user_input)

if money >= 1000 and hireTeam.own == True:
    print('You won!')