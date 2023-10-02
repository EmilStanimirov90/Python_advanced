n, m = input().split()
n_set = set()
m_set = set()
for _ in range(int(n)):
    n_set.add(input())
for _ in range(int(m)):
    m_set.add(input())

print("\n".join(n_set & m_set))
