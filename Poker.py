
#  File: Poker.py

#  Description: program of traditional poker rules allowing players of size 2 - 6 to play against each other

#  Student's Name: Monish Jayakumar

#  Student's UT EID: mj27639

#  Partner's Name: Talah El-Zein

#  Partner's UT EID: the272

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/17

#  Date Last Modified: 9/20


import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.all_hands.append (hand)

  #def test(self, hand_type, hand_points):
   # for i in range (len(self.all_hands)):
    #  points, type = self.is_full_house(self.all_hands[i])
    #  hand_type.append(type)
    #  hand_points.append(points)

  # populates hand_type and hand_points array from player decks
  def getTypeandPoints(self, hand_type, hand_points):
    for i in range (len(self.all_hands)):
        points, type = 0, ""
        points, type = self.is_royal(self.all_hands[i])
        if points == 0 and type == "":
           points, type = self.is_straight_flush(self.all_hands[i])
           # print(points, type)
        if points == 0 and type == "":
            points, type = self.is_four_kind(self.all_hands[i])
            # print(points, type)
        if points == 0 and type == "":
            points, type = self.is_full_house(self.all_hands[i])
        if points == 0 and type == "":
            points, type = self.is_flush(self.all_hands[i])
        if points == 0 and type == "":
            points, type = self.is_straight(self.all_hands[i])
        if points == 0 and type == "":
            points, type = self.is_three_kind(self.all_hands[i])
        if points == 0 and type == "":
            points, type = self.is_two_pair(self.all_hands[i])
        if points == 0 and type == "":
            points, type = self.is_one_pair(self.all_hands[i])
        if points == 0 and type == "":
          points, type = self.is_high_card(self.all_hands[i])
        
        hand_type.append(type)
        hand_points.append(points)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand

    self.getTypeandPoints(hand_type, hand_points)
    # determine winner and print
    win_order = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 
    'Three of a Kind', 'Two Pair', 'One Pair', 'High Card']
    lst = []
    # finds numerical value of deck to be able to compare deck types
    for i in hand_type:
      type_of_deck = i
      ind = win_order.index(type_of_deck)
      lst.append(ind)

    winner = min(lst)
    ind = lst.index(winner)

    # if one winner then print winner
    if lst.count(winner) == 1:
      print("Player {} wins.".format(ind))
    
    # if there's a ties print ties
    else:
      for i in range(len(lst)):
        if lst[i] == winner:
          print("Player {} ties.".format(i))
  
  
    # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)   

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  # determines if hand is straight flush
  def is_straight_flush (self, hand):
    rank_order = True
    highest = hand[0].rank
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == highest - i)
    
    if (not rank_order):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    
    return points, 'Straight Flush'
  
  # determines if hand is four of a kind
  def is_four_kind (self, hand):
    equal_count = 0

    for i in range(1,len(hand)):
        card1 = hand[i - 1].rank
        card2 = hand[i].rank
        if (card1 == card2):
            equal_count += 1

    if equal_count != 3:
        return 0, ''
    
    # if highest card in deck is the side card, move card to the end of the hand
    hand2 = hand
    if hand[0].rank != hand[1].rank:
        temp = hand2[0]
        hand2[0] = hand2[4]
        hand2[4] = temp
    
    points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Four of a Kind"

  # determines if hand is full_house
  def is_full_house (self, hand):
    if hand[0] == hand[1] == hand[2] and hand[3] == hand[4]:
      points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

    elif hand[0] == hand[1] and hand[2] == hand[3] == hand[4]:
      points = 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 
      points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[1].rank)

    else:
      return 0, ''
  
    return points, "Full House"


  # determines if hand is flush
  def is_flush (self, hand):
    for i in range(1,len(hand)):
      if not hand[i].suit == hand[i - 1].suit:
        return 0, ""

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Flush'

  # determines if hand is straight
  def is_straight (self, hand):
    for i in range(1, len(hand)):
      if not hand[i - 1].rank == hand[i].rank + 1:
        return 0, ""

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'

  # determines if hand is three of a kind
  def is_three_kind (self, hand):
    isThreePair = False
    for i in range(len(hand)):
      count = 1
      lst = [0,1,2,3,4]
      lst.remove(i)
      ind = [i]
      for j in range(len(hand)):
        if hand[i] == hand[j] and i != j:
          count += 1
          ind.append(j)
          lst.remove(j)
      if count == 3:
        isThreePair = True
        break

    if not isThreePair:
      return 0, ""
    

    points = 4 * 15 ** 5 + (hand[ind[0]].rank) * 15 ** 4 + (hand[ind[1]].rank) * 15 ** 3
    points = points + (hand[ind[2]].rank) * 15 ** 2 + (hand[lst[0]].rank) * 15 ** 1
    points = points + (hand[lst[1]].rank)
      
    return points, 'Three of a Kind'

  # determines if hand is two pair
  def is_two_pair (self, hand):
    isTwoPair = False
    ind = []
    lst = [0,1,2,3,4]
    for i in range(len(hand)):
      for j in range(len(hand)):
        if hand[i].rank == hand[j].rank and i != j and i not in ind and j not in ind:
          ind.append(i)
          ind.append(j)
          lst.remove(i)
          lst.remove(j)
          if (len(ind) == 4):
            isTwoPair = True
            break
    
    if not isTwoPair:
      return 0, ""
   
    points = 3 * 15 ** 5 + (hand[ind[0]].rank) * 15 ** 4 + (hand[ind[1]].rank) * 15 ** 3
    points = points + (hand[ind[2]].rank) * 15 ** 2 + (hand[ind[3]].rank) * 15 ** 1
    points = points + (hand[lst[0]].rank)

    return points, 'Two Pair'
         
  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        pair = [i, i+1]
        one_pair = True
        break

    if (not one_pair):
      return 0, ''

    lst = [0,1,2,3,4]
    lst.remove(pair[0])
    lst.remove(pair[1])

    
    points = 2 * 15 ** 5 + (hand[pair[0]].rank) * 15 ** 4 + (hand[pair[1]].rank) * 15 ** 3
    points = points + (hand[lst[0]].rank) * 15 ** 2 + (hand[lst[1]].rank) * 15 ** 1
    points = points + (hand[lst[2]].rank)

    return points, 'One Pair'

  # determines if hand is high card
  def is_high_card (self,hand):
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'High Card'

    
def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int(line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()


