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
            if lines > 0 and lines <= 5:
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
            if bet > 0:
                break
            else:
                print("Bet must be greater than 0.")
        else:
            print("Please enter a number.")
    return bet

