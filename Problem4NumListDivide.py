# Created by Kamil krawczyk
# 03/15/2020


#Problem 4
#This problem creates a a counter that starts at 0 and goes up to 50. When it reaches a number divisible by 10, it puts it in a list.
#Prints out the numbers that are divisible by 10.

tens = []

num = 0

while num <= 50:
  if num % 10 == 0:
    tens.append(num)
  num += 1


print(tens)