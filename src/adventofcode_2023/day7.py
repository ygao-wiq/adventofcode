import enum
import utils

class Card(enum.Enum):
    A=14
    K=13
    Q=12
    J=11
    Ten=10
    Nine=9
    Eight=8
    Seven=7
    Six=6
    Five=5
    Four=4
    Three=3
    Two=2

class Hand_Pattern(enum.Enum):
    Five_Kind = 7
    Four_Kind = 6
    Full_House = 5
    Three_Kind = 4
    Two_Pairs = 3
    One_Pair = 2
    High_Card = 1

def parse_card(card_value: str) -> Card:
    if card_value == "A":
        return Card.A
    elif card_value == "K":
        return Card.K
    elif card_value == "Q":
        return Card.Q
    elif card_value == "J":
        return Card.J
    elif card_value == "T":
        return Card.Ten
    elif card_value == "9":
        return Card.Nine
    elif card_value == "8":
        return Card.Eight
    elif card_value == "7":
        return Card.Seven
    elif card_value == "6":
        return Card.Six
    elif card_value == "5":
        return Card.Five
    elif card_value == "4":
        return Card.Four
    elif card_value == "3":
        return Card.Three
    elif card_value == "2":
        return Card.Two
        
class Hand:
    
    def __init__(self, cards: str, stake: int):
        self.cards = list()
        i = 0
        pattern_calc_map = dict()
        while i<len(cards):
            self.cards.append(parse_card(cards[i]))
            i += 1
            pattern_calc_map[self.cards[-1]] = pattern_calc_map.get(self.cards[-1], 0) + 1
        if len(pattern_calc_map) == 1:
            self.hand_pattern = Hand_Pattern.Five_Kind
        elif len(pattern_calc_map) == 2 and max(pattern_calc_map.values()) == 4:
            self.hand_pattern = Hand_Pattern.Four_Kind
        elif len(pattern_calc_map) == 2 and max(pattern_calc_map.values()) == 3 and min(pattern_calc_map.values()) == 2:
            self.hand_pattern = Hand_Pattern.Full_House
        elif len(pattern_calc_map) == 3 and max(pattern_calc_map.values()) == 3 and min(pattern_calc_map.values()) == 1:
            self.hand_pattern = Hand_Pattern.Three_Kind
        elif len(pattern_calc_map) == 3 and max(pattern_calc_map.values()) == 2 and min(pattern_calc_map.values()) == 1:
            self.hand_pattern = Hand_Pattern.Two_Pairs
        elif len(pattern_calc_map) == 4 and max(pattern_calc_map.values()) == 2 and min(pattern_calc_map.values()) == 1:
            self.hand_pattern = Hand_Pattern.One_Pair
        elif len(pattern_calc_map) == 5 and max(pattern_calc_map.values()) == 1 and min(pattern_calc_map.values()) == 1:
            self.hand_pattern = Hand_Pattern.High_Card
        tmp_stg_list = [hex(self.hand_pattern.value)[-1]]
        for c in self.cards:
            tmp_stg_list.append(hex(c.value)[-1])
        self.stake = stake
        self.hand_strength = "".join(tmp_stg_list)

class Hand_With_Joker:
    
    def __init__(self, cards: str, stake: int):
        self.cards = list()
        i = 0
        pattern_calc_map = dict()
        has_joker = 0
        self.hand_pattern = None
        while i<len(cards):
            self.cards.append(parse_card(cards[i]))
            i += 1
            if self.cards[-1] != Card.J:
                pattern_calc_map[self.cards[-1]] = pattern_calc_map.get(self.cards[-1], 0) + 1
            else:
                has_joker += 1
        original_pattern_calc_map = pattern_calc_map.copy()
        if cards == "JQ999":
            print(cards)
        for c in pattern_calc_map.keys():
            if c != Card.J:
                pattern_calc_map[c] = pattern_calc_map[c] + has_joker
        if has_joker == 5 or max(pattern_calc_map.values()) == 5:
            self.hand_pattern = Hand_Pattern.Five_Kind
        elif max(pattern_calc_map.values()) == 4:
            self.hand_pattern = Hand_Pattern.Four_Kind
        elif len(pattern_calc_map) == 2 and max(pattern_calc_map.values()) == 3:
            self.hand_pattern = Hand_Pattern.Full_House
        elif len(pattern_calc_map) == 3 and max(pattern_calc_map.values()) == 3:
            self.hand_pattern = Hand_Pattern.Three_Kind
        elif len(pattern_calc_map) == 3 and max(pattern_calc_map.values()) == 2:
            self.hand_pattern = Hand_Pattern.Two_Pairs  
        elif len(pattern_calc_map) == 4 and max(pattern_calc_map.values()) == 2:
            self.hand_pattern = Hand_Pattern.One_Pair
        elif max(pattern_calc_map.values()) == 1:
            self.hand_pattern = Hand_Pattern.High_Card
        tmp_stg_list = [hex(self.hand_pattern.value)[-1]]
        for c in self.cards:
            if c != Card.J:
                tmp_stg_list.append(hex(c.value)[-1])
            else:
                tmp_stg_list.append("1")
        self.stake = stake
        self.hand_strength = "".join(tmp_stg_list)

def solution_1():
    data_lines = utils.get_file_content("day7.dat")
    hands = list()
    for l in data_lines:
        hands.append(Hand(l.split(" ")[0], int(l.split(" ")[1])))
    hands = sorted(hands, key=lambda c: c.hand_strength)
    ret = 0
    for i, c in enumerate(hands):
        ret += (i+1)*c.stake
    print(ret)
    
def solution_2():
    data_lines = utils.get_file_content("day7.dat")
    hands = list()
    for l in data_lines:
        hands.append(Hand_With_Joker(l.split(" ")[0], int(l.split(" ")[1])))
    hands = sorted(hands, key=lambda c: c.hand_strength)
    ret = 0
    for i, c in enumerate(hands):
        ret += (i+1)*c.stake
    print(ret)

if __name__ == "__main__":
    solution_1()
    solution_2()
       