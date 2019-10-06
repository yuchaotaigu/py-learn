sum = 0
ite = 0

while True:
    inp_n = input('Enter a number:')
    try:
        num = float(inp_n)
        sum = sum + num
        ite = ite + 1
    except:
        if inp_n == 'done':
            break
        else:
            print('Invalid input')
try:
    print(sum,ite,sum/ite)
except:
    print(sum,ite)
