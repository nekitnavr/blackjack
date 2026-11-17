import random

players = 0
hands = []
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
  # print(deck)

def choosePlayers(playerCount = None):
  global players
  if 2 <= playerCount <= 6:
    players = playerCount
    return
  else:
    print('Enter a valid player count to override')

  while players < 2 or players > 6:
      players = int(input('How many players do you want (2 to 6): '))

def populateHands():
  global hands, deck, players
  print(players)
  for i in range(players):
    hands.append([])
    hands[i].append(deck.pop())
  for i in range(players):
    hands[i].append(deck.pop())
  # print(hands)

def deal():
  print('Dealing starts!')
  print(f'Your cards are: {hands[0][0][0]} of {hands[0][0][1]} and {hands[0][1][0]} of {hands[0][1][1]}.')
  print(f'Dealer\'s first card is: {hands[players-1][0][0]} of {hands[players-1][0][1]}.')

def play():
  print('Play')

def startGame():
  print('Welcome to a blackjack table!')
  populateDeck()
  choosePlayers(8)
  populateHands()
  deal()
  play()
  

startGame() 