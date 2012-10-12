morse_dictionary = {'a':'.-', 
                    'b':'-...', 
                    'c':'-.-.', 
                    'd':'-..', 
                    'e':'.', 
                    'f':'..-.', 
                    'g':'--.', 
                    'h':'....', 
                    'i':'..', 
                    'j':'.---', 
                    'k':'-.-', 
                    'l':'.-..', 
                    'm':'--', 
                    'n':'-.', 
                    'o':'---', 
                    'p':'.--.', 
                    'q':'--.-', 
                    'r':'.-.', 
                    's':'...', 
                    't':'-', 
                    'u':'..-', 
                    'v':'...-', 
                    'w':'.--', 
                    'x':'-..-', 
                    'y':'-.--', 
                    'z':'--..', 
                    '1':'.----', 
                    '2':'..---', 
                    '3':'...--', 
                    '4':'....-', 
                    '5':'.....', 
                    '6':'-....', 
                    '7':'--...', 
                    '8':'---..', 
                    '9':'----.', 
                    '0':'-----', 
                    ',':'--..--', 
                    '.':'.-.-.-', 
                    '?':'..--..', 
                    '/':'-..-.', 
                    '-':'-....-', 
                    '(':'-.--.', 
                    ')':'-.--.-'}
def convert(input):
    # check if input is morse or abc's
    # if it doesn't begin with . or -, it's
    # alphabetic... convert to morse
    if input[0] == '.' or input[0] == '-':
        alphabetic = []
        abc = dict((value,key) for key,value in morse_dictionary.iteritems())
        abc[''] = ' '
        letters = input.split(' ')
        for i in range(len(letters)):
            if letters[i] in letters:
                alphabetic.append(abc[letters[i]])
        alpha_str = ''.join(alphabetic)
        final_str = alpha_str.replace('   ',' ')
        return final_str   
    else:
        morse = []
        letters = list(input)
        for i in range(len(letters)):
            if letters[i] == ' ':
                morse.append('  ')
            else:
                morse.append(morse_dictionary[letters[i]])
        final_str = ' '.join(morse)
        return final_str

                
