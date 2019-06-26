my_list_of_bits = [
# 0b_0000_0000,
# 0b_0000_0000,
# 0b_0010_0100,
# 0b_0000_0000,
# 0b_0100_0010,
# 0b_0011_1100,
# 0b_0000_0000,
# 0b_0000_0000
0b_0000_0000,
0b_0110_0110,
0b_1111_1111,
0b_0111_1110,
0b_0011_1100,
0b_0001_1000,
0b_0000_0000,
0b_0000_0000
]

for row in my_list_of_bits:
    row_as_string = f'{row:08b}'
    print( row)
    # for bit in row_as_string:
    #     if bit == '1':
    #         print('#', end='')
    #     else:
    #         print(' ', end='')
    # print()
