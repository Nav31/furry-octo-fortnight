# https://www.codewars.com/kata/vasya-clerk/train/python

def tickets(people):
    ticket_cost = 25
    cash_register = {100: 0, 50: 0, 25: 0}
    for note in people:
        # check to see if you can make change based off note given
        change_due = note - ticket_cost
        if change_due == 75:
            if cash_register[50] <= 1:
                if cash_register[25] < 3:
                    return "NO"
            else:
                cash_register[50]

        # if yes add note to cash_register
        # else return no
    return "YES"