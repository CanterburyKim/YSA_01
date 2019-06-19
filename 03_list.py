# Part 1 A Sentence
my_sentence = 'You only live once, but if you do it right, once is enough'
print(my_sentence[0])

# Part 2 Slicing the sentence
print(my_sentence[0:5])
print(my_sentence[5:10])
print(my_sentence[:3])
print(my_sentence[:-3])
print(my_sentence[-6:])
print(my_sentence[::2])
print(my_sentence[::3])
print(my_sentence[::-1])


# Part 3 List of numbers
my_list_of_numbers = [1,3,7,201,-1, 99, 0b_0110_0111, 13]

print(f'{my_list_of_numbers[0]}')
print(f'{my_list_of_numbers[1]}')
print(f'{my_list_of_numbers[2]}')
print(f'{my_list_of_numbers[-1]}')

# Part 4 List of names
my_list_of_names = ['Shuri', 'Okoye', 'T\'Chaka', 'T\'Challa',
    'Xoliswa']

print(my_list_of_names[0])
print(my_list_of_names[2])

# List of List of names
print(f'{my_list_of_names[0][0]}')
print(f'{my_list_of_names[0][1]}')
print(f'{my_list_of_names[0][::2]}')
