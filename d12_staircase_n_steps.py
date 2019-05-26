# def staircase(n):
#     if n <= 1:
#         return 1
#     return staircase(n - 1) + staircase(n - 2)

# def staircase(n):
#     a, b = 1, 2
#     for _ in range(n - 1):
#         a, b = b, a + b
#     return a

# def staircase(n, X):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return sum(staircase(n - x, X) for x in X)

def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

X = [1,2,5]
print(staircase(4, X))