
print("\t\t\t\t\t\tWELCOME TO MY CALL CENTER")



def cardpin():
    card = input("INPUT YOUR CARD:\t")
    cardcheck(card)


def simcenter():
    simrecharge = 1000
    callmade = 300
    balance = simrecharge - callmade
    return balance

def cardcheck(a):

    if len(a) == 7:
        card200 = a.count("0")
        card500 = a.count('1')
        card1000 = a.count('8')
        if card200 == 4:
            print(f'{"YOUR RECHARGE OF 200 NAIRA WAS SUCCESSFUL, YOUR ACCOUNT BALANCE IS"} {simcenter() + 200} {"NAIRA"}')

        elif card500 == 4:
            print(f'{"YOUR RECHARGE OF 500 NAIRA WAS SUCCESSFUL, YOUR ACCOUNT BALANCE IS"} {simcenter() + 500} {"NAIRA"}')
        elif card1000 == 4:
            print(f'{"YOUR RECHARGE OF 1000 NAIRA WAS SUCCESSFUL, YOUR ACCOUNT BALANCE IS"} {simcenter() + 1000} {"NAIRA"}')
        else:
            lessThan7()

    else:
       lessThan7()

import secrets
import datetime
import time
x = datetime.datetime.now()

def lessThan7():
    customerCare = ["08133179788", "081771836985", "08199787098"]
    print(f'{"YOU ENTERED SOMETHING INCORRECT, YOUR LINE HAS BEEN BANNED FOR 4HRS"}')
    print(x.strftime("%X"))
    carenumber = secrets.choice(customerCare)
    print(f'{"PLEASE CALL OUR CUSTOMER CARE LINE ON:-"} {carenumber}')





cardpin()
