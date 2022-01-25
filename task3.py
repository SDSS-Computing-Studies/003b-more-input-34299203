#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
import math
a = input("Enter your first price")
b = input("Enter your second price")
c = input("Enter your three price")
d = input("Enter your forth price")
e = input("Enter your fifth price")
a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)


l = a+b+c+d+e
k = l*0.12
v = l+k
v = round(v,2)
l = round(l,2)
k = round(k,2)
v = str(v)
k = str(k)
l = str(l)
print("Your subtotal is $" + l + " and your taxes total $" +k+ " for a total of $"+v+"")

