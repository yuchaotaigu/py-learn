fruit = 'banana'

new_fruit = []
while not(new_fruit == '#'):
    new_fruit = input('Your fruit: ')

    if new_fruit < fruit:
        print('Your fruit '+new_fruit+' comes before '+fruit)
    elif new_fruit > fruit:
        print('Your fruit '+new_fruit+' comes after '+fruit)
