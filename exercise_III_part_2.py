hours = input('Enter Hours:')
rate = input('Enter Rate:')
try:
    pay = int(hours)*int(rate)
    print('Payment received: ',pay)
except:
    print('Error, please enter numeric input')