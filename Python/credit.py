from cs50 import get_string


def main():
    # Get user input
    card = get_string("Number: ")

    # Check if input is numeric
    if card.isnumeric() == True:

        if len(card) == 15:
            if (card[0] == '3' and card[1] == '4') or (card[0] == '3' and card[1] == '7'):
                check(card)
                if check(card) == True:
                    print("AMEX")

        elif len(card) == 16:
            if card[0] == '4':
                check(card)
                if check(card) == True:
                    print("VISA")

            if card[0] == '5' and ('0' < card[1] < '6'):
                check(card)
                if check(card) == True:
                    print("MASTERCARD")

        elif len(card) == 13:
            if card[0] == '4':
                check(card)
                if check(card) == True:
                    print("VISA")

        else:
            print("INVALID")

# Check if card number is valid
# 1.Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
# 2.Add the sum to the sum of the digits that weren’t multiplied by 2.
# 3.If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!


def check(card):
    # Initialize a list
    cardnum = []
    for i in range(0, len(card), 1):
        cardnum.append(card[i])
    
    total1 = 0
    for i in range((len(cardnum) - 2), 0, 2):
        mult = cardnum[i] * 2
        if mult > 9:
            mult1 = mult % 10
            total1 += (1 + mult1)
        else:
            total1 += mult
    
    total2 = 0
    for i in range((len(cardnum) - 1), 0, 2):
        total2 += cardnum[i]
    
    total0 = total1 + total2
    
    if total0 % 10 == 0:
        return True
    else:
        return False


main()
