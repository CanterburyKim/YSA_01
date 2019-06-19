my_list_of_bits = [
0b_1111_1111,
0b_1000_1111,
0b_1000_1111,
0b_1000_1111,
0b_1000_1111,
0b_1000_1111,
0b_1000_1111,
0b_1111_1111
]

for row in my_list_of_bits:
    row_as_string = f'{row:08b}'
    for bit in row_as_string:
        if bit == '1':
            print('#', end='')
        else:
            print(' ', end='')
    print()
