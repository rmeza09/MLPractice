import random

def main():
    playGame()


def deal():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    draw  = ['', '']
    draw[1] = random.choice(suits)
    draw[0] = random.choice(value)
    return draw


def playGame():
    myHand = []
    house = []
    # begin cycle
    for i in range(2):
        myHand.append(deal())
        house.append(deal())
    print('My hand')
    print(myHand)
    print('Dealers hand')
    print(house)




main()
