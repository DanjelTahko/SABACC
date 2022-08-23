from card import Card
from settings import *
from debug import debug

class Calculate:

    def __init__(self, player_hand) -> None:
        self.player_hand = player_hand
        self.values_hand = [] # cards with real value (negative & positive)
        self.number_hand = [] # cards with ABS value (always positive)
        self.is_zero = False
        self.score_name = None
        self.score = None

    def count_pairs(self):

        search_count = []
        for index in range(len(self.number_hand)):
            counted = self.number_hand.count(self.number_hand[index])
            search_count.append(counted)

        # Banthas Wild - Zero with three of a kind
        if (search_count.count(3) == 3):
            self.score_name = "BANTHAS WILD"
            self.score = WINNING_HANDS[self.score_name]

        # Rule of Two - Zero with two pairs
        elif (search_count.count(2) == 4):
            self.score_name = "RULE OF TWO"
            self.score = WINNING_HANDS[self.score_name]

        # Sabacc - Zero with one pairs
        elif (search_count.count(2) == 2):
            self.score_name = "SABACC"
            self.score = WINNING_HANDS[self.score_name]
        
        # Zero with most cards
        else:
            self.score_name = "ZERO"
            self.score = WINNING_HANDS[self.score_name]

    def get_zero(self):
        
        total_value = 0
        # Adds every card in new array, ex [-2, 2, 0]
        for card in self.player_hand:
            self.number_hand.append(card.number)
            card_value = card.value
            total_value += card_value
            self.values_hand.append(card_value)

        self.values_hand.sort()
        self.number_hand.sort()
        self.score = total_value

        if (total_value == 0):
            self.is_zero = True

    def get_points(self):
        
        # 2 Cards in hand
        if (len(self.values_hand) == 2):

            # Pure Sabacc
            if (self.values_hand.count(0) == 2):

                self.score_name = "PURE SABACC"
                self.score = WINNING_HANDS[self.score_name]
                
            # Sabacc
            else:

                self.score_name = "SABACC"
                self.score = WINNING_HANDS[self.score_name]
        
        # 5 Cards in hand
        elif (len(self.values_hand) == 5):
            # Full Sabacc
            if (self.number_hand.count(10) == 4):

                self.score_name = "FULL SABACC"
                self.score = WINNING_HANDS[self.score_name]

            # Fleet
            elif (self.number_hand.count(self.number_hand[-1] == 4)):

                self.score_name = "FLEET"
                self.score = WINNING_HANDS[self.score_name]

            # Rhylet
            elif (self.number_hand.count(self.number_hand[0]) == 3 and
                  self.number_hand.count(self.number_hand[-1]) == 2):

                self.score_name = "RHYLET"
                self.score = WINNING_HANDS[self.score_name]

            # Gee Whiz - Zero with 1-4 & 10
            elif (self.number_hand[0] == 1 and 
                  self.number_hand[1] == 2 and
                  self.number_hand[2] == 3 and
                  self.number_hand[3] == 4 and 
                  self.number_hand[4] == 10):

                self.score_name = "GEE WHIZ"
                self.score = WINNING_HANDS[self.score_name]

            else:
                self.count_pairs()

        # 4 Cards
        elif (len(self.values_hand) == 4):
            
            # Squadron - Zero with four of a kind
            if (self.number_hand.count(self.number_hand[0]) == 4):
                self.score_name = "SQUADRON"
                self.score = WINNING_HANDS[self.score_name]

            # STRAIGHT KHYRON - Zero with run of four
            elif ((self.number_hand[0] == 7 and
                  self.number_hand[1] == 8 and
                  self.number_hand[2] == 9 and
                  self.number_hand[3] == 10) or
                  (self.number_hand[0] == 2 and
                  self.number_hand[1] == 3 and
                  self.number_hand[2] == 4 and
                  self.number_hand[3] == 5)):

                  self.score_name = "STRAIGHT KHYRON"
                  self.score = WINNING_HANDS[self.score_name]

            else:
                self.count_pairs()

        # 3 Cards
        elif (len(self.values_hand) == 3):

            if(self.number_hand[0] == 0):
                self.score_name = "YEE-HAA"
                self.score = WINNING_HANDS[self.score_name]

            else:
                self.count_pairs()


    def run(self):
        self.get_zero()
        if (self.is_zero):
            self.get_points()
        else:
            self.score_name = 'NULRHEK'
            self.score = int(f"-{abs(self.score)}")

        print(f"{self.score_name} : {self.score}\n{self.number_hand}")
    
        return self.score

"""
card1 = Card(5, "square", "positive")
card2 = Card(5, "square", "negative")
card3 = Card(3, "square", "positive")
card4 = Card(3, "square", "positive")
card5 = Card(6, "square", "negative")
test_array = [card1, card2, card3, card4, card5]

calc = Calculate(test_array)
calc.run()
"""

