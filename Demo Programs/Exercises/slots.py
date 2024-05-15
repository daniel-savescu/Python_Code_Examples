import random

def spin():
    luckNumbersList = []
    for i in range(0,5):
        n = random.randint(1,5)
        luckNumbersList.append(n)
    return luckNumbersList


def checkForJackpot(jackpot, money, bet):
    all_same = all(val == jackpot[0] for val in jackpot[1:])
    if all_same:
        print("You win the Jackpot !")
        money = bet * 100
        print("Your current money is : ", money)
    else:
        money = money - bet  # Update money here
    print("Your current money is : ", money)
    return money  # Return the updated money



def checkForNormalWin(normalWin, money, bet):
    if normalWin[0] == normalWin[1] and normalWin[1] == normalWin[2] and normalWin[2] == normalWin[0]:
        print("You win the lucky three !")
        money = bet * 10
        print("Your current money is : ", money)
    else:
        money = money - bet  # Update money here
    print("Your current money is : ", money)
    return money  # Return the updated money


totalMoney = int(input("How much money you want to play : ?"))

while totalMoney >= 0:
    gameStatus = input("Do you want to play slots ? : [Y | N] : ")
    if gameStatus.lower() == 'y':
        userBet = int(input("Enter how much money you want to bet : ?"))
        luckyNumbers = spin()
        print(luckyNumbers)
        # Check for normal win first
        if all(val == luckyNumbers[0] for val in luckyNumbers):  # Check for all matching numbers
            totalMoney = checkForNormalWin(luckyNumbers, totalMoney, userBet)
        else:
            # Check for jackpot only if not normal win
            totalMoney = checkForJackpot(luckyNumbers, totalMoney, userBet)
    else:
        break
    








            





