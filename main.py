import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 200

ROWS = 3
COLS = 3


symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8

}

def get_slot_machine_count(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols:
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    colums = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]

        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            column.append(value)

        colums.append(column)
    return colums

def print_slot_machine(colums):
    for row in range(len(colums[0])):
        for i, colum in  enumerate(colums):
            if i != len(colums) - 1:
                print(f"{colum[row]} | ")
            else:
                print(f"{colum[row]}")



def deposit():
    while True:
        amount = input("Enter the amount to Deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be Greater than 0")
        else:
            print("Please Enter a Number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}) ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Vaild Number of Lines")
        else:
            print("Please Enter a Number.")

    return lines

def get_bet_amount():
    while True:
        betamount = input("What would you like to get Bet on Each line? $")
        if betamount.isdigit():
            betamount = int(betamount)
            if MIN_BET <= betamount <= MAX_BET:
                break
            else:
                print(f"Bet Amount must be Between {MIN_BET} - {MAX_BET}")
        else:
            print("Please Enter a Number.")

    return betamount
    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:

        bet = get_bet_amount()
        total = lines * bet

        if total > balance:
            print(f"You don't have enough amount to Bet, Your current Balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total Bet is Equal to: ${total}")

    # print(balance, lines)



main()