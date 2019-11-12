# FIND SUM OF LIST

list_nums = [1, 4, 6, 7, 9, 10, 14]
list_sum = list_nums[0] + list_nums[1] + list_nums[2] + list_nums[3] + list_nums[4] + list_nums[5] + list_nums[6]
print(list_sum)

# FIND LARGEST NUMBER IN LIST

# list_nums = [1, 4, 6, 7, 9, 10, 14]
def max_num_in_list(list_to_large):
    max = list_nums[0]
    for num_large in list_to_large:
        if num_large > max:
            max = num_large
    return max
print(max_num_in_list(list_nums))

# FIND SMALLEST NUMBER IN LIST

# list_nums = [1, 4, 6, 7, 9, 10, 14]
def min_num_in_list(list_to_small):
    min = list_nums[0]
    for num_small in list_to_small:
        if num_small < min:
            min = num_small
    return min
print(min_num_in_list(list_nums))

# FIND EVEN NUMBERS

# list_nums = [1, 4, 6, 7, 9, 10, 14]
def even_nums(list_to_check):
    even = []
    for num_even in list_to_check:
        if num_even % 2 == 0:
            even.append(num_even)
    return even
print(even_nums(list_nums))        

# MULTIPLY A LIST

list_nums_new = [2, 5, 7, 8, 10, 11, 15]
my_multi_list = []
fact_or = 5
for new_num in list_nums_new:
    my_multi_list.append(new_num * fact_or)
print(my_multi_list)

# MULTIPLY VECTORS

vect_list_1 = [2, 4, 5]
vect_list_2 = [2, 3, 6]
for vect_num in vect_list_1:
    a = (vect_list_1[0] * vect_list_2[0])
    b = (vect_list_1[1] * vect_list_2[1])
    c  = (vect_list_1[2] * vect_list_2[2])
new_vect_list = [a, b, c]
print(new_vect_list)



# USING IMPORT MUL
# from operator import mul
# vect_list_1 = [2, 4, 5]
# vect_list_2 = [2, 3, 5]
# multi = [*map(mul, vect_list_1, vect_list_2)]
# print(multi)

# MATRIC ADDITION

m1 = [
    [1, 3, ],
    [2, 4]
]

m2 = [
    [5, 2, 7],
    [1, 0]
]
result = [
    # [m1[0][0] + m2[0][0], m1[0][1] + m2[0][1]],
    # [m1[1][0] + m2[1][0], m1[1][0] + m2[1][1]]
    # [0, 0],
    # [0, 0]
]
for row_num in range(len(m1)):
    row = m1[row_num]
    result_row = []
    for column_num in range(len(row)):
        print(f"{row_num} {column_num}")
        print(f"I want to add {m1[row_num][column_num]} to {m2[row_num][column_num]}")
        # result[row_num][column_num] = m1[row_num][column_num] + m2[row_num][column_num]
        result_row.append(m1[row_num][column_num] + m2[row_num][column_num])
    result.append(result_row)
print(result)