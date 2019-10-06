def computepay(hours, rate):
    if hours <= 40:
        pay = hours*rate
    else:
        pay = 40*rate + (hours-40)*1.5*rate

    return pay

inp_h = input('Enter hours: ')
try:
    hours = float(inp_h)
except:
    print('Error, please enter numeric input!')
    quit()
inp_r = input('Enter rate: ')
try:
    rate = float(inp_r)
except:
    print('Error, please enter numeric input!')
    quit()


pay = computepay(hours, rate)
print('Payment: ', pay)
