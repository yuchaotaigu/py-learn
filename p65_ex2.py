maxv = None
minv = None
ite = 0

while True:
    inp_n = input('Enter a number:')
    try:
        num = float(inp_n)
        if maxv == None or maxv < num:
            maxv = num

        if minv == None or minv > num:
            minv = num
        ite = ite + 1
    except:
        if inp_n == 'done':
            break
        else:
            print('Invalid input')

print(ite,maxv,minv)
