#Functions
'''
def fun_name(parameters):
    logic
func_name(arguments)
func_name(arguments)
'''


def hello(student_name):
    print("Good Morning ",student_name)
# hello("Harry","Sam")
# hello("Sam")

# string formatting 
# a,b,c,d,age = "harry","sam","john","peter",15
# print("My first name is",a,"My second name is",b,"My third name is",c,"My fourth name is",d,"i am ",age,"yrs old")
# print(f"My first name is {a}. My second name is {b}. My third name is {c}. My fourth name is {d} I am {age}yrs old")

# *args

# def display(*students):
#     for i in students:
#         print(i)
# display("Harry","Sam","John")

'''

Create a function that takes a number as an argument,
 increments the number by +1 and returns the result.

Examples
addition(0) ➞ 1

addition(9) ➞ 10

addition(-3) ➞ -2
Notes
Don't forget to return the result.
'''
def addition(numb):
    return numb+1
print(addition(-3))
'''
Create a function that finds the maximum range of a triangle's third edge,
 where the side lengths are all integers.

Examples
next_edge(8, 10) ➞ 17

next_edge(5, 7) ➞ 11

next_edge(9, 2) ➞ 10
Notes
(side1 + side2) - 1 = maximum range of third edge.

Q2:-
Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has 
obtained so far.

wins get 3 points
draws get 1 point
losses get 0 points
Examples
football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0
Notes
Inputs will be numbers greater than or equal to 0.

Q3:-
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals.
 The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. 
You have to implement a function that returns the total number of legs of all the animals.

Examples
animals(2, 3, 5) ➞ 36     ->2*2 + 3*4 + 5*4 = 36

animals(1, 2, 3) ➞ 22

animals(5, 2, 8) ➞ 50
Notes
Don't forget to return the result.
The order of animals passed is animals(chickens, cows, pigs).
Remember that the farmer wants to know the total number of legs and not the total number of animals.


Q4:-
Create a function that takes a list and returns the difference between the biggest and smallest numbers.

Examples
difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32. 32 - (-50) 32+50 = 82

difference_max_min([44, 32, 86, 19]) ➞ 67
# Smallest number is 19, biggest is 86.

.sort
sorting lst  0  = min   len -1 = max
'''


def display(*students):
    print(f"first name is {students[1]}")

display("Harry","Sam","John")