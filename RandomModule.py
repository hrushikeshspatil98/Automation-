import random

#Get 10 random numbers
for i in range (0,10):
    print(random.randrange(0,100),end=" ") #randrange() returns a random number between the given range

#Get  random int number
print("\n",random.randint(100,200))  #randint() returns a random int number between the given range

#Get 3 random float numbers
for i in range (0,3):
    print(random.uniform(0,10.5),end=" ") #uniform() returns a random float number between given range

# getrandbits() method returns an integer in the specified size.Size is in bits, if 3 bits value are in range 0 to 7
#000,001,010,011,100,101,110,111
print("\n",random.getrandbits(3)) 

numList=[10,20,30,40,50,60,70,80]
print(random.choice(numList)) #It returns a random element from the specified sequence.

random.shuffle(numList)  #It takes a sequence and rearrange the order of the items.
print("List is: ",numList)

'''Output:
76 60 73 3 22 79 76 5 60 27 
132
8.755953712946393 4.370068699909414 1.5531761848305905 
5
80
List is:  [30, 80, 10, 70, 40, 20, 50, 60]
'''
