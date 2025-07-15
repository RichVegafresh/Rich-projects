# Rich-projects
Learning journey
#write a program to calculate the Area of a rectangle
import math
while True:
  try:
    length = float(input("Enter the length of the rectangle:, "))
    break
  except ValueError:
    print("Please enter a valid number")
while True:
  try:
    width = float(input("Enter the value of the rectangle:, "))
    break
  except ValueError:
    print("Please enter a valid number")

Area = (length * width)
print("The Area of the Rectangle is:", Area)
