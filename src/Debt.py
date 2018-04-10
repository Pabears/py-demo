"""
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def pay1(balance,annualInterestRate,monthlyPaymentRate):
    for i in range(1, 13):
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        # print('Month', i, 'Remaining balance:', round(updatedBalanceEachMonth,2))
        balance = updatedBalanceEachMonth

    print('Remaining balance:', round(balance, 2))

def pay2():
    rate=(annualInterestRate/12+1)**12
    print(rate)

    updatedBalanceEachMonth = balance*rate/12
    print('Lowest Payment:', round(updatedBalanceEachMonth, 2))

pay1(balance,annualInterestRate,monthlyPaymentRate)
balance = 3329
annualInterestRate = 0.2
pay2()

