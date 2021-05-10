from time import sleep
import random


suits = ("Червей", "Пик", "Крестей", "Бубей")

ranks = ("Двойка", "Тройка", "Четверка", "Пятерка", "Шестерка", "Семерка",
         "Восьмерка", "Девятка", "Десятка", "Валет",
         "Дама", "Король", "Туз")

values = {"Двойка": 2, "Тройка": 3, "Четверка": 4, "Пятерка": 5,
          "Шестерка": 6, "Семерка": 7, "Восьмерка": 8, "Девятка": 9,
          "Десятка": 10, "Валет": 10, "Дама": 10, "Король": 10, "Туз": 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Туз":
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



game_on = True
test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
ai_player = Hand()

test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())

ai_player.add_card(test_deck.deal())
ai_player.add_card(test_deck.deal())

print()
print("У Вас ", end="")
for i in test_player.cards:
    print(i, end=", ")
test_player.adjust_for_aces()
print(f"Всего: {test_player.value}")

if test_player.value == 21:
    print("Blackjack! Игрок победил!")
    game_on = False

print("\nУ компьютера ", end="")

for i in ai_player.cards:
    print(i, end=", ")
print(f"Всего: {ai_player.value}")
if ai_player.value == 21:
    print("Blackjack! Компьютер победил!")
    game_on = False


while game_on:
    print()
    decision = input("Ещё? ").lower()

    if decision == "да":
        test_player.add_card(test_deck.deal())
        test_player.adjust_for_aces()
        print(test_player.cards[-1])
        print(f"Всего: {test_player.value}")
        if test_player.value > 21:
            print("Перебор! Компьютер выиграл ")
            game_on = False
            break

    elif decision == "нет":
        while game_on:
            if ai_player.value < test_player.value:
                ai_player.add_card(test_deck.deal())
                print("Компьютер добирает...")
                sleep(2)
                print(f"Компьютер вытянул {ai_player.cards[-1]}")
                print(f"Всего: {ai_player.value}")
                if ai_player.value > 21:
                    print("Перебор! Игрок выиграл!")
                    game_on = False
                    break
            elif ai_player.value == test_player.value:
                print("Ничья")
                game_on = False
                break
            else:
                print("Компьютер побеждает!")
                game_on = False
                break
    else:
        print("Ошибка ввода")
        break
