import random

players = 3
suites = ['hearts', 'spades', 'clubs', 'diamonds']
values = [2,3,4,5,6,7,8,9,10,'jack', 'queen', 'king', 'ace']
deck = [0]*52

def populateDeck():
  order = list(range(0,52))
  random.shuffle(order)
  i = 0
  for suite in suites:
    for value in values:
      deck[order[i]] = (value, suite)
      i+=1
  print(deck)

def startGame():
  print('Welcome to a blackjack table!')
  populateDeck()
  

startGame() 