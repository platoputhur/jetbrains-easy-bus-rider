def range_sum(numbers, start, end):
    # ...
    numbers = [int(n) for n in numbers]
    sorted_num = sorted(numbers)
    sum_of_numbers = 0
    for item in sorted_num:
        if int(start) <= item <= int(end):
            sum_of_numbers += item
    return sum_of_numbers


input_numbers = input().split(" ")
a, b = input().split(" ")
print(range_sum(input_numbers, a, b))
