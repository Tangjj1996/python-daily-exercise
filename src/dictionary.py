number_2_words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

input_val = input('This is an amazing game, Please enter your keywords: ')
new_val = ''
for key in input_val:
    new_val += number_2_words.get(key) + ' '
print(new_val)
