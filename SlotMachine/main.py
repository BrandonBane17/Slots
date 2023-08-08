import random

MAX_BET = 1000
MAX_LINES = 5
MIN_BET = 1

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and 5.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet must be greater than 0.")
        else:
            print("Please enter a number.")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough money to make that bet. Please try again.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}")

main()