def fibonacci(n):
    if n <= 0:
        return []

    elif n == 1:
        return [0]

    else:
        prev2 = 0
        prev1 = 1
        current = 0

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current


print(fibonacci(10000))
