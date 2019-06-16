# Q1. Write a Python program to find the repeated items of a tuple.
#
# tuple_var = (2,4,5,6,7,4,4,7)
# print(tuple_var)
#
# a = int(input("enter no. you want to check: "))
# count = tuple_var.count(a)
# print(count)



# Q2. Write a Python program to replace last value of a list.

# list_var=[1,2,'abc','def',3.21,6.15,True,22,12]
# print(list_var)
# list_var[8]='hello'
# print(list_var)


# Q3. Write a Python script to merge two Python dictionaries.
#
# dict1 = {'a': 100, 'b': 200}
# dict2 = {'x': 300, 'y': 200}
#
# print(dict1)
# print(dict2)
#
# dict = dict2.copy()
# dict.update(dict1)
# print(dict)



# Q4. Write a Python program to combine two dictionary adding values for common keys.
#
# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(d1)
# print(d2)
# d = Counter(d1) + Counter(d2)
# print(d)




# Q6. Write a function that takes multiple inputs from the user and perform mathematical operation on all the numbers. e.g.
#     if the numbers sent are -2,3,4,their result for addition is: 9, multiplication is:24.
#
# def fun():
#     a=int(input("enter first no.:"))
#     b=int(input("enter second no.:"))
#     operator=input("enter any operator")
#     if (operator=='+'):
#         return a + b
#     elif(operator=='-'):
#         if(b>a):
#             return b-a
#         else:
#             return a-b
#     elif (operator=='*'):
#         return a * b
#     elif (operator=='/'):
#         return a/b
#     else:
#         return ('error, Try again.')
#
# var=fun()
# print("result is: ",var)




# Q7. Take a list from the user and get a list where all the elements from the list are shuffled.

# from random import shuffle
# input_list=[(input('enter any value')) for i in range(1,7)]
# print(input_list)
#
# shuffle(input_list)
# print(input_list)



# Q8. What is the difference between range and xrange?

# range returns  a python list object and xrange returns an xrange object.
# It means  that xrange does not actually generate a static list at run time like range does.
# from pip._vendor.msgpack.fallback import xrange

#  program-

# for i in xrange(10):
#     print(i)
#
# for i in range(10):
#     print(i)




# Q9. I have a tuple_var = (10,35,12,8,32). What will the program return, if I use print(tuple_var[:10]) and
#     print(tuple_var[10]).

# tuple_var=(10,35,12,8,32)
# print(tuple_var)
# print(tuple_var[:10])  // it will execute properly.
# print(tuple_var[10])  // error will come = IndexError: tuple index out of range



# Q10. What is the use of ** operator in python? Using this operator print the square of 5.

#  ** is a Exponent Operator.
# It returns the exponential power.
# Statement m**n will be calculated as "m to the power of n".

# program-

# number = int (input ("Enter an integer number: "))
#
# square = number**2
# print ("Square of {0} is {1} ".format (number, square))