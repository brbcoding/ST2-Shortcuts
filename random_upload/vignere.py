import string
import math

def encrypt(message, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    no_spaces = message.replace(' ', '')
    message_letters = list(no_spaces)
    key_list = list(key)
    alpha_values = []
    key_values = []
    sum_values = []
    i = 0
    n = 0    
    x = 0
    #this while loop will get all the values of the letters in the string to be encrypted (later to be added to values of the key
    while i < len(no_spaces):
        vals = alphabet.index(message_letters[i])
        alpha_values.append(vals)
        i = i + 1
    while n < len(key):
        vals = alphabet.index(key_list[n])
        n = n + 1
        key_values.append(vals)
    message_length = len(no_spaces)
    key_length = len(key)
    key_length = float(key_length)
    num_times = int(math.ceil(message_length/key_length))
    new_key = key_values * num_times
    alpha_length = len(alpha_values)
    final_key = new_key[:alpha_length]
    x = 0
    while x < len(no_spaces):
        sum = alpha_values[x] + final_key[x]
        sum_values.append(sum)
        x = x + 1
    print sum_values
    #now we need to get the corresponding letter
    
    
    
    
    
    
    
    
    







