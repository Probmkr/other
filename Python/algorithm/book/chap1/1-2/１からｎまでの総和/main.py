n = 55555555  # int(input('n : '))


def first(n):  # 6.4秒
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum
# 見よ、この二つの差を。


def second(n):  # 3.5秒
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def fastest(n): # wwww こっちは比べもんになんない
    return n * (n + 1) // 2

print(fastest(n))
