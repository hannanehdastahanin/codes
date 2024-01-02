def normalize_list(input_list):
    mean_value = sum(input_list) / len(input_list)
    max_value = max(input_list)
    min_value = min(input_list)
    normalized_list = [(x - mean_value) / (max_value - min_value) for x in input_list]
    return normalized_list
n = int(input(" "))
lists = []
for _ in range(n):
    numbers_str = input().split(',')
    numbers = [float(num) for num in numbers_str]
    lists.append(numbers)
normalized_lists = [normalize_list(lst) for lst in lists]
for normalized_lst in normalized_lists:
    formatted_numbers = ["{:.2f}".format(num) for num in normalized_lst]
    print(" ".join(formatted_numbers))
