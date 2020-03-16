# Created by Kamil krawczyk
# 03/15/2020


#Problem 2
#This program creates a list with the numbers 0 to 10. It then adds the current value on the counter until the counter reaches 10.

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = 0

while num <= 10:
  L.append(num)
  num += 1

print(L)