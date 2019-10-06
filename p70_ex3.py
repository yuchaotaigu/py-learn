def count(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter = counter + 1

    return counter

word = []
letter = []
while not(letter == '#'):
    word = input('Please enter the word: ')
    letter = input('Please enter the letter: ')
    print(count(word, letter))
