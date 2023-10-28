n = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(n)]
prime_diagonal = [matrix[i][i] for i in range(n)]
sec_diagonal = [matrix[i][-i -1] for i in range(n)]

print(sec_diagonal)
print(f'{abs(sum(prime_diagonal) - sum(sec_diagonal))}')
