#Command Line Arguments

import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

#argv[0] contains program name and argv[1] contains input string
inputString=sys.argv[1]
print("String is: ",inputString)
reverseString=""
for i in inputString[::-1]:
    reverseString=reverseString+i

print("Reverse String is: ",reverseString)

'''
Run Command: >> python main.py python

Output:
Number of arguments: 2 arguments.                                                                                  
Argument List: ['main.py', 'python']                                                                               
String is:  python                                                                                                 
Reverse String is:  nohtyp 
'''
