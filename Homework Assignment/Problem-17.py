def factorial(n):
    result = [1]

    for num in range(2, n + 1):
        carry = 0
        for i in range(len(result)):
            product = result[i] * num + carry
            result[i] = product % 10
            carry = product // 10

        while carry:
            result.append(carry % 10)
            carry //= 10

    return result[::-1]


print(factorial(5))
print(factorial(10))

