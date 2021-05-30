# number_2_words = {
#     '0': 'zero',
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine'
# }

# input_val = input('This is an amazing game, Please enter your keywords: ')
# new_val = ''
# for key in input_val:
#     new_val += number_2_words.get(key) + ' '
# print(new_val)

######
# advance usage
input_val = input('let your comment here: ')
word_group = input_val.split(' ')
emoji_map = {
    ':)': '😃',
    ':(': '🙁'
}
out_str = ''
for word in word_group:
    out_str += emoji_map.get(word, word) + ' '
print(out_str)
