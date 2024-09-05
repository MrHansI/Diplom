#С помощью данного кода можно построить таблицу отображений и проверить были ли найдены все элементы 
def multiply_permutations(perm1,perm2):
    if len(perm1) != len(perm2):
        raise ValueError("Длины перестановок должны быть одинаковыми")
 
    perm1_dict = dict(enumerate(perm1))
    perm2_dict = dict(enumerate(perm2))
 
    result_perm_dict = {}
    for i in range(len(perm1)):
        result_perm_dict[i] = perm2_dict[perm1[i]] 
 
        result_perm = [result_perm_dict[i] for i in range(len(perm1))]
 
    return result_perm

k1 = [0,0,0,0,0,0,0,0,0,0,0,0]
k2 = [0,1,2,3,4,5,6,7,8,9,10,11]
k3 = [1,1,1,1,1,1,1,1,1,1,1,1]
k4 = [2,2,2,2,2,2,2,2,2,2,2,2]
k5 = [3,3,3,3,3,3,3,3,3,3,3,3]
k6 = [4,4,4,4,4,4,4,4,4,4,4,4]
k7 = [5,5,5,5,5,5,5,5,5,5,5,5]
k8 = [6,6,6,6,6,6,6,6,6,6,6,6]
k9 = [7,7,7,7,7,7,7,7,7,7,7,7]
k10 = [8,8,8,8,8,8,8,8,8,8,8,8]
k11 = [9,9,9,9,9,9,9,9,9,9,9,9]
k12 = [10,10,10,10,10,10,10,10,10,10,10,10]
k13 = [11,11,11,11,11,11,11,11,11,11,11,11]

permutations = [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10,
 k11, k12 , k13]

with open("matrix2.txt", "w") as file:
    for i, perm1 in enumerate(permutations):
        for j, perm2 in enumerate(permutations):
            result = multiply_permutations(perm1, perm2)
            file.write(f"k{i+1} * k{j+1} = {result}\n")
