def divide_array(array):
    n = len(array)
    half = n // 2
    combinations_set = set()
 
    for indices in combinations(range(n), half):
        first_half = [array[i] for i in indices]
        second_half = [elem for j, elem in enumerate(array) if j not in indices]
        first_half.sort()
        second_half.sort()
        combination = (tuple(first_half), tuple(second_half))
        combinations_set.add(combination)
 
    return combinations_set

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
combinations = divide_array(A)
print("Количество комбинаций:", len(combinations))
print("Список комбинаций:")

for combination in combinations:
    print(combination)