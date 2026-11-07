import random
differentWays = []
day = True
surppasedAmmount = float(input("How much do you want to spend this week? (what is your budget)"))
foodItems = int(input("How many different types of ways do you spend your money (e.g., Food, Travel, etc.)? "))
ammountTotal = 0
for i in range(foodItems):
    typeOfWay = str(input("What type of way do you spend your money? tell me the "+ str(i) + "way you sepnd money"))
    differentWays.append(typeOfWay)

print("You spend your money in the following ways:")
for i in range(len(differentWays)):
    print(differentWays[i])
while day == True:
    for i in range(len(differentWays)):
        wayToSpend = int(input("Tell me the amount you have used on " + differentWays[i] + " today "))
        ammountTotal += wayToSpend
        # Provide budget feedback after each entry
        remaining = surppasedAmmount - ammountTotal
        if remaining < 0:
            print(f"You have surpassed your budget by {-remaining}.")
        elif remaining <= surppasedAmmount * 0.1:
            print(f"You are nearing the end of your budget. {remaining} left.")
        elif remaining >= surppasedAmmount * 0.5:
            print(f"You have plenty left to spend. {remaining} remaining.")
        else:
            print(f"You have {remaining} left for the week.")
    fullWeekComplete = str(input("Have you completed the week? yes or no"))
    if fullWeekComplete == "yes":
        
        if ammountTotal > surppasedAmmount:
            print("You have spent more than your budget this week. You have spent " + str(ammountTotal) + " and your budget was " + str(surppasedAmmount))
        elif ammountTotal < surppasedAmmount:
            print("You have spent less than your budget this week. You have spent " + str(ammountTotal) + " and your budget was " + str(surppasedAmmount))
        day = False
    elif fullWeekComplete == "no":
        
        if ammountTotal > surppasedAmmount:
            print("You have already spent more than your budget this week.Try limit your expenses today!")
        elif ammountTotal < surppasedAmmount:
            print("You have spent less than your budget this week. You have spent " + str(ammountTotal) + " and your budget was " + str(surppasedAmmount))  
        day = True