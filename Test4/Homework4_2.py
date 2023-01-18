def factor_recursive(n):
    if n == 1:
        return n
    else:
        return n * factor_recursive(n - 1)


print(factor_recursive(4))
