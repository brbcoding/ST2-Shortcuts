sum_squares, sum = 0,  0
for i in range (101):
    sum_squares = sum_squares + i**2
for i in range (101):
    sum = sum + i
squares_sum = sum ** 2
answer = squares_sum - sum_squares
print answer
    
        
    
    
