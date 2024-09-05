bell = [[0 for _ in range(n+1)] for _ in range(n+1)]
 bell[0][0] = 1
 for i in range(1, n+1):
 bell[i][0] = bell[i-1][i-1]
 for j in range(1, i+1):
 bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
 return bell[n][0]
n = 12
print(f"Число Белла для {n} равно {bell_number(n)}")