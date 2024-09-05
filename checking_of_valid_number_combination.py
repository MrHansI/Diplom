A = [[0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9, 11]]
B = [[0, 1], [2,3] ,[4,11],[5,6],[7,8],[9,10]]
C = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]]
D = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]
E = [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]]
def check_mapping_for_E(E1, E2, E3, mapping):
    mapping_set = set(mapping)
    E1_set = set(E1)
    E2_set = set(E2)
    E3_set = set(E3)
    if len(mapping_set) == 1:
        return True
    if all(x in E2_set or x in E3_set or x not in mapping_set for x in E1):
        return True
    if all(x in E1_set or x in E3_set or x not in mapping_set for x in E2):
        return True
    if all(x in E1_set or x in E2_set or x not in mapping_set for x in E3):
        return True
    if all((x == y) or (x in E1_set and y in E1_set) or (x in E2_set and y in E2_set)
        or (x in E3_set and y in E3_set)
    for x, y in enumerate(mapping)):
        return True
    return False
def check_mapping_for_D(D1, D2, D3, D4, mapping):
    mapping_set = set(mapping)
    D1_set = set(D1)
    D2_set = set(D2)
    D3_set = set(D3)
    D4_set = set(D4)
    if len(mapping_set) == 1:
        return True
    if all(x in D2_set or x in D3_set or x in D4_set or x not in mapping_set for x in 
    D1):
        return True
    if all(x in D1_set or x in D3_set or x in D4_set or x not in mapping_set for x in 
    D2):
        return True
    if all(x in D1_set or x in D2_set or x in D4_set or x not in mapping_set for x in 
    D3):
 return True
 if all(x in D1_set or x in D2_set or x in D3_set or x not in mapping_set for x in 
D4):
 return True
 if all((x == y) or (x in D1_set and y in D1_set) or (x in D2_set and y in D2_set)
 or (x in D3_set and y in D3_set) or (x in D4_set and y in D4_set)
 for x, y in enumerate(mapping)):
 return True
 return False
def check_mapping_for_C(C1, C2, C3, C4, C5, C6, mapping):
 mapping_set = set(mapping)
 C1_set = set(C1)
 C2_set = set(C2)
 C3_set = set(C3)
 C4_set = set(C4)
 C5_set = set(C5)
 C6_set = set(C6)
 if len(mapping_set) == 1:
 return True
 if all(x in C2_set or x in C3_set or x in C4_set or x in C5_set or x in C6_set or x 
not in mapping_set for x in C1):
 return True
 if all(x in C1_set or x in C3_set or x in C4_set or x in C5_set or x in C6_set or x 
not in mapping_set for x in C2):
 return True
 if all(x in C2_set or x in C1_set or x in C4_set or x in C5_set or x in C6_set or x 
not in mapping_set for x in C3):
 return True
 if all(x in C2_set or x in C3_set or x in C1_set or x in C5_set or x in C6_set or x 
not in mapping_set for x in C4):
 return True
 if all(x in C2_set or x in C3_set or x in C4_set or x in C1_set or x in C6_set or x 
not in mapping_set for x in C5):
 return True
 if all(x in C2_set or x in C3_set or x in C4_set or x in C5_set or x in C1_set or x 
not in mapping_set for x in C6):
 return True
 if all((x == y) or (x in C1_set and y in C1_set) or (x in C2_set and y in C2_set)
 or (x in C3_set and y in C3_set) or (x in C4_set and y in C4_set)
 or (x in C5_set and y in C5_set) or (x in C6_set and y in C6_set)
 for x, y in enumerate(mapping)):
 return True
def check_mapping_for_A(A1, A2, mapping):
 mapping_set = set(mapping)
 A1_set = set(A1)
 A2_set = set(A2)
 if len(mapping_set) == 1:
 return True
 if all(x in A2_set or x not in mapping_set for x in A1):
 return True
 if all(x in A1_set or x not in mapping_set for x in A2):
 return True
 if all((x == y) or (x in A1_set and y in A1_set) or (x in A2_set and y in A2_set)
 for x, y in enumerate(mapping)):
 return True
 return False
def check_mapping_for_B(B1, B2, B3, B4, B5, B6, mapping):
 mapping_set = set(mapping)
 B1_set = set(B1)
 B2_set = set(B2)
 B3_set = set(B3)
 B4_set = set(B4)
 B5_set = set(B5)
 B6_set = set(B6)
 if len(mapping_set) == 1:
 return True
 if all(x in B2_set or x in B3_set or x in B4_set or x in B5_set or x in B6_set or x 
not in mapping_set for x in B1):
 return True
 if all(x in B1_set or x in B3_set or x in B4_set or x in B5_set or x in B6_set or x 
not in mapping_set for x in B2):
 return True
 if all(x in B1_set or x in B2_set or x in B4_set or x in B5_set or x in B6_set or x 
not in mapping_set for x in B3):
 return True
 if all(x in B1_set or x in B2_set or x in B3_set or x in B5_set or x in B6_set or x 
not in mapping_set for x in B4):
 return True
 if all(x in B2_set or x in B3_set or x in B4_set or x in B1_set or x in B6_set or x 
not in mapping_set for x in B5):
 return True
 if all(x in B2_set or x in B3_set or x in B4_set or x in B5_set or x in B1_set or x 
not in mapping_set for x in B6):
 return True
 if all((x == y) or (x in B1_set and y in B1_set) or (x in B2_set and y in B2_set)
 or (x in B3_set and y in B3_set) or (x in B4_set and y in B4_set)
 or (x in B5_set and y in B5_set) or (x in B6_set and y in B6_set)
 for x, y in enumerate(mapping)):
 return True
 return check(B1, mapping) and check(B2, mapping) and check(B3, mapping) 
and check(B4, mapping) and check(B5, mapping) and check(B6, mapping)
 return False
mappings = [
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
 [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
 [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
 [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
 [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
 [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
 
 ]
def check_all_mappings():
 mappings_result = {}
 for mapping in mappings:
 mapping_result = {}
 mapping_result['A'] = all(check_mapping_for_A(A[0], A[1], mapping) for A 
in zip(A, B))
 mapping_result['B'] = check_mapping_for_B(*B, mapping)
 mapping_result['C'] = check_mapping_for_C(*C, mapping)
 mapping_result['D'] = check_mapping_for_D(*D, mapping)
 mapping_result['E'] = check_mapping_for_E(*E, mapping)
 mappings_result[str(mapping)] = mapping_result
 return mappings_result
results = check_all_mappings()
for mapping, mapping_result in results.items():
 print("Mapping:", mapping)
 for matrix, is_correct in mapping_result.items():
 print(f"Matrix {matrix}: {'Correct' if is_correct else 'Incorrect'}")