from currency_converter import CurrencyConverter

def get_money_interval(lvl_sel):
    c = CurrencyConverter()
    usd_value = c.convert(lvl_sel, "USD", "ILS")
    interval = (usd_value - (5 - lvl_sel), usd_value + (5 - lvl_sel))
    return interval


def get_guess_from_user(lvl_sel):
    return float(input('''Enter your guess for the value of USD in ILS 
    for the next mathematical calculation:
    (USD Value - (5 - Selected Difficulty), USD Value + (5 - Selected Difficulty)):  '''))


def play(lvl_sel):
    random_money = get_money_interval(lvl_sel)
    money_from_user = float(get_guess_from_user(lvl_sel))

    if random_money[0] <= money_from_user <= random_money[1]:
        print("You won!")
        return True
    else:
        print(f'The value was between {random_money[0]} and {random_money[1]}')
        print("You lost.")
        return False
