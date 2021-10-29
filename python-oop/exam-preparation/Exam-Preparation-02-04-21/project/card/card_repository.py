from project.card.card import Card


class CardRepository:
    def __init__(self) -> None:
        self.count = 0
        self.cards = []
    
    def add(self, card: Card):
        for c in self.cards:
            if c.name == card.name:
                raise ValueError(f'Card {card.name} already exists!')
        
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError('Card cannot be an empty string!')
        
        c = [c for c in self.cards if c.name == card]
        if c:
            card_to_remove = c[0]
            self.cards.remove(card_to_remove)
            self.count -= 1

    def find(self, name: str):
        c = [c for c in self.cards if c.name == name]
        if c:
            found_card = c[0]

            return found_card
    