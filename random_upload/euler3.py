def prime_factorization(input):
    factors = []
    lastnum = input
    divisor = 2
    for i in range(input):
        if lastnum % divisor != 0:
            divisor += 1
        else:
            factors.append(divisor)
            lastnum /= divisor
    return factors
