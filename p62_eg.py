largest = None
print('Before: ',largest)

for iterv in [3, 41, 12, 9, 74, 15]:
    if largest == None or iterv > largest:
        largest = iterv
    print('Loop:', largest,iterv)

print('Largest:',largest)
