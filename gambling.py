import random as rand

SYMBOLS = ["💛", "💥", "❌", "⚜", "🟢", "💲"]
NUMBER_OF_SYMBOLS = 5

print("\n"*5, "Welcome to the slot marchine!", SYMBOLS)



def play():
    bank = 500
    bet = 0
    multiplier = 0
    while bank > 0:
        bet = get_bet(bank)
        bank -= bet
        random_symbols = generate_random_symbols()
        print_symbols(random_symbols)
        max_count = calculate_winnings(random_symbols)
        multiplier = get_multiplier(max_count)
        winning = bet * multiplier
        bank += winning
        print("Du har", bank,"dollar")
        play_again = input("Play again? (y/n) -> ")
        if play_again == "y" or play_again == "Y":
            continue
        else:
            break

def get_bet(bank):
    print("du har", bank,"dollar i banken")
    bet = int(input("Hur mycket pengar vill du satsa? "))
    return bet

def play_again():
    '''
    This function asks the user if play should continue. Returns True if the player 
    wants to play again and False otherwise.
    '''
    play_again_user_input = input("Play again? (y/n) -> ")
    play_again_bool = (play_again_user_input ==
                       "y" or play_again_user_input == "Y")
    return play_again_bool


def generate_random_symbols():
    return rand.choices(SYMBOLS, k=5)


def calculate_winnings(random_symbols: list):
    max_count = 0
    for sym in random_symbols:
        c = random_symbols.count(sym)
        if c > max_count:
            max_count = c
    return max_count
  

def get_multiplier(max_count):
    if max_count == 2:
        return 0.5
    elif max_count == 3:
        return 2
    elif max_count == 4:
        return 4
    elif max_count == 5:
        return 10
    else:
        return 0

def print_symbols(list_of_symbols):

    print(list_of_symbols)


play()
