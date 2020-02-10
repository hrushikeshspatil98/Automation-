#5 break and continue
string="pythaon"
for i in string:
    if (i=='t'):
        break
    print(i,end='')
print()
for i in string:
    if (i=='a'):
        continue
    print(i,end='')
    
"""
Output:
py
python 
"""
