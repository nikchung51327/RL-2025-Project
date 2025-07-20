# Exercise 1
s = "Batman's real name is Bruce Wayne"
print(len(s))

# Exercise 2
print(s.endswith('Wayne'))

# Exercise 3
print(f'The string s has a length of {len(s)} items')

# Exercise 4
print(s.count('e'))

# Exercise 5
string1 = '33Ø12'
string2 = string1.replace('Ø', 'Y')
print(f'The string {string1} was replaced by {string2}')

# Exercise 6
dummy_string = 'Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups.'
if len(dummy_string) > 100:
    print('String has more than 100 characters')
else:
    print('String has less than or exactly 100 characters')

#Exercise 7
num_space = dummy_string.count(' ')
print(num_space)

# Exercise 8
letter1 = 'a'
letter2 = 's'

num_1 = dummy_string.count(letter1)
num_2 = dummy_string.count(letter2)

if num_1 > num_2:
    print(f'There are more {letter1}\'s than {letter2}\'s')
elif num_1 < num_2:
    print(f'There are more {letter2}\'s than {letter1}\'s')
else:
    print(f'There are exactly the same number of {letter1}\'s and {letter2}\'s')