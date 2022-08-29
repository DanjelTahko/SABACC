class Player:

    def __init__(self) -> None:
        
        self.credits = 500
        self.cards = []
        self.rounds = 0
        self.card_values = -4

    def get_cards_value(self):
        # Returns value of all cards in hand
        value = 0
        for card in self.player_cards:
            value += card.value
        return value
