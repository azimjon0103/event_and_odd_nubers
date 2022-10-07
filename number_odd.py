#A four-digit integer is given. Find the number of odd digits in it.
from re import A


var_int=3756
#Create a variable "var_int" and assign it a four-digit integer value.
b=var_int//1000%2
d=var_int-b*1000
c=d//100%2
e=d-c*100
f=e//10%2
g=e-f*10 
h=g%2
#Print the number of odd digits in the variable "var_int".
a=b+c+f+h
print(a)