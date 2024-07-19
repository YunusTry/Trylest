import random

class Blackjack:

    def __init__(self, num_players, starting_balance=1000):
        self.num_players = num_players
        self.starting_balance = starting_balance
        self.players = {input(f"Player {i + 1} name: "): {'balance': self.starting_balance, 'bet': 0} for i in range(self.num_players)}
        self.reset()

    def reset(self):
        self.deck = self.create_deck()
        self.dealer_hand = []
        self.player_hands = {player: [] for player in self.players}  

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck_cards = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck_cards)
        return deck_cards

    def deal_cards(self):
        for _ in range(2):  
            for player in self.players:
                card = self.deck.pop()
                self.player_hands[player].append(card)

        for _ in range(2):
            card = self.deck.pop()
            self.dealer_hand.append(card)

    def hand_value(self, hand):
        value = 0
        ace_count = 0

        for card in hand:
            rank = card['rank']
            if rank.isdigit():
                value += int(rank)
            elif rank in ['Jack', 'Queen', 'King']:
                value += 10
            else:
                value += 11
                ace_count += 1

        while ace_count > 0 and value > 21:
            value -= 10
            ace_count -= 1

        return value

    def same_cards(self, hand):
        return hand[0]['rank'] == hand[1]['rank']

    def bet_control(self, player, player_balances):
        while True:
            try:
                bet = int(input(f"{player}'s Bet Amount (Current Balance: {player_balances[player]}): "))
                if 0 < bet <= player_balances[player]:
                    return bet
                else:
                    print("Invalid bet amount. Please enter a bet greater than 0 and not exceeding your current balance.")
            except ValueError:
                print("Please enter a valid number.")

    def play_round(self):
        player_balances = {player: self.players[player]['balance'] for player in self.players}

        while True:
            self.reset()  
            self.deal_cards()

            for player in self.players:
                bet = self.bet_control(player, player_balances)
                self.players[player]['bet'] = bet

            print(f"Dealer's First Card: {self.dealer_hand[0]['rank']} {self.dealer_hand[0]['suit']}")

            for player in self.players:
                print(f"\n{player}'s Cards:")
                for card in self.player_hands[player]:
                    print(f"{card['rank']} {card['suit']}")

                if self.same_cards(self.player_hands[player]):
                    choice = input(f"{player}, you have the same cards. Would you like to open a separate game? (y/n): ").lower()
                    if choice == 'y':
                        self.open_separate_game(player)

                while True:
                    total_value = self.hand_value(self.player_hands[player])
                    print(f"Total Value: {total_value}")

                    if total_value == 21:
                        print(f"{player} got Blackjack!")
                        break
                    elif total_value > 21:
                        print(f"{player} Busted!")
                        player_balances[player] -= self.players[player]['bet']
                        break

                    choice = input(f"{player}, do you want to draw another card? (y/n): ").lower()
                    if choice == 'y':
                        card = self.deck.pop()
                        self.player_hands[player].append(card)
                        print(f"{player} drew {card['rank']} {card['suit']}.")
                    else:
                        break

            while self.hand_value(self.dealer_hand) < 17:
                card = self.deck.pop()
                self.dealer_hand.append(card)

            self.determine_results(player_balances)

            for player in self.players:
                player_balances[player] = self.players[player]['balance']

            play_again = input("Do you want to play another game? (y/n): ").lower()
            if play_again != 'y':
                break

    def open_separate_game(self, player):
        print(f"{player}, opening a separate game!")

        new_game = [self.player_hands[player].pop(), self.deck.pop()]
        self.player_hands[player].append(self.deck.pop())
        new_game_value = self.hand_value(new_game)

        print(f"\nNew Game Cards:")
        for card in new_game:
            print(f" {card['suit']} {card['rank']}")

        while True:
            print(f"Total Value: {new_game_value}")

            if new_game_value == 21:
                print(f"{player} got Blackjack!")
                break
            elif new_game_value > 21:
                print(f"{player} Busted!")
                break

            choice = input(f"{player}, do you want to draw another card? (y/n): ").lower()
            if choice == 'y':
                card = self.deck.pop()
                new_game.append(card)
                print(f"{player} drew {card['rank']} {card['suit']}.")
                new_game_value = self.hand_value(new_game)
            else:
                break

        if new_game_value <= 21:
            dealer_value = self.hand_value(self.dealer_hand)
            print(f"\nDealer's Second Card: {self.dealer_hand[1]['rank']} {self.dealer_hand[1]['suit']}")
            print(f"New Game Total Value: {new_game_value}")
            while dealer_value < 17:
                card = self.deck.pop()
                self.dealer_hand.append(card)
                dealer_value = self.hand_value(self.dealer_hand)

            self.determine_separate_game_results(new_game_value, dealer_value, player)
        else:
            print(f"{player}, separate game lost!")

    def determine_separate_game_results(self, player_value, dealer_value, player):
        print(f"\nSeparate Game Results:")
        print(f"{player}'s Total Value: {player_value}")
        print(f"Dealer's Total Value: {dealer_value}")

        if player_value > dealer_value or dealer_value > 21:
            print(f"{player} won the separate game!")
            self.players[player]['balance'] += self.players[player]['bet']
        elif player_value == dealer_value:
            print(f"{player} It's a tie!")
        else:
            print(f"{player} lost the separate game!")
            self.players[player]['balance'] -= self.players[player]['bet']

        print(f"{player}'s Updated Balance: {self.players[player]['balance']}")

    def determine_results(self, player_balances):
        for player in self.players:
            total_value = self.hand_value(self.player_hands[player])
            print(f"\n{player}'s Total Value: {total_value}")

            if total_value > 21:
                print(f"{player} Busted!")
                self.players[player]['balance'] -= self.players[player]['bet']
            else:
                dealer_value = self.hand_value(self.dealer_hand)
                print(f"Dealer's Total Value: {dealer_value}")

                if dealer_value > 21 or total_value > dealer_value:
                    print(f"{player} won!")
                    winnings = self.players[player]['bet'] 
                    self.players[player]['balance'] += winnings
                    print(f"{player} won {winnings} units!")
                elif total_value == dealer_value:
                    print(f"{player} It's a tie!")
                else:
                    print(f"{player} lost!")
                    self.players[player]['balance'] -= self.players[player]['bet']

            print(f"{player}'s Updated Balance: {self.players[player]['balance']}")

# Start the game
while True:
    try:
        num_players = int(input("Hello! How many players do you want to play with?: "))
        if num_players > 0:
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

game = Blackjack(num_players)
game.play_round()

play_again = input("Do you want to play another game? (y/n): ").lower()
if play_again != 'y':
    print("You closed the game. Have a nice day!")
