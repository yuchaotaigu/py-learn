str = 'X-DSPAM-Confidence:0.8475'

com_pos = str.find(':')
num_str = str[com_pos+1:]
num_float = float(num_str)

print(type(num_float))
print('The number is %g' % num_float)
