def winsAndLoses (wins,loses):
    if wins - loses < 10:
        return "iron"
    elif wins - loses >= 11 and wins-loses <= 20:
        return "Bronze"
    elif wins - loses >= 21 and wins - loses <=50:
        return "Silver"
    elif wins - loses >= 51 and wins - loses <= 80:
        return "Gold"
    elif wins - loses >= 81 and wins - loses <= 90:
        return "Diamond"
    elif wins - loses >= 91 and wins - loses <= 100:
        return "Legendary"
    elif wins - loses >= 101:
        return "Immortal"
    else:
        return "Value Invalid"



wins = int(input("write your number of wins:"))
loses = int(input("write your number of loses:"))

print("")

print(f"the hero has a balance of {wins} and is at the level of {winsAndLoses(wins,loses)}")