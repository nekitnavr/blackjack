# Blackjack
# Milestone 2: Design
1. Pseudocode:
`First outputs a card For Player 1
Asks the user if they want to deal another card
If the P1 says yes, then the code will deal another
card and display the sum of what the cards are, how
far away they are from reaching 21.
Next, it is P2’s turn and the same will be applied to
them.
The rounds will keep on continuing until a player’s
sum hits or surpasses 21.
In each turn, the player can type in “hint” or “Hint”
before they choose to deal another card
The hint shows the probability of the next card
causing the sum to hit 21 by analyzing the rest of the
cards left in the deck.
Then it prompts the question again “Draw another
card?”
The players turn switch alternatively.`

3. Function Breakdown
- getNewCard() = outputs and removes a random card from the list Cards.
- getSum(int counter) = returns the sum of all the cards the players dealt and how
far away they are from 21.
- getHint() = returns the probability of the next card increasing the sum to 21

4. Program Data
The program will contain a list called Deck that contains all 52 cards (no jokers).
It will calculate the sum of all the cards the players dealt by having the function
getSum()’s parameter by getNewCard().

5. Test Examples
    1. Starting the game  
      Input: Start  
      Output: Player 1 draws the 7 of Hearts.  
    2. Player 1 draws another card  
      Input: Yes  
      Output: Player 1 draws the 5 of Spades. Total: 12. Points away from 21: 9.  
    3. Player chooses not to draw  
      Input: No  
      Output: Player 1 ends their turn. It is now Player 2's turn.  
    4. Player requests a hint  
      Input: hint  
      Output: There is a 25% chance that your next card will cause you to reach or  
      exceed 21.
    5. Calculating the sum of multiple cards   
      Input: Player has a 4, 6, and 3.  
      Output: Your total is 13. You are 8 points away from 21.  

6. Use of Ai and Other Resources
a. After placing our pseudocode in Google Gemini, we asked it to point out any gaps
in our plan. It suggested that we should emphasize more on the game-ending
conditions like what happens by the time the deck is completely depleted and both
players still haven't reached 21. Thus, we will also implement a rule in our game
that the player with the sum closest to 21 will win if both player’s sums haven’t
surpassed 21.
