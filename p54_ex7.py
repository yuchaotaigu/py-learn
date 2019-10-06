def computegrade(inp_s):
    try:
        score = float(inp_s)
        if score >=0 and score <= 1:
            if score >= 0.9:
                print('A')
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            else:
                print('F')
        else:
            print('Bad score')
    except:
        print('Bad score')

inp_s = input('Enter score:')
computegrade(inp_s)
