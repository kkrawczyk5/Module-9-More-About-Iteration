# Created by Kamil Krawczyk
# 03/11/2020


# Problem 3
# This program asks for a user input and adds the numbers until it reaches 100


num = 0
print("enter a number - ")
n = int(input())
while n != 0:
  num += n
  if num >= 100:
      print('Total sum is', num)
      break
  print("Enter another nunber - ")    
  n = int(input())
