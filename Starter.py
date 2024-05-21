numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]

max_num = max(numsList)
max_index = numsList.index(max_num)

min_num = min(numsList)
min_index = numsList.index(min_num)

average = sum(numsList) / len(numsList)

print(f"The biggest number is {max_num} at position {max_index}.")
print(f"The smallest number is {min_num} at position {min_index}.")
print(f"The average of all numbers is {average}.")