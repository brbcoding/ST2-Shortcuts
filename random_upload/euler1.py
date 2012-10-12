def sum_multiples(n):
    nums = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    total = sum(nums)
    print total
