def check_all_mappings():
 mappings_result = {}
 for mapping in mappings:
 mapping_result = {}
 mapping_result['A'] = all(check_mapping_for_A(A[0], A[1], mapping) for A in 
zip(A, B))
 mapping_result['B'] = check_mapping_for_B(*B, mapping)
 mapping_result['C'] = check_mapping_for_C(*C, mapping)
 mapping_result['D'] = check_mapping_for_D(*D, mapping)
 mapping_result['E'] = check_mapping_for_E(*E, mapping)
 mappings_result[str(mapping)] = mapping_result
 return mappings_result
results = check_all_mappings()
print(results)
def find_valid_mappings():
 valid_mappings = []
 for mapping in mappings:
 if (check_mapping_for_A(A[0], A[1], mapping) and
 check_mapping_for_B(B[0], B[1], B[2], B[3], B[4] , B[5] , mapping) and
 check_mapping_for_C(C[0], C[1], C[2], C[3], C[4], C[5], mapping) and
 check_mapping_for_D(D[0], D[1], D[2], D[3], mapping) and
 check_mapping_for_E(E[0], E[1], E[2], mapping)):
 valid_mappings.append(mapping)
 return valid_mappings
def get_ABCDE_from_mapping(mapping):
 A_indices = [i for i, x in enumerate(mapping) if x == 0]
 B_indices = [i for i, x in enumerate(mapping) if x == 1]
 C_indices = [i for i, x in enumerate(mapping) if x == 2]
 D_indices = [i for i, x in enumerate(mapping) if x == 3]
 E_indices = [i for i, x in enumerate(mapping) if x == 4]
 
 A_values = [A[0][i] if i < len(A[0]) else A[1][i - len(A[0])] for i in A_indices]
 B_values = [B[0][i] if i < len(B[0]) else B[1][i - len(B[0])] if i < len(B[0]) + len(B[1])
 else B[2][i - len(B[0]) - len(B[1])] if i < len(B[0]) + len(B[1]) + len(B[2])
 else B[3][i - len(B[0]) - len(B[1]) - len(B[2])] if i < len(B[0]) + len(B[1]) + 
len(B[2]) + len(B[3])
 else B[4][i - len(B[0]) - len(B[1]) - len(B[2]) - len(B[3])] if i < len(B[0]) + 
len(B[1]) + len(B[2]) + len(B[3]) + len(B[4])
 else B[5][i - len(B[0]) - len(B[1]) - len(B[2]) - len(B[3]) - len(B[4])] for i in 
B_indices]
 C_values = [C[0][i] if i < len(C[0]) else C[1][i - len(C[0])] if i < len(C[0]) + len(C[1])
 else C[2][i - len(C[0]) - len(C[1])] if i < len(C[0]) + len(C[1]) + len(C[2])
 else C[3][i - len(C[0]) - len(C[1]) - len(C[2])] if i < len(C[0]) + len(C[1]) + 
len(C[2]) + len(C[3])
 else C[4][i - len(C[0]) - len(C[1]) - len(C[2]) - len(C[3])] if i < len(C[0]) + 
len(C[1]) + len(C[2]) + len(C[3]) + len(C[4])
 else C[5][i - len(C[0]) - len(C[1]) - len(C[2]) - len(C[3]) - len(C[4])] for i in 
C_indices]
 D_values = [D[0][i] if i < len(D[0]) else D[1][i - len(D[0])] if i < len(D[0]) + len(D[1])
 else D[2][i - len(D[0]) - len(D[1])] if i < len(D[0]) + len(D[1]) + len(D[2])
 else D[3][i - len(D[0]) - len(D[1]) - len(D[2])] for i in D_indices]
 E_values = [E[0][i] if i < len(E[0]) else E[1][i - len(E[0])] if i < len(E[0]) + len(E[1])
 else E[2][i - len(E[0]) - len(E[1])] for i in E_indices]
 
 return A_values, B_values, C_values, D_values, E_values
valid_mappings = find_valid_mappings()
ABCDE_combinations = [get_ABCDE_from_mapping(mapping) for mapping in 
valid_mappings]
print(valid_mappings)
print(ABCDE_combinations)
with open("output11.txt", "w") as file:
 for mapping in valid_mappings:
 A_values, B_values, C_values, D_values, E_values = 
get_ABCDE_from_mapping(mapping)
 if len(A_values) > 1:
 file.write(f"A = {[A_values[:6], A_values[6:]]}\n")
 if len(B_values) > 1:
 file.write(f"B = {[B_values[i:i+2] for i in range(0, len(B_values), 2)]}\n")
 if len(C_values) > 1:
 file.write(f"C = {[C_values[i:i+2] for i in range(0, len(C_values), 2)]}\n")
 if len(D_values) > 1:
 file.write(f"D = {[D_values[i:i+3] for i in range(0, len(D_values), 3)]}\n")
 if len(E_values) > 1:
 file.write(f"E = {[E_values[i:i+4] for i in range(0, len(E_values), 4)]}\n")
output_strings = []
with open("output11.txt", "r") as file:
 for line in file:
 output_strings.append(line.strip())
sorted_output_strings = sorted(output_strings, key=len, reverse=True)
for i in range(5):
 print(sorted_output_strings[i])