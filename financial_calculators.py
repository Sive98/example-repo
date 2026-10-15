import math


Calculator_needed =  input("What would you like to Calculate:").lower() # Check what the user wants to calculate

#This is an investment calculator
if Calculator_needed =="investment":# This will take all the neccesary imputs

    deposit = round(float(input("How much will you deposit: R")),2) 
    interest_rate = float(input("At what rate? (%):")) 
    Period = int(input("For How long will you invest your money(Years) :"))
    interest = input("Will you opt for simple or compound interest: ").lower()

    if interest == "compound":
        a = round(deposit*math.pow((1 + (interest_rate/100)), Period),2)
    elif interest == "Simple":
        a = round(deposit* (1 + ((interest_rate/100)*Period)),2)
    print("In {} years time your invest will be R{}".format(Period, a))


#This is a bond calculator

elif Calculator_needed == "bond":
    P_Value = float(input("How much is the house you want to buy?: R"))
    annual_interest = float(input("Enter the annual interest rate (%): "))
    months = int(input("How many months are you planning to repay the loan?: "))

    repayment = ((annual_interest / 1200) * P_Value) / (1 - math.pow((1 + (annual_interest / 1200)), -months))

    print("Your monthly repayment will be: R{:.2f}".format(repayment))
else:
    print("Oops! Check your option and try again.")