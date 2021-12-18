def last_indexof_max(numbers):
    # write the modified algorithm here
    max_num = 0
    max_index = -1
    for index, num in enumerate(numbers):
        if num >= max_num:
            max_num = num
            max_index = index
    return max_index
