inp = input('Enter temperature in Fahrenheit:\n')
try:
    temp_f = float(inp)
    temp_c = (temp_f-32)/9*5
    print(temp_c)
except:
    print('Please enter a number!')
