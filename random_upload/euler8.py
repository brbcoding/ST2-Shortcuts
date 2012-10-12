def greatest_product(input):
    products = []
    digits = list(str(input))
    for i in range(len(digits)-4):
        product = int(digits[i]) * int(digits[i+1]) * int(digits[i+2]) * int(digits[i+3]) * int(digits[i+4])
        products.append(product)
    return max(products)
