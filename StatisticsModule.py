#Python statistics module provides the functions to mathematical statistics of numeric data.
import statistics

dataset = [5, 9, 15, 16, 19, 27, 28, 28]  

x=statistics.mean(dataset)
print("Mean is: ",x) # (5+9+15+16+19+27+28+28)/8=18.375

x=statistics.median(dataset)
print("Median is: ",x)   #data is even so (16+19/2=17.5) it returns 17.5, if odd it return middle value in DS
x=statistics.median_low(dataset)
print("Low Median is: ",x) #smaller than and value near to 17.5 in DS i.e 16
x=statistics.median_high(dataset)
print("High Median is: ",x) #greater than and value near to 17.5 in DS i.e 19

x=statistics.mode(dataset)
print("Mode is: ",x) #returns 28 because it appeared frequently

x=statistics.stdev(dataset)
print("Standard Deviation is: ",x)

x=statistics.variance(dataset)
print("Variance is: ",x)

x=statistics._sum(dataset)
print("Type of data, Addition of data of 1st column and no of elements in DS is: \n",x)

"""Output:
Mean is:  18.375
Median is:  17.5
Low Median is:  16
High Median is:  19
Mode is:  28
Standard Deviation is:  8.814557763803501
Variance is:  77.69642857142857
Type of data, Addition of data of 1st column and no of elements in DS is: 
 (<class 'int'>, Fraction(147, 1), 8)
 """
